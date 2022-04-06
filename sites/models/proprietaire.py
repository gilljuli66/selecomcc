from odoo import models, fields
class Proprietaire(models.Model):
    _name = 'proprietaire.sites'

    name = fields.Char(string="Nom proprietaire")
