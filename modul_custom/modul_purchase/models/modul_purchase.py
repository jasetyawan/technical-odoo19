from odoo import models, fields, _


class ModulPurchase(models.Model):
    _name = "modul.purchase"
    _description = "Custom purchase module"

    name = fields.Char(string="Name", required=True)
    date = fields.Date(string="Date", default=fields.Date.context_today)
    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("approve", "Approve"),
            ("done", "Done"),
        ],
        string="Status",
        default="draft",
    )