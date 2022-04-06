from odoo import models, fields
class Relais(models.Model):
    _name = 'relais.sites'

    name = fields.Char(string="Nom relais")
