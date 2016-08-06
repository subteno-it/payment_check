# -*- coding: utf-8 -*-
##############################################################################
#
#    payment_check module for OpenERP, Check Payment Acquirer
#    Copyright (C) 2016 SYLEAM Info Services (<http://www.syleam.fr>)
#              Sebastien LANGE <sebastien.lange@syleam.fr>
#
#    This file is a part of payment_check
#
#    payment_check is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    payment_check is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

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
