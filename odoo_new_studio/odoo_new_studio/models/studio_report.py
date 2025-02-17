from odoo import models, fields

class StudioReport(models.Model):
    _name = 'studio.report'
    _description = 'Studio Reports'

    name = fields.Char(string="Report Name", required=True)
    model_id = fields.Many2one('studio.model', string="Related Model", required=True)
    report_type = fields.Selection([
        ('pdf', 'PDF Report'),
        ('xls', 'Excel Report'),
        ('xlsx', 'Excel Report'),
        ('csv', 'CSV'),
    ], string="Report Type", required=True)
    template_id = fields.Many2one('studio.template', string="Report Template")
    active = fields.Boolean(string="Active", default=True)
