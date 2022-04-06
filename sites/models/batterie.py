from odoo import models, fields
class Batterie(models.Model):
    _name = 'batterie.sites'

    name = fields.Char(string="Nom batterie")
