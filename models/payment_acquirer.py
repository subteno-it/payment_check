# -*- coding: utf-8 -*-
# Copyright 2016 Syleam
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.payment.models.payment_acquirer import ValidationError
from odoo import api, fields, models, _
from odoo.tools.float_utils import float_compare

import logging
import pprint

_logger = logging.getLogger(__name__)


class CheckPaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('check', _('Check'))])

    def transfer_get_form_action_url(self):
        return '/payment/check/feedback'

    def _format_transfer_data(self):
        # TODO: return address of company
        return ""

    @api.model
    def create(self, values):
        """ Hook in create to create a default post_msg. This is done in create
        to have access to the name and other creation values. If no post_msg
        or a void post_msg is given at creation, generate a default one. """
        if values.get('provider') == 'check' and not values.get('post_msg'):
            values['post_msg'] = self._format_transfer_data()
        return super(CheckPaymentAcquirer, self).create(values)


class CheckPaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    @api.model
    def _check_form_get_tx_from_data(self, data):
        reference = data.get('reference')
        tx = self.search([('reference', '=', reference)])
        if not tx or len(tx) > 1:
            error_msg = _('received data for reference %s') % (pprint.pformat(reference))
            if not tx_ids:
                error_msg += _('; no order found')
            else:
                error_msg += _('; multiple order found')
            _logger.info(error_msg)
            raise ValidationError(error_msg)

        return tx

    def _check_form_get_invalid_parameters(self, data):
        invalid_parameters = []

        if float_compare(float(data.get('amount', '0.0')), self.amount, 2) != 0:
            invalid_parameters.append(('amount', data.get('amount'), '%.2f' % self.amount))
        if data.get('currency') != self.currency_id.name:
            invalid_parameters.append(('currency', data.get('currency'), self.currency_id.name))

        return invalid_parameters

    def _check_form_validate(self, data):
        _logger.info('Validated check payment for tx %s: set as pending' % (self.reference))
        return self.write({'state': 'pending'})
