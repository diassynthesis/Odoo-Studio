from odoo import models, fields

class StudioView(models.Model):
    _name = 'studio.view'
    _description = 'Custom Views'

    name = fields.Char(string="View Name", required=True)
    model_id = fields.Many2one('studio.model', string="Target Model", required=True)
    view_type = fields.Selection([
        ('form', 'Form'),
        ('tree', 'List'),
        ('kanban', 'Kanban'),
        ('calendar', 'Calendar'),
        ('graph', 'Graph'),
        ('pivot', 'Pivot'),
    ], string="View Type", required=True)
    xml_definition = fields.Text(string="View XML")
