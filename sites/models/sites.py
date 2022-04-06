from odoo import models, fields
class Sites(models.Model):
    _name = 'sites.sites'

    name = fields.Char(string="Nom du site")
    type = fields.Char(string="Type de site")
    adresse = fields.Char(string="Adresse")
    commune = fields.Char(string="commune")
    num_dept = fields.Integer("N° Département")
    code_postal = fields.Integer("Code Postal")
    long = fields.Float("Longitude",digits=(3,5))
    lat = fields.Float("Latitude",digits=(3,5))
    alt_ngf = fields.Float("Altitude NGF",digits=(4,3))
    type_relais = fields.Many2one(comodel_name='relais.sites',string='Relais')
    type_chargeur = fields.Many2one(comodel_name='chargeur.sites',string='Chargeur')
    type_batterie = fields.Many2one(comodel_name='batterie.sites',string='batterie')
    type_cable = fields.Many2one(comodel_name='cable.sites',string='Cable')
    multicoup = fields.Selection([('OUI','OUI'),('NON','NON'),],'Multicoupleur',default='NON')
    type_ant_40 = fields.Many2one(comodel_name='antenne.sites',string='Antenne')
    haut_ant_40 = fields.Float("Hauteur antenne 40MHz",digits=(4,3))
    type_ant_FH = fields.Many2one(comodel_name='antenne.sites',string='Antenne')
    haut_ant_FH = fields.Float("Hauteur antenne FH",digits=(4,3))
    type_support = fields.Many2one(comodel_name='support.sites',string='Support')
