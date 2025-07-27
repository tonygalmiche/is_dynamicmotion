# -*- coding: utf-8 -*-
import string
from odoo import models,fields,api  # type: ignore


class stock_move(models.Model):
    _inherit = "stock.move"

    is_sale_line_description = fields.Text(related="sale_line_id.name", string="Description commande")
    is_manquant              = fields.Float('Manquant', digits='Product Unit of Measure', default=0.0, compute="_compute_is_manquant", store=False)


    @api.depends("quantity_done","forecast_availability")
    def _compute_is_manquant(self):
        for obj in self:
            manquant =  obj.forecast_availability - obj.product_uom_qty     
            obj.is_manquant = manquant

            #product_uom_qty   
            # <field name="quantity_done" string="Consumed" decoration-success="not is_done and (quantity_done - should_consume_qty == 0)" decoration-warning="not is_done and (quantity_done - should_consume_qty &gt; 0.0001)" attrs="{'column_invisible': [('parent.state', '=', 'draft')], 'readonly': [('has_tracking', '!=','none')]}" force_save="1" widget="mrp_consumed"/>
