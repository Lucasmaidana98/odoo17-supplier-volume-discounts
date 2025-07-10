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