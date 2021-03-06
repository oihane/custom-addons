# -*- coding: utf-8 -*-
# Copyright 2017 Oihane Crucelaegui - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import fields, models


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    safeguard_ip = fields.Boolean(string='IP Safeguard')
    safeguard_ik = fields.Boolean(string='IK Safeguard')
