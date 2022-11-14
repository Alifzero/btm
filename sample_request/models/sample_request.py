# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api


class SampleRequest(models.Model):
    _name = 'sample.request'
    # _description = 'sample_request.sample_request'

    name = fields.Char(string='Req #', readonly=True)

    @api.model
    def create(self, vals):
        record = super(SampleRequest, self).create(vals)
        # seq_number = self.env['ir.sequence'].next_by_code('self.sample.request.seq') or ('New')
        record['name'] = self.env['ir.sequence'].next_by_code('sample_request_seq') or ('New')
        # code =  seq_number
        return record

    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('pre_costing', 'Pre Costing'),
        ('planing', 'Planing'),
        ('manufacturing', 'Manufacturing'),
        ('done', 'Done')],
        default='draft', required=True)
    requested_by = fields.Many2one('res.users', 'Current User', readonly=True, default=lambda self: self.env.user)
    f_req_date = fields.Date(string='1st Requested Date', default=datetime.today())
    s_req_date = fields.Date(string='2st Requested Date')
    samp_requ_date = fields.Date(string='Sample Required Date')

    greige = fields.One2many('greige.sample.request','greige_id')

    pile_count = fields.Many2one('pile.count')
    ground_count = fields.Many2one('ground.count')
    blend = fields.Many2one('blend.sample')
    loom_type = fields.Many2one('loom.type')
    yarn_type = fields.Many2one('yarn.type', string='Type Of Yarn in Pile')
    weft_count = fields.Many2one('weft.count')
    fancy_yarn = fields.Many2one('fancy.yarn')

    fancy_design = fields.Char(string='Fancy Design')
    fancy_size = fields.Char(string='Fancy Size')
    cam_size = fields.Char(string='CAM Size')
    reed = fields.Char(string='REED')
    fancy_design_size = fields.Char(sting='End Hem Fancy & Design')
    picks = fields.Char(string='Picks')
    pile_height = fields.Char(string='Pile Height')

    #### DYEING

    soft_flow_drier = fields.Selection([
        ('tick', '✓'),
        ('vat', 'N/A'),
        ('reactive', 'X')], )
    soft_flow_drier_text = fields.Text(string='Remarks')

    kier_soft_drier = fields.Selection([
        ('tick', '✓'),
        ('vat', 'N/A'),
        ('reactive', 'X')], )
    kier_soft_drier_text = fields.Text(string='Remarks')

    kier_winch_drier = fields.Selection([
        ('tick', '✓'),
        ('vat', 'N/A'),
        ('reactive', 'X')], string='Kier+Winch+Drier')
    kier_winch_drier_text = fields.Text(string='Remarks')

    kier_winch_hanger = fields.Selection([
        ('tick', '✓'),
        ('vat', 'N/A'),
        ('reactive', 'X')], string='Kier+Winch+Hanger')
    kier_winch_hanger_text = fields.Text(string='Remarks')

    stripe_wash = fields.Selection([
        ('tick', '✓'),
        ('vat', 'N/A'),
        ('reactive', 'X')])
    stripe_wash_text = fields.Text(string='Remarks')

    special_finishes_softness = fields.Selection([
        ('tick', '✓'),
        ('vat', 'N/A'),
        ('reactive', 'X')])
    special_finishes_softness_text = fields.Text(string='Remarks')

    bio_polish = fields.Selection([
        ('tick', '✓'),
        ('vat', 'N/A'),
        ('reactive', 'X')])
    bio_polish_text = fields.Text(string='Remarks')
    ekotex = fields.Selection([
        ('tick', '✓'),
        ('vat', 'N/A'),
        ('reactive', 'X')])
    ekotex_text = fields.Text(string='Remarks')
    others = fields.Selection([
        ('tick', '✓'),
        ('vat', 'N/A'),
        ('reactive', 'X')])
    others_text = fields.Text(string='Remarks')

    color_ref = fields.Many2many('dyeing.color')

    ### STITCHING

    label = fields.Char()
    packaging = fields.Char()
    total_required_pcs = fields.Integer()
    sample_purpose = fields.Char()
    special_inst = fields.Text()

    pre_costing = fields.One2many('yarn.pre.cost','pre_cost_id')
    pre_cost_rate = fields.One2many('pre.cost.rate','pre_cost_rate_id')


    pd_width = fields.Float(string='Width')
    pd_gsm = fields.Float(string='GSM')
    pd_length = fields.Float(string='Length')
    pd_weight = fields.Float(string='Weight/Pc in Gram')
    pd_lbs = fields.Float(string='LBS/Dozen')

    psc_packs = fields.Integer(string='Pcs/Packs')
    pk_carton = fields.Float(string='Pk/Carton')
    no_of_poly_bags = fields.Float(string='No Of Poly Bags')

    def DirectorApproval(self):
        self.state = 'approved'


class GreigeSampleRequest(models.Model):
    _name = 'greige.sample.request'

    name = fields.Many2one('product.template', string='Description')
    size = fields.Many2one('size.greige.sample.request', string='Size')
    weight = fields.Many2one('weight.greige.sample.request', string='Weight')
    greige_id = fields.Many2one('sample.request')

    gsm = fields.Integer(string='GSM')
    qty = fields.Integer(string='QTY')


class DescriptionGreigeSampleRequest(models.Model):
    _name = 'disc.greige.sample.request'

    name = fields.Char()


class SizeGreigeSampleRequest(models.Model):
    _name = 'size.greige.sample.request'

    name = fields.Char()


class WeightGreigeSampleRequest(models.Model):
    _name = 'weight.greige.sample.request'

    name = fields.Char()


class PileCountSampleRequest(models.Model):
    _name = 'pile.count'

    name = fields.Char()


class GroundCountSampleRequest(models.Model):
    _name = 'ground.count'

    name = fields.Char()


class DyingColorSampleRequest(models.Model):
    _name = 'dyeing.color'

    name = fields.Char()
    color = fields.Integer()


class WeftCountSampleRequest(models.Model):
    _name = 'weft.count'

    name = fields.Char()


class BlendSampleRequest(models.Model):
    _name = 'blend.sample'

    name = fields.Char()


class LoomTypeSampleRequest(models.Model):
    _name = 'loom.type'

    name = fields.Char()


class FancyYarnSampleRequest(models.Model):
    _name = 'fancy.yarn'

    name = fields.Char()


class YarnTypeSampleRequest(models.Model):
    _name = 'yarn.type'

    name = fields.Char()

