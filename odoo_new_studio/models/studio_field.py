from odoo import models, fields

class StudioField(models.Model):
    _name = 'studio.field'
    _description = 'Custom Studio Fields'

    name = fields.Char(string="Field Name", required=True)
    field_type = fields.Selection([
        ('char', 'Char'),
        ('integer', 'Integer'),
        ('float', 'Float'),
        ('boolean', 'Boolean'),
        ('datetime', 'Datetime'),
        ('text', 'Text'),
        ('selection', 'Selection'),
        ('many2one', 'Many2One'),
        ('one2many', 'One2Many'),
        ('many2many', 'Many2Many'),
    ], string="Type", required=True)
    model_id = fields.Many2one('studio.model', string="Model", required=True)
    required = fields.Boolean(string="Required")
