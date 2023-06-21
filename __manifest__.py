# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo 16 pour Dynamic Motion',
    'version'  : '0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',
    'description': """
InfoSaône - Module Odoo 16 pour Dynamic Motion
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        "stock",
    ],
    'data' : [
        "report/report_deliveryslip.xml",
        "report/report_etiquette_colis.xml",
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
    'license': 'LGPL-3',
}

