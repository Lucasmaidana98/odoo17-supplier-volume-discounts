from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    volume_discount_percentage = fields.Float(
        string='Volume Discount (%)',
        digits=(16, 2),
        help="Percentage discount applied when minimum purchase amount is reached",
        default=0.0
    )
    
    minimum_purchase_amount = fields.Monetary(
        string='Minimum Purchase Amount',
        currency_field='currency_id',
        help="Minimum amount required to qualify for volume discount",
        default=0.0
    )

    @api.constrains('volume_discount_percentage')
    def _check_volume_discount_percentage(self):
        for partner in self:
            if partner.volume_discount_percentage < 0 or partner.volume_discount_percentage > 100:
                raise models.ValidationError("Volume discount percentage must be between 0 and 100.")

    @api.constrains('minimum_purchase_amount')
    def _check_minimum_purchase_amount(self):
        for partner in self:
            if partner.minimum_purchase_amount < 0:
                raise models.ValidationError("Minimum purchase amount must be positive.")