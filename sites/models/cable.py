from odoo import models, fields
class Cable(models.Model):
    _name = 'cable.sites'

    name = fields.Char(string="Nom cable")
