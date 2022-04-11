from odoo import models, fields
class Centre(models.Model):
    _name = 'centre.sites'

    name = fields.Char(string="Nom du centre")