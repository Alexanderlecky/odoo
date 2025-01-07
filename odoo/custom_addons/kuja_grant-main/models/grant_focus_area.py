# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GrantFocusArea(models.Model):
    _name = 'grant.focus.area'
    _description = 'Grant Focus Area'

    name = fields.Char(string='Focus Area', required=True)
    description = fields.Char(string='Description')
