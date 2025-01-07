# -*- coding: utf-8 -*-

from odoo import models, fields, api

GRANT_STATE = [
    ("draft", "Draft"),
    ("approved", "Approved"),
]


class Grant(models.Model):
    _name = "grant.grant"
    _description = "Kuja Grants module"
    _inherit = "mail.thread"
    _rec_name = "title"

    title = fields.Char(string="Title", required=True)
    description = fields.Char(string="Description", required=True)
    state = fields.Selection(
        selection=GRANT_STATE,
        string="Status",
        readonly=True, copy=False, index=True,
        tracking=3,
        default="draft")
    donor_name = fields.Many2one("res.partner", string="Donor Name", required=True, domain="[('partner_type', '=', 'donor')]")
    deadline = fields.Datetime(string="Deadline", required=True)
    currency_id = fields.Many2one('res.currency', required=True)
    amount_from = fields.Float(string="Amount From", required=True)
    amount_to = fields.Float(string="Amount To", required=True)
    focus_area = fields.Many2many("grant.focus.area", string="Focus Area", required=True)
    geographic_area = fields.Many2many("grant.geographic.area", string="Geographic Area", required=True)
    eligibility = fields.Many2many("grant.eligibility", string="Eligibility", required=True)
    source_url = fields.Char(string="Source Url", required=True)
    user_likes = fields.Many2many("res.users", string="User Likes")
    user_likes_count = fields.Integer(compute="_compute_user_likes", string="Number of user likes")
    active = fields.Boolean(string="Active", default=True)

    @api.depends("user_likes_count")
    def _compute_user_likes(self):
        for record in self:
            record.user_likes_count = len(record.user_likes)

    def action_view_user_likes(self):
        action = self.env["ir.actions.act_window"]._for_xml_id("kuja_grant.act_grant_res_users")
        action["domain"] = [("id", "in", self.user_likes.ids)]
        return action

    def action_approve(self):
        for record in self:
            record.write({"state": "approved"})
