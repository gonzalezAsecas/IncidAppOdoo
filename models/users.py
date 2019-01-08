# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api

class Users(models.Model):
    _inherit = 'res.users'
    project_chief_ids = fields.One2many('gastos.project', 'id_chief', string='Project chief')
    project_colab_ids = fields.Many2many('gastos.project', string='Partners')
    id_townhall = fields.Many2one('gastos.townhall', on_delete='set null', string='Town hall id')
