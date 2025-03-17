# -*- coding: utf-8 -*-
{
    'name': 'Change internal reference for sku',
    'version': '18.0.1.0',
    'category': 'Sales',
    'summary': 'This module customizes Odoo product views to replace the Internal Reference field label with SKU',
    'description': """
    This module customizes Odoo's product views to replace the "Internal Reference" field label with "SKU"

    ===================================================
    Changes "Internal Reference" to "SKU" in the admin product form and product list views.
    Updates the product detail page on the website to display SKU above product attributes.
    Uses Odoo's inheritance system (XPath) for clean and efficient modifications.
    """,
    'author': 'Diego Naranjo',
    'category': 'Sales/Products',
    'depends': ['sale',
                'base',
                'product',
                'website_sale',
                'website',],
    'data': [
            'views/product_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
