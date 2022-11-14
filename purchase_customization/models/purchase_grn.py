# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api


class purchaseCustomizationGRN(models.Model):
    _inherit = 'stock.picking'

    gate_check = fields.Boolean(default=False, copy=False, compute='GateCheckAvailable')
    gate_check_done = fields.Boolean(default=False, copy=False)

    vehicle_no = fields.Char(string='Vehicle No', copy=False)
    driver_name = fields.Char(string='Driver Name', copy=False)
    gate_pass_date = fields.Datetime(string='Gate Pass Date',
                                     default=datetime.now())

    inward_status = fields.Selection([
        ('pending', 'Pending'),
        ('done', 'Done')
    ], string='Delivery Status', compute='_get_delivery_status', store=True, readonly=True, default='pending',
        copy=False)

    def GateCheckAvailable(self):
        for rec in self:
            if rec.picking_type_id.code == 'incoming' or 'outgoing':
                self.gate_check = True
                # self.status_bar_view = True

    def _get_delivery_status(self):
        for rec in self:
            if rec.picking_type_id.code == 'incoming' or 'outgoing':
                self.gate_check = True
                # self.status_bar_view = True

    def InwardDoneButton(self):
        self.gate_check = True
        self.inward_status = 'done'


class purchaseGRNQTY(models.Model):
    _inherit = 'stock.move'
    gate_pass_qty = fields.Integer(string='Inward QTY', copy=False)
