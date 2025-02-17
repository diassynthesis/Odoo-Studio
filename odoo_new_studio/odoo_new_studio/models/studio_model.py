from odoo import models, fields

class StudioModel(models.Model):
    _name = 'studio.model'
    _description = 'Custom Models'

    name = fields.Char(string="Model Name", required=True)
    model_id = fields.Char(string="Technical Name", required=True)
    fields_ids = fields.One2many('studio.field', 'model_id', string="Fields")
    active = fields.Boolean(default=True)
