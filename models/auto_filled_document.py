from odoo import models, fields, api

class AutoFilledDocument(models.Model):
    _name = 'autolegal.document'
    _description = 'Auto-Filled Legal Document'

    name = fields.Char(string='Document Name', required=True)
    template_id = fields.Many2one('autolegal.template', string='Template Used', required=True)
    filled_content = fields.Text(string='Filled Content', readonly=True)
    partner_id = fields.Many2one('res.partner', string='Client')
    validated = fields.Boolean(string='Legally Validated', default=False)

    @api.model
    def create(self, vals):
        # Example logic: auto-fill template placeholders with dummy data
        template = self.env['autolegal.template'].browse(vals['template_id'])
        content = template.content
        content = content.replace('{{client_name}}', self.env['res.partner'].browse(vals['partner_id']).name)
        vals['filled_content'] = content
        return super().create(vals)
