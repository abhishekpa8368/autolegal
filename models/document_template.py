from odoo import models, fields

class DocumentTemplate(models.Model):
    _name = 'autolegal.template'
    _description = 'Legal Document Template'

    name = fields.Char(string='Template Name', required=True)
    content = fields.Text(string='Template Content', required=True)
    doc_type = fields.Selection([
        ('contract', 'Contract'),
        ('nda', 'NDA'),
        ('agreement', 'Agreement'),
    ], string='Document Type', required=True)
    active = fields.Boolean(default=True)
