# create empty file
# create memory file - output = io.BytesIO()
# create a workbook = xlsxwriter.Workbook(output) - take a entire exccel file
# create worksheet = workbook.add_worksheet('sales')
# write data take column , row number worksheet.write(0,0,'order_number')
# last use to download ir.actions.act_url


from odoo import models
import io
import xlsxwriter
import base64


class SalesQuotation(models.Model):
    _inherit = 'sales.quotation'

    def action_export_xlsx(self):

        output = io.BytesIO()

        workbook = xlsxwriter.Workbook(output, {
            'in_memory': True
        })

        worksheet = workbook.add_worksheet('Quotation')

        title = workbook.add_format({
            'bold': True,
            'font_size': 16,
            'align': 'center'
        })

        header = workbook.add_format({
            'bold': True,
            'border': 1,
            'align': 'center'
        })

        normal = workbook.add_format({
            'border': 1
        })

        worksheet.merge_range(
            'A1:E1',
            'Sales Quotation Report',
            title
        )

        headers = [
            'Quotation No',
            'Customer',
            'Date',
            'Status',
            'Total'
        ]

        row = 2
        col = 0

        for head in headers:
            worksheet.write(row, col, head, header)
            col += 1

        row = 3

        for rec in self:

            worksheet.write(row, 0, rec.quotation_number, normal)
            worksheet.write(row, 1, rec.customer_name, normal)
            worksheet.write(row, 2, str(rec.quotation_date), normal)
            worksheet.write(row, 3, rec.status, normal)
            worksheet.write(row, 4, rec.total_amount, normal)

            row += 1

        worksheet.set_column('A:E', 20)

        workbook.close()

        output.seek(0)

        attachment = self.env['ir.attachment'].create({
            'name': 'quotation_report.xlsx',
            'type': 'binary',
            'datas': base64.b64encode(output.read()),
            'res_model': self._name,
            'res_id': self.id,
            'mimetype':
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        })

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true'
                   % attachment.id,
            'target': 'self',
        }