# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api

class Cost(models.Model):
    _name = 'gastos.cost'
    date = fields.Datetime(string='Expenditure date')
    money = fields.Float(string='Spent money')
    description = fields.Text(string='Description of the spenditure')
    project_id = fields.Many2one('gastos.project', 
                            on_delete='cascade', string='The project')
