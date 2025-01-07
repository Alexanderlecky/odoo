from odoo import http
from odoo.http import request
import math

class WebsiteGrants(http.Controller):
    @http.route('/grants', type='http', auth='public', website=True)
    def list_grants(self, page=1, **kwargs):
        items_per_page = 3  # Number of grants per page
        page = int(page)
        offset = (page - 1) * items_per_page

        grants = request.env['grant.grant'].sudo().search([], offset=offset, limit=items_per_page)
        total_grants = request.env['grant.grant'].sudo().search_count([])
        total_pages = math.ceil(total_grants / items_per_page)

        return request.render('kuja_grant.website_grants', {
            'grants': grants,
            'current_page': page,
            'total_pages': total_pages,
            'items_per_page': items_per_page,
        })
