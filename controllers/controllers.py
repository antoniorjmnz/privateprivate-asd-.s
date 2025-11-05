# from odoo import http


# class Upocubo(http.Controller):
#     @http.route('/upocubo/upocubo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upocubo/upocubo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('upocubo.listing', {
#             'root': '/upocubo/upocubo',
#             'objects': http.request.env['upocubo.upocubo'].search([]),
#         })

#     @http.route('/upocubo/upocubo/objects/<model("upocubo.upocubo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upocubo.object', {
#             'object': obj
#         })

