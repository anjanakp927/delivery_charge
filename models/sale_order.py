from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_charge = fields.Monetary(string='Delivery Charge', compute='_compute_delivery_charge', store=True)

    @api.depends('amount_total')
    def _compute_delivery_charge(self):
        for order in self:
            order.delivery_charge = order.amount_total * 0.1
            # order.amount_total += order.delivery_charge

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['delivery_charge'] = self.delivery_charge
        return invoice_vals

    @api.depends('order_line.price_total', 'delivery_charge', 'currency_id', 'company_id', 'date_order',
                 'delivery_charge')
    def _amount_all(self):
        super(SaleOrder, self)._amount_all()
        for order in self:
            untaxed_amount = 0.0
            taxed_amount = 0.0
            for line in order.order_line:
                taxed_amount += line.price_total
                untaxed_amount += line.price_subtotal
            print(order.delivery_charge,"?????????????????????????????????????????")
            taxed_amount += order.delivery_charge
            print(taxed_amount,"AAAAAAAAAAAAAAAAAA")

            order.update({
                'amount_untaxed': untaxed_amount,
                'amount_tax': taxed_amount - untaxed_amount,
                'amount_total': taxed_amount,
            })
