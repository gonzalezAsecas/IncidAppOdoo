# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api

class Cost(models.Model):
    _name = 'gastos.cost'
    date = fields.Datetime(string='Expenditure date', required = True)
    money = fields.Float(string='Spent money', required = True)
    description = fields.Text(string='Description of the spenditure', required = True)
    project_id = fields.Many2one('gastos.project', on_delete='cascade', string='The project', required = True)
    
    #onchange handler for see money positive always
    @api.onchange('money')
    def _onchange_price(self):
        if (self.money <= 0.0):
            return{
                'warning':{
                    'title': "Incorrect investment value",
                    'message': "The investment may not be negative"
                },
            }