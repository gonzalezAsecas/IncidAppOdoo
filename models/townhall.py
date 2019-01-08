# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api

class TownHall(models.Model):
    _name = 'gastos.townhall'
    locality = fields.Char(string = "Locality")
    email = fields.Char(string = "Email")
    telephone = fields.Char(string = "Telephone")
    users_id = fields.One2many('res.users', 'id_townhall', string='Town hall users')
