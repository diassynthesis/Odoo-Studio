from odoo import models, fields #good file

class StudioViewBuilder(models.Model):
    _name = 'studio.view.builder'
    _description = 'Studio View Builder'

    name = fields.Char(string="View Name", required=True)
    model_id = fields.Many2one('ir.model', string="Target Model", required=True)
    view_type = fields.Selection([
        ('form', 'Form'),
        ('tree', 'Tree'),
        ('kanban', 'Kanban'),
        ('graph', 'Graph'),
        ('calendar', 'Calendar'),
    ], string="View Type", required=True)
    arch_base = fields.Text(string="View Architecture")
