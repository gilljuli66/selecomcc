from odoo import models, fields, api
class Immat(models.Model):
    _name = 'immat.sites'

    centre = fields.Many2one(comodel_name='centre.sites',string='Centre')
    modele = fields.Many2one(comodel_name='vehicule.sites',string="Modele")
    name = fields.Char(string="Immatriculation")
    num_sup = fields.Char(string="N° Superviseur")
    code_radio = fields.Char(string="Code radio")
    
    