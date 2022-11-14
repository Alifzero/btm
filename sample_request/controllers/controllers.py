# -*- coding: utf-8 -*-
# from odoo import http


# class SampleRequest(http.Controller):
#     @http.route('/sample_request/sample_request', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sample_request/sample_request/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sample_request.listing', {
#             'root': '/sample_request/sample_request',
#             'objects': http.request.env['sample_request.sample_request'].search([]),
#         })

#     @http.route('/sample_request/sample_request/objects/<model("sample_request.sample_request"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sample_request.object', {
#             'object': obj
#         })
