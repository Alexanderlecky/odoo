from odoo import http

class TShop(http.Controller):
    @http.route('/shop', auth='public', website=True)
    def shop_page(self, **kw):
        products = http.request.env['t_shop.product'].search([])
        return http.request.render('t_shop.shop_page', {'products': products})