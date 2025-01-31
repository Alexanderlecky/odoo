from odoo import models, fields

class TShopCategory(models.Model):
    _name = 't_shop.category'
    _description = 'Product Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')


class TShop(models.Model):
    _name = 't_shop'
    _description = 'Shop'

    name = fields.Char(string='Product Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price', required=True)
    stock = fields.Integer(string='Stock', default=0)
    category_id = fields.Many2one('t_shop.category', string='Category')  # Make sure this is correct

