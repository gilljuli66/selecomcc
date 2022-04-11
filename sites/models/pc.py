from odoo import models, fields
class Pc(models.Model):
    _name = 'pc.sites'

    name = fields.Char(string="Nom PC")