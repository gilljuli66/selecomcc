from odoo import models, fields
class Antenne(models.Model):
    _name = 'antenne.sites'

    name = fields.Char(string="Nom antenne")