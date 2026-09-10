from odoo import fields, models


class CustomBrand(models.Model):
    _name = "custom.brand"
    _description = "Custom Brand"

    name = fields.Char(string="Brand Name", required=True)
    description = fields.Text(string="Description")