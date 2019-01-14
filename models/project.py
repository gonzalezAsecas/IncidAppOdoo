# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api

class Project(models.Model):
    _name = 'gastos.project'
    name = fields.Char(string = "Name", required = True)
    investment_estimated = fields.Float(digits = (12,2), 
                                    string = "Estimated investment")
    investment_final = fields.Float(digits = (12,2), 
                                    string = "Final investment")
    description = fields.Text(string="Description")
    start_date = fields.Date(string="Start date")
    finish_date = fields.Date(string="Finish date")
    status = fields.Char(string="Status")
    id_chief = fields.Many2one('res.users', 
                                string = "Project chief", on_delete='set null')
    partner = fields.Many2many('res.users', 
                                string="Partner")
    costs = fields.One2many('gastos.cost', 
                                'project_id',
                                string="Cost")
