from odoo import fields, models


class CustomBrand(models.Model):
    _name = "custom.brand"
    _description = "Custom Brand"

    # Brand fields
    name = fields.Char(string="Brand Name", required=True)
    description = fields.Text(string="Description")

    # SQL Constraints
    _sql_constraints = [
        ("name_uniq", "unique (name)", "The brand name must be unique!"),
    ]