# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GrantResPartner(models.Model):
    _inherit = 'res.partner'

    partner_type = fields.Selection([('donor', 'Donor')], string='Partner Type')
