from odoo import models, fields
class Support(models.Model):
    _name = 'support.sites'

    name = fields.Char(string="Nom support")
