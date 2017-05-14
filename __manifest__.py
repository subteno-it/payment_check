# -*- coding: utf-8 -*-
# Copyright 2016 Syleam
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Check Payment Acquirer',
    'category': 'Accounting',
    'summary': 'Payment Acquirer: Check Implementation',
    'author': 'SYLEAM',
    'website': 'http://www.syleam.fr/',
    'version': '1.0',
    'description': """Check Payment Acquirer""",
    'depends': [
        'payment',
    ],
    'data': [
        'views/payment_check.xml',
        'data/payment_check.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
}
