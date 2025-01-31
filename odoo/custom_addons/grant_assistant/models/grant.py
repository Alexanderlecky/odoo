from odoo import models, fields

class Grant(models.Model):
    _name = 'grant.grant'
    _description = 'Grant Information'

    name = fields.Char(string='Grant Name', required=True)
    description = fields.Text(string='Description')
    amount = fields.Float(string='Grant Amount')
    deadline = fields.Date(string='Application Deadline')
