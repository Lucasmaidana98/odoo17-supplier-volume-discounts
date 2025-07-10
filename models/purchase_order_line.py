from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_category_id = fields.Many2one(
        'product.category',
        string='Product Category',
        related='product_id.product_tmpl_id.categ_id',
        readonly=True,
        help="Category of the product"
    )
    
    product_category_name = fields.Char(
        string='Category',
        related='product_category_id.name',
        readonly=True,
        help="Name of the product category"
    )

    @api.onchange('product_id')
    def _onchange_product_id_update_category(self):
        if self.product_id:
            self.product_category_id = self.product_id.product_tmpl_id.categ_id
            
    @api.onchange('product_qty', 'price_unit', 'product_id')
    def _onchange_volume_discount_auto_apply(self):
        """Auto-apply volume discount when quantity, price, or product changes"""
        if not self.order_id or not self.order_id.partner_id or not self.product_id:
            return
            
        # Calculate current line subtotal
        current_subtotal = (self.product_qty or 0) * (self.price_unit or 0)
        
        # Calculate total of all lines including current changes
        order_total = 0
        for line in self.order_id.order_line:
            if line.product_id:
                if line.id == self.id or line == self:
                    # Use current values for this line
                    order_total += current_subtotal
                else:
                    # Use saved values for other lines
                    order_total += line.price_subtotal
        
        # Get supplier discount settings
        supplier_discount = self.order_id.partner_id.volume_discount_percentage
        min_amount = self.order_id.partner_id.minimum_purchase_amount
        
        # Apply discount if conditions are met
        if order_total >= min_amount and supplier_discount > 0:
            if self.discount != supplier_discount:
                self.discount = supplier_discount
        else:
            # Remove discount if conditions are not met
            if self.discount > 0:
                self.discount = 0.0
                
    @api.model_create_multi
    def create(self, vals_list):
        """Apply volume discount on creation if conditions are met"""
        lines = super().create(vals_list)
        for line in lines:
            if line.order_id and line.order_id.partner_id and line.product_id:
                order_total = sum(l.price_subtotal for l in line.order_id.order_line if l.product_id)
                supplier_discount = line.order_id.partner_id.volume_discount_percentage
                min_amount = line.order_id.partner_id.minimum_purchase_amount
                
                if order_total >= min_amount and supplier_discount > 0:
                    line.discount = supplier_discount
        return lines