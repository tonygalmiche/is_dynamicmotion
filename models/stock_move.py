# -*- coding: utf-8 -*-
import string
from odoo import models,fields,api  # type: ignore


class stock_move(models.Model):
    _inherit = "stock.move"

    is_sale_line_description = fields.Text(related="sale_line_id.name", string="Description commande")

