{
    'name': 'Custom Purchase Module',
    'version': '1.0',
    'category': 'Purchases',
    'summary': 'Customize purchase workflow for Odoo 19',
    'description': """
        Custom purchase module testing
    """,
    'website': '',
    'author': 'jasetyawan',
    'depends': ['base', 'purchase', 'product', 'uom'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_purchase_view.xml',
        'views/custom_purchase_action.xml',
        'views/custom_purchase_menuitem.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}