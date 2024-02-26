from odoo import fields, models

class ApiProducts(models.Model):
    _name = 'api.products'
    _description = 'API Products'
    name = fields.Char(string='Product Name')
    cost = fields.Float(string='Product Price')