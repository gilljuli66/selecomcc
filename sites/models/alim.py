from odoo import models, fields
class Alim(models.Model):
    _name = 'alim.sites'

    name = fields.Char(string="Nom alim")