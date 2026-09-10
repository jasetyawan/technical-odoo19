from odoo import api, fields, models


class CustomPurchaseLine(models.Model):
    _name = "custom.purchase.line"
    _description = "Custom Purchase Line"

    purchase_id = fields.Many2one(
        comodel_name="custom.purchase",
        string="Purchase Reference",
        ondelete="cascade",
    )
    product_id = fields.Many2one(
        comodel_name="product.product",
        string="Product",
        required=True,
    )
    product_name = fields.Char(string="Product Name")
    quantity = fields.Float(string="Quantity", default=1.0)
    price_unit = fields.Float(string="Unit Price", digits="Product Price")
    uom_id = fields.Many2one(
        comodel_name="uom.uom",
        string="Unit of Measure",
    )

    @api.onchange("product_id")
    def _onchange_product_id(self):
        for line in self:
            if line.product_id:
                line.product_name = line.product_id.display_name
                line.price_unit = line.product_id.list_price
                line.uom_id = line.product_id.uom_id.id