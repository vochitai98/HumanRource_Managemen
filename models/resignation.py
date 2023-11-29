from odoo import models, fields, api


class Resignation(models.Model):
    _name = 'human_resource.resignation'
    _description = 'Bảng nghỉ việc'

    employee_id = fields.Many2one('human_resource.employee', string='Nhân viên', required=True)
    resignation_date = fields.Date(string='Ngày nghỉ việc', required=True)
    reason = fields.Text(string='Lý do nghỉ việc')
    state = fields.Selection([
        ('draft', 'Chờ duyệt'),
        ('approved', 'Đã duyệt'),
        ('rejected', 'Từ chối'),
    ], default='draft', string='Trạng thái')
    approved_by = fields.Many2one('res.users', string='Duyệt bởi')
    rejection_reason = fields.Text(string='Lý do từ chối')
    attachment = fields.Binary(string='Tài liệu đính kèm')
    attachment_name = fields.Char(string='Tên tài liệu đính kèm')
