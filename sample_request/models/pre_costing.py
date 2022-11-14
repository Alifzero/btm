from odoo import models, fields, api


class YarnSampleCostPreCosting(models.Model):
    _name = 'yarn.pre.cost'

    yarn_name = fields.Many2one('product.template', string='Description')

    yarn_type_pre_cost = fields.Many2one('yarn.type')
    yarn_color = fields.Many2one('dyeing.color')
    yarn_percentage = fields.Float()
    yarn_wastage = fields.Float()
    yarn_rate = fields.Float()
    dyeing_rate = fields.Float()
    lbs_cost = fields.Float()
    pre_cost_id = fields.Many2one('sample.request')

class YarnSamplePreCostRate(models.Model):
    _name = 'pre.cost.rate'

    name = fields.Many2one('product.template', string='Item')
    rate_lbs = fields.Float(string='Rs/Lbs')
    rate_pc = fields.Float(string='Rs/Pc', compute='RatePerPiece')
    pre_cost_rate_id = fields.Many2one('sample.request')


    def RatePerPiece(self):
        self.rate_pc = self.rate_lbs / 10
