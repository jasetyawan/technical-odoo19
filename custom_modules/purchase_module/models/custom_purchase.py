from odoo import _, fields, models


class CustomPurchase(models.Model):
    _name = "custom.purchase"
    _description = "Custom Purchase"

    name = fields.Char(string="Reference", required=True)
    date = fields.Date(string="Date", default=fields.Date.context_today)
    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("approved", "Approved"),
            ("done", "Done"),
        ],
        string="Status",
        default="draft",
        required=True,
    )
    line_ids = fields.One2many(
        comodel_name="custom.purchase.line",
        inverse_name="purchase_id",
        string="Purchase Lines",
    )
    brand_ids = fields.Many2many(
        comodel_name="custom.brand",
        relation="custom_purchase_brand_rel",
        column1="purchase_id",
        column2="brand_id",
        string="Brands",
    )

    # Action methods for form view buttons
    def action_approve(self):
        for record in self:
            record.status = "approved"

    def action_done(self):
        for record in self:
            record.status = "done"

    def action_draft(self):
        for record in self:
            record.status = "draft"