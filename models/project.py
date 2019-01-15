# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api

class Project(models.Model):
    _name = 'gastos.project'
    name = fields.Char(string = "Name", required = True)
    investment_stimated = fields.Float(digits = (12,2), string = "Estimated investment")
    investment_final = fields.Float(digits = (12,2), string = "Final investment")
    description = fields.Text(string="Description")
    start_date = fields.Date(string="Start date")
    finish_date = fields.Date(string="Finish date")
    status = fields.Char(string="Status")
    id_chief = fields.Many2one('res.users', string = "Project chief", on_delete = 'set null', required = True)
    partner = fields.Many2many('res.users', string="Partner")
    costs = fields.One2many('gastos.cost', 'project_id', string="Cost")
    
    #onchange handler of the dates of the project and the costs
    @api.onchange('investment_stimated', 'investment_final')
    def _onchange_price(self):
        if self.investment_stimated | self.investment_final < 0.0:
            return{
                'warning':{
                    'title': "Incorrect investment value",
                    'message': "The investment may not be negative"
                },
            }