from odoo import models, fields
class Base(models.Model):
    _name = 'base.sites'

    name = fields.Char(string="Nom base")