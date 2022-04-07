from odoo import models, fields, api
class Vehicule(models.Model):
    _name = 'vehicule.sites'
    
    name = fields.Char("name")
    marque = fields.Char(string="Marque")
    modele = fields.Char(string="Modele")
    type = fields.Char(string="Type")
    
@api.depends('marque','modele')
def _compute_car(self):
    
    self.name = 'RENAULT CAR'
    return self.name
    