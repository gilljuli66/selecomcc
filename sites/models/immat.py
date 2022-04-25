from odoo import models, fields, api
class Immat(models.Model):
    _name = 'immat.sites'
    

    partner_name = fields.Many2one('res.partner',string="DIRNO CEI")
    
    #centre = fields.Many2one(comodel_name='centre.sites',string='Centre')
    #modele = fields.Many2one(comodel_name='vehicule.sites',string="Modele")
    name = fields.Char(string="Immatriculation")
    modelev = fields.Char(string="Modele")
    typev = fields.Char(string="Type")
    num_sup = fields.Char(string="N° Superviseur")
    code_radio = fields.Char(string="Code radio")
    
    