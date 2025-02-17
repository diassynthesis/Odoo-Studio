from odoo import models, fields, api

class StudioNewAppWizard(models.TransientModel):
    _name = 'studio.new.app.wizard'
    _description = 'New App Creation Wizard'

    name = fields.Char(string="App Name", required=True)
    technical_name = fields.Char(string="Technical Name", compute="_compute_technical_name", store=True)
    model_count = fields.Integer(string="Number of Models", default=1)
    
    @api.depends('name')
    def _compute_technical_name(self):
        for record in self:
            record.technical_name = record.name.lower().replace(" ", "_")

    def create_new_app(self):
        """Generate a new app with default structure"""
        new_app = self.env['studio.model'].create({
            'name': self.name,
            'model_name': f'x_{self.technical_name}',
        })
        return {
            'type': 'ir.actions.act_window',
            'name': 'New App',
            'res_model': 'studio.model',
            'res_id': new_app.id,
            'view_mode': 'form',
            'target': 'current',
        }
