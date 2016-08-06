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

import logging
import pprint
import werkzeug

from openerp import http, SUPERUSER_ID
from openerp.http import request

_logger = logging.getLogger(__name__)


class CheckController(http.Controller):
    _accept_url = '/payment/check/feedback'

    @http.route([
        '/payment/check/feedback',
    ], type='http', auth='none', csrf=False)
    def check_form_feedback(self, **post):
        cr, uid, context = request.cr, SUPERUSER_ID, request.context
        _logger.info('Beginning form_feedback with post data %s', pprint.pformat(post))
        request.registry['payment.transaction'].form_feedback(cr, uid, post, 'check', context)
        return werkzeug.utils.redirect(post.pop('return_url', '/'))


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
