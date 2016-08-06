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

from openerp.addons.payment.models.payment_acquirer import ValidationError
from openerp.osv import osv
from openerp.tools.float_utils import float_compare
from openerp.tools.translate import _

import logging
import pprint

_logger = logging.getLogger(__name__)


class CheckPaymentAcquirer(osv.Model):
    _inherit = 'payment.acquirer'

    def _get_providers(self, cr, uid, context=None):
        providers = super(CheckPaymentAcquirer, self)._get_providers(cr, uid, context=context)
        providers.append(['check', _('Check')])
        return providers

    def transfer_get_form_action_url(self, cr, uid, id, context=None):
        return '/payment/check/feedback'

    def _format_transfer_data(self, cr, uid, context=None):
        # TODO: return address of company
        return ""

    def create(self, cr, uid, values, context=None):
        """ Hook in create to create a default post_msg. This is done in create
        to have access to the name and other creation values. If no post_msg
        or a void post_msg is given at creation, generate a default one. """
        if values.get('provider') == 'check' and not values.get('post_msg'):
            values['post_msg'] = self._format_transfer_data(cr, uid, context=context)
        return super(CheckPaymentAcquirer, self).create(cr, uid, values, context=context)


class CheckPaymentTransaction(osv.Model):
    _inherit = 'payment.transaction'

    def _cehck_form_get_tx_from_data(self, cr, uid, data, context=None):
        reference = data.get('reference')
        tx_ids = self.search(
            cr, uid, [
                ('reference', '=', reference),
            ], context=context)

        if not tx_ids or len(tx_ids) > 1:
            error_msg = _('received data for reference %s') % (pprint.pformat(reference))
            if not tx_ids:
                error_msg += _('; no order found')
            else:
                error_msg += _('; multiple order found')
            _logger.info(error_msg)
            raise ValidationError(error_msg)

        return self.browse(cr, uid, tx_ids[0], context=context)

    def _check_form_get_invalid_parameters(self, cr, uid, tx, data, context=None):
        invalid_parameters = []

        if float_compare(float(data.get('amount', '0.0')), tx.amount, 2) != 0:
            invalid_parameters.append(('amount', data.get('amount'), '%.2f' % tx.amount))
        if data.get('currency') != tx.currency_id.name:
            invalid_parameters.append(('currency', data.get('currency'), tx.currency_id.name))

        return invalid_parameters

    def _check_form_validate(self, cr, uid, tx, data, context=None):
        _logger.info('Validated check payment for tx %s: set as pending' % (tx.reference))
        return tx.write({'state': 'pending'})

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
