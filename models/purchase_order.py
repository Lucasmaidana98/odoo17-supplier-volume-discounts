from odoo import models, fields, api
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    supplier_volume_discount_percentage = fields.Float(
        string='Supplier Volume Discount (%)',
        related='partner_id.volume_discount_percentage',
        readonly=True,
        help="Volume discount percentage from supplier"
    )
    
    supplier_minimum_purchase_amount = fields.Monetary(
        string='Supplier Minimum Purchase Amount',
        related='partner_id.minimum_purchase_amount',
        readonly=True,
        help="Minimum purchase amount required for volume discount"
    )
    
    qualifies_for_discount = fields.Boolean(
        string='Qualifies for Volume Discount',
        compute='_compute_qualifies_for_discount',
        store=True,
        help="True if order amount exceeds minimum purchase amount"
    )
    
    total_discount_amount = fields.Monetary(
        string='Total Discount Amount',
        compute='_compute_discount_amounts',
        store=True,
        help="Total amount saved due to volume discount"
    )
    
    amount_without_discount = fields.Monetary(
        string='Amount Without Discount',
        compute='_compute_discount_amounts',
        store=True,
        help="Total amount before volume discount"
    )
    
    discount_percentage_savings = fields.Float(
        string='Discount Percentage Savings',
        compute='_compute_discount_amounts',
        store=True,
        help="Percentage of savings compared to original amount"
    )

    @api.depends('amount_untaxed', 'supplier_minimum_purchase_amount')
    def _compute_qualifies_for_discount(self):
        for order in self:
            order.qualifies_for_discount = (
                order.amount_untaxed >= order.supplier_minimum_purchase_amount
                and order.supplier_minimum_purchase_amount > 0
                and order.supplier_volume_discount_percentage > 0
            )

    @api.depends('amount_untaxed', 'qualifies_for_discount', 'supplier_volume_discount_percentage')
    def _compute_discount_amounts(self):
        for order in self:
            if order.qualifies_for_discount:
                order.amount_without_discount = order.amount_untaxed / (1 - order.supplier_volume_discount_percentage / 100)
                order.total_discount_amount = order.amount_without_discount - order.amount_untaxed
                if order.amount_without_discount > 0:
                    order.discount_percentage_savings = (order.total_discount_amount / order.amount_without_discount) * 100
                else:
                    order.discount_percentage_savings = 0.0
            else:
                order.amount_without_discount = order.amount_untaxed
                order.total_discount_amount = 0.0
                order.discount_percentage_savings = 0.0

    @api.onchange('partner_id')
    def _onchange_partner_id_apply_discount(self):
        if self.partner_id:
            self._apply_volume_discount()

    def _apply_volume_discount(self):
        if self.qualifies_for_discount:
            discount_percentage = self.supplier_volume_discount_percentage
            for line in self.order_line:
                if line.product_id:
                    line.discount = discount_percentage

    def button_confirm(self):
        products_without_supplier = []
        for order in self:
            for line in order.order_line:
                if line.product_id and line.product_id.product_tmpl_id.seller_ids:
                    main_supplier = line.product_id.product_tmpl_id.seller_ids[0]
                    if not main_supplier:
                        products_without_supplier.append(line.product_id.display_name)
                elif line.product_id:
                    products_without_supplier.append(line.product_id.display_name)
        
        if products_without_supplier:
            raise UserError(
                "Cannot confirm purchase order. The following products do not have a main supplier defined:\n" +
                "\n".join(f"- {product}" for product in products_without_supplier) +
                "\n\nPlease assign a main supplier to these products before confirming the order."
            )
        
        return super(PurchaseOrder, self).button_confirm()