{
    'name': 'T-Shop',
    'description': 'Shop App for managing products and sales',
    'version': '1.0',
    'summary': 'Shop App for managing products and sales',
    'author': 'Alexander Karanja',
    'category': 'Sales',
    'depends': ['base', 'sale', 'website'],
    'data': [
        'views/menu.xml',
        'views/t_shop_views.xml',
        'views/templates.xml',
    ],
    'demo': ['data/demo_data.xml'],
    'installable': True,
    'application': True,
}
