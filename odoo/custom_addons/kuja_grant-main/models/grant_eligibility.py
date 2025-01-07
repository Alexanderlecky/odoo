# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GrantEligibility(models.Model):
    _name = 'grant.eligibility'
    _description = 'Grant Eligibility'

    name = fields.Char(string='Eligibility', required=True)
    description = fields.Char(string='Description')
