from odoo import models, fields, api


class LeaveRequest(models.Model):
    _name = 'human_resource.leave_request'
    _description = 'Bảng Nghỉ Phép'

    employee_id = fields.Many2one('human_resource.employee', string='Nhân Viên', required=True)
    start_date = fields.Date(string='Ngày Bắt Đầu', required=True)
    end_date = fields.Date(string='Ngày Kết Thúc', required=True)
    leave_type = fields.Selection([
        ('annual_leave', 'Nghỉ phép hằng năm'),
        ('sick_leave', 'Nghỉ ốm'),
        ('unpaid_leave', 'Nghỉ không lương'),
        ('longterm_sick_leave', 'Nghỉ ốm dài ngày'),
        ('maternity_leave', 'Nghỉ thai sản'),
        ('other', 'Lý do khác'),
    ], string='Loại Nghỉ Phép', required=True)

    leave_reason = fields.Text(string='Lý do cụ thể', help="Nêu rõ lý do chi tiết của việc nghỉ phép.")
    attachment = fields.Binary(string='Tải lên bằng chứng',
                               help="Tải lên bằng chứng hoặc tài liệu liên quan đến nghỉ phép.")

    state = fields.Selection([
        ('draft', 'Nháp'),
        ('waiting', 'Đang Chờ Xử Lý'),
        ('approved', 'Đã Chấp Nhận'),
        ('rejected', 'Từ Chối'),
    ], string='Trạng Thái', default='draft', required=True)

