from odoo import models, fields
class Chargeur(models.Model):
    _name = 'chargeur.sites'

    name = fields.Char(string="Nom chargeur")
