# -*- coding: utf-8 -*-
import string
from odoo import models,fields  # type: ignore


class sale_order(models.Model):
    _inherit = "sale.order"

    is_description = fields.Char(string="Description")
    is_avancement  = fields.Integer(string="Avancement")

