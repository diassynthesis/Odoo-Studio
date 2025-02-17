from odoo import models, fields

class StudioFieldGroup(models.Model):
    _name = 'studio.field_group'
    _description = 'Studio Field Groups'

    name = fields.Char(string="Group Name", required=True)
    model_id = fields.Many2one('studio.model', string="Related Model", required=True)
    field_ids = fields.Many2many('studio.field', string="Fields")
