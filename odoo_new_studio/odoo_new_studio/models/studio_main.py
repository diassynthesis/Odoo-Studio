from odoo import models, fields

class StudioMain(models.Model):
    _name = "studio.main"
    _description = "Studio Main"

    name = fields.Char(string="Name", required=True)
