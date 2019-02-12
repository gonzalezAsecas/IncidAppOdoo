# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api, exceptions

class Project(models.Model):
    _name = 'gastos.project'
    name = fields.Char(string = "Name", required = True)
    investment_stimated = fields.Float(digits = (12,2), string = "Estimated investment", required = True, default = 1.00)
    investment_final = fields.Float(digits = (12,2), string = "Final investment")
    description = fields.Text(string="Description")
    start_date = fields.Date(string="Start date", required = True)
    finish_date = fields.Date(string="Finish date")
    status = fields.Char(string="Status")
    id_chief = fields.Many2one('res.users', string = "Project chief", on_delete = 'set null', required = True)
    partner = fields.Many2many('res.users', string="Partner")
    costs = fields.One2many('gastos.cost', 'project_id', string="Cost")
    
    #onchange handler of the dates of the project and the costs
    @api.onchange('investment_stimated')
    def _onchange_price(self):
        for r in self:
            if r.investment_stimated <= 0.00:
                raise exceptions.ValidationError("The investment can't be zero or lower.")
    
    #oncreate start and finish date
    @api.constrains('start_date', 'finish_date')
    def _verify_dates(self):
        for r in self:
            if r.finish_date and r.finish_date < r.start_date:
                raise exceptions.ValidationError("The finish date can't be previous to start date.")
    
    #onchange start and finish date
    @api.onchange('start_date', 'finish_date')
    def _onchange_dates(self):
        for r in self:
            if r.finish_date and r.finish_date < r.start_date:


