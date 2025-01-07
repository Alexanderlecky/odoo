# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GrantGeographicArea(models.Model):
    _name = 'grant.geographic.area'
    _description = 'Grant Geographic Area'

    name = fields.Char(string='Geographic Area', required=True)
    description = fields.Char(string='Description')
