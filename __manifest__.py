{
    'name': 'Supplier Volume Discounts',
    'version': '17.0.1.0.0',
    'category': 'Purchase',
    'summary': 'Manage volume discounts from suppliers in purchase orders',
    'description': """
        This module extends the purchase management functionality to handle volume discounts from suppliers.
        
        Features:
        - Add volume discount percentage and minimum purchase amount fields to suppliers
        - Display supplier discount information in purchase order headers
        - Show product categories in purchase order lines
        - Automatically apply volume discounts when subtotal exceeds minimum amount
        - Validate that all products have a main supplier before confirming orders
        - Enhanced purchase order reports showing discount savings
    """,
    'author': 'Lucas Maidana',
    'depends': ['base', 'purchase', 'product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}