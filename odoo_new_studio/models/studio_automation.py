from odoo import models, fields

class StudioAutomation(models.Model):
    _name = 'studio.automation'
    _description = 'Automations'

    name = fields.Char(string="Automation Name", required=True)
    model_id = fields.Many2one('studio.model', string="Target Model", required=True)
    trigger_type = fields.Selection([
        ('create', 'On Create'),
        ('write', 'On Write'),
        ('unlink', 'On Delete'),
        ('scheduled', 'Scheduled'),
    ], string="Trigger", required=True)
    action = fields.Text(string="Action Code")
    condition = fields.Text(string="Condition (Python Expression)")
    action_type = fields.Selection([
        ('update', 'Update Field'),
        ('email', 'Send Email'),
        ('webhook', 'Trigger Webhook')
    ], string="Action Type", required=True)
    action_data = fields.Text(string="Action Data (JSON)")
#   active = fields.Boolean(string="Active", default=True)
