from odoo import models, fields

class StudioAccess(models.Model):
    _name = 'studio.access'
    _description = 'Access Control'

    name = fields.Char(string="Access Rule Name", required=True)
    model_id = fields.Many2one('studio.model', string="Model", required=True)
    group_id = fields.Many2one('res.groups', string="Group")
    permissions = fields.Selection([
        ('read', 'Read'),
        ('write', 'Write'),
        ('create', 'Create'),
        ('delete', 'Delete'),
    ], string="Permission", required=True)
