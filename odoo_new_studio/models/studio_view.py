from odoo import models, fields

class StudioView(models.Model):
    _name = 'studio.view'
#    _inherit = 'studio.view'
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
    xml_definition = fields.Text(string="View XML", help="Stores the generated XML")
    
    def open_view_builder(self):
        """Opens the View Builder interface"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'View Builder',
            'res_model': 'studio.view.builder',
            'view_mode': 'form',
            'target': 'new',
        }
        
 #   @api.model
    def create_view(self, model_id, view_type, xml_data):
        return self.create({
            'name': f'{view_type.capitalize()} View for {model_id}',
            'model_id': model_id,
            'view_type': view_type,
            'xml_definition': xml_data
        })
