from odoo import http
from odoo.http import request

class StudioController(http.Controller):

    @http.route('/studio/get_fields', type='json', auth='user')
    def get_fields(self, model_id):
        model = request.env['studio.model'].browse(model_id)
        if model.exists():
            fields = [{'name': f.name, 'type': f.field_type} for f in model.field_ids]
            return {'fields': fields}
        return {'status': 'error', 'message': 'Model not found'}
        
    @http.route('/studio/create_new_app', type='json', auth='user')
    def create_new_app(self, name):
        """Create a new app dynamically"""
        new_app = request.env['studio.model'].create({
            'name': name,
            'model_name': f'x_{name.lower().replace(" ", "_")}',
        })
        return {'status': 'success', 'app_id': new_app.id}
