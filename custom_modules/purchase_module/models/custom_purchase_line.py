from odoo import api, fields, models


class CustomPurchaseLine(models.Model):
    _name = "custom.purchase.line"
    _description = "Custom Purchase Line"

    # Parent relational field
    purchase_id = fields.Many2one(
        comodel_name="custom.purchase",
        string="Purchase Reference",
        ondelete="cascade",
    )

    # Product and measurement fields
    product_id = fields.Many2one(
        comodel_name="product.product",
        string="Product",
        required=True,
    )
    product_name = fields.Char(string="Product Name")
    quantity = fields.Float(string="Quantity", default=1.0)
    price_unit = fields.Float(string="Unit Price", digits="Product Price")
    subtotal = fields.Float(
        string="Subtotal",
        compute="_compute_subtotal",
        store=True,
    )
    uom_id = fields.Many2one(
        comodel_name="uom.uom",
        string="Unit of Measure",
    )

    # Compute methods
    @api.depends("quantity", "price_unit")
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit

    # Onchange methods
    @api.onchange("product_id")
    def _onchange_product_id(self):
        for line in self:
            if line.product_id:
                line.product_name = line.product_id.display_name
                line.price_unit = line.product_id.list_price
                line.uom_id = line.product_id.uom_id
            else:
                line.product_name = False
                line.price_unit = 0.0
                line.uom_id = False

    # Action methods
    def action_discard_line(self):
        """Delete this purchase line record."""
        self.unlink()