# -*- coding: utf-8 -*-
# Copyright 2016 Syleam
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import pprint
import werkzeug

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class CheckController(http.Controller):
    _accept_url = '/payment/check/feedback'

    @http.route([
        '/payment/check/feedback',
    ], type='http', auth='none', csrf=False)
    def check_form_feedback(self, **post):
        _logger.info('Beginning form_feedback with post data %s', pprint.pformat(post))  # debug
        request.env['payment.transaction'].sudo().form_feedback(post, 'check')
        return werkzeug.utils.redirect(post.pop('return_url', '/'))
