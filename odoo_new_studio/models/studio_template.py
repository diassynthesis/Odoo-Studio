from odoo import models, fields


class StudioTemplate(models.Model):
    _name = "studio.template"
    _description = "Studio Template"

    name = fields.Char(string="Template Name", required=True)

    template_type = fields.Selection(
        selection=[
            ('form', 'Form Template'),
            ('list', 'List Template'),
            ('kanban', 'Kanban Template'),
            ('email', 'Email Template'),
            ('report', 'Report Template'),
            ('other', 'Other'),
        ],
        string="Template Type",
        required=True,
        default="form"
    )

    description = fields.Text(string="Description")
    content = fields.Html(string="Content")
