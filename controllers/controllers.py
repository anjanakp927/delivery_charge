# -*- coding: utf-8 -*-
# from odoo import http


# class DeliveryCharges(http.Controller):
#     @http.route('/delivery_charges/delivery_charges/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delivery_charges/delivery_charges/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('delivery_charges.listing', {
#             'root': '/delivery_charges/delivery_charges',
#             'objects': http.request.env['delivery_charges.delivery_charges'].search([]),
#         })

#     @http.route('/delivery_charges/delivery_charges/objects/<model("delivery_charges.delivery_charges"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delivery_charges.object', {
#             'object': obj
#         })
