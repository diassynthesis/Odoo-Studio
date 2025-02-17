from odoo import models, fields

class StudioMenu(models.Model):
    _name = "studio.menu"
    _description = "Odoo New Studio Menu"

    name = fields.Char(string="Menu Name", required=True)
    parent_id = fields.Many2one('odoo.new.studio.menu', string="Parent Menu")
    sequence = fields.Integer(string="Sequence", default=10)
