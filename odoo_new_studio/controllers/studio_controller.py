from odoo import http
from odoo.http import request

class StudioController(http.Controller):
    @http.route('/studio/get_models', type='json', auth='user')
    def get_models(self):
        models = request.env['studio.model'].search([])
        return [{'id': m.id, 'name': m.name} for m in models]
