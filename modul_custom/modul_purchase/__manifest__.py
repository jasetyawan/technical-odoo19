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
    'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/modul_purchase_view.xml',
        'views/modul_purchase_action.xml',
        'views/modul_purchase_menuitem.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'QEEL-1',
}