# -*- coding: utf-8 -*-
import string
from odoo import models,fields  # type: ignore


class stock_picking(models.Model):
    _inherit = "stock.picking"

    is_note_bl = fields.Text(string="Note BL")

