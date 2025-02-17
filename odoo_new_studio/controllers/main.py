from odoo import http
from odoo.http import request

class OdooNewStudioController(http.Controller):

    @http.route('/odoo_new_studio', type='http', auth='user', website=True)
    def home(self, **kwargs):
        return "Welcome to Odoo New Studio!"

    @http.route('/odoo_new_studio/models', type='json', auth='user')
    def get_models(self):
        """Return a list of all models that can be customized in Studio"""
        models = request.env['ir.model'].search([])
        return [{'id': model.id, 'name': model.name, 'model': model.model} for model in models]

    @http.route('/odoo_new_studio/views', type='json', auth='user')
    def get_views(self, model_name):
        """Return views related to a specific model"""
        views = request.env['ir.ui.view'].search([('model', '=', model_name)])
        return [{'id': view.id, 'name': view.name, 'type': view.type} for view in views]

    @http.route('/odoo_new_studio/create_model', type='json', auth='user')
    def create_model(self, model_name, fields):
        """Dynamically create a new model"""
        model = request.env['ir.model'].sudo().create({'name': model_name, 'model': 'x_' + model_name.lower().replace(' ', '_')})
        for field in fields:
            request.env['ir.model.fields'].sudo().create({
                'model_id': model.id,
                'name': field['name'],
                'field_description': field['label'],
                'ttype': field['type'],
            })
        return {'status': 'success', 'message': 'Model created successfully'}
