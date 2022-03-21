# -*- coding: utf-8 -*-
# from odoo import http


# class Sitess(http.Controller):
#     @http.route('/sitess/sitess', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sitess/sitess/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sitess.listing', {
#             'root': '/sitess/sitess',
#             'objects': http.request.env['sitess.sitess'].search([]),
#         })

#     @http.route('/sitess/sitess/objects/<model("sitess.sitess"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sitess.object', {
#             'object': obj
#         })
