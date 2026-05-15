from odoo  import models
import io
import xlsxwriter
import base64


class One(models.Model):
    _inherit = 'sales.order'

    def action_export_order_xlsx(self):

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})

        worksheet = workbook.add_worksheet('Order')

        worksheet.merge_range(
            'A1:E1',
            'Sales Order report',
        )

        headers = [
            'customer_name',
            'date',
            'status',
            'total_amount',
        ]
        row = 2
        col = 0

        for hed in headers:
            worksheet.write(row,col,hed)
            col += 1
        row = 3

        for rec in self:

            worksheet.write(row,0, rec.customer_name)
            worksheet.write(row, 1, rec.date)
            worksheet.write(row, 2, rec.state)
            worksheet.write(row, 3, rec.total_amount)

            row += 1

        worksheet.set_column('A:E',20)

        workbook.close()

        output.seek(0)

        attachment = self.env['ir.attachment'].create({
            'name': 'order_report.xlsx',
            'type':'binary',
            'datas': base64.b64encode(output.getvalue()),
            'res_model': self._name,
            'res_id': self.id,
            # 'minetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true'
                   % attachment.id,
            'target': 'self',
        }


