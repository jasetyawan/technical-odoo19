from odoo import fields, models


class CustomPurchase(models.Model):
    _name = "custom.purchase"
    _description = "Custom Purchase"

    # Header fields
    name = fields.Char(
        string="Reference",
        required=True,
        copy=False,
        default="New",
    )
    date = fields.Date(
        string="Date",
        default=fields.Date.context_today,
    )
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("approved", "Approved"),
            ("done", "Done"),
        ],
        string="Status",
        default="draft",
        required=True,
    )

    # Relational fields
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
            record.state = "approved"

    def action_done(self):
        for record in self:
            record.state = "done"

    def action_draft(self):
        for record in self:
            record.state = "draft"

    # Form navigation methods
    def action_save_and_close(self):
        """Save current record and return back to purchase list view."""
        return {
            "type": "ir.actions.act_window",
            "name": "Purchases",
            "res_model": "custom.purchase",
            "view_mode": "list,kanban,form",
            "target": "main",
        }

    def action_discard_record(self):
        """Discard/delete new draft record and return back to list view."""
        self.unlink()
        return {
            "type": "ir.actions.act_window",
            "name": "Purchases",
            "res_model": "custom.purchase",
            "view_mode": "list,kanban,form",
            "target": "main",
        }