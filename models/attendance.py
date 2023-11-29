from odoo import models, fields, api
from odoo.exceptions import UserError

from odoo import models, fields, api

class Attendance(models.Model):
    _name = 'human_resource.attendance'
    _description = 'Bảng Chấm Công Nhân Viên'

    employee_id = fields.Many2one('human_resource.employee', string='Mã nhân Viên', required=True,
                                  help="Nhân viên liên quan đến bản ghi chấm công.")
    employee_name = fields.Char(string='Họ và tên', help="Nhập họ và tên", related='employee_id.full_name', store=True)

    checkin_time_morning = fields.Datetime(string='Thời Gian Check-In Buổi Sáng', required=True)
    checkout_time_morning = fields.Datetime(string='Thời Gian Check-out Buổi Trưa', required=True)
    checkin_time_afternoon = fields.Datetime(string='Thời Gian Check-In Buổi Chiều', required=True)
    checkout_time_afternoon = fields.Datetime(string='Thời Gian Check-Out Buổi Chiều', required=True)
    status = fields.Selection([
        ('present', 'Có Mặt'),
        ('absent', 'Vắng Mặt'),
        ('late', 'Đi Trễ'),
        ('early_checkout', 'Về Sớm'),
    ], string='Trạng Thái', help="Trạng thái chấm công.")
    date = fields.Date(string='Ngày', required=True, help="Ngày chấm công.")
    late_minutes_morning = fields.Float(string='Thời Gian Trễ Buổi Sáng (Phút)', compute='_compute_tre_sang', store=True, readonly=True)
    late_minutes_afternoon = fields.Float(string='Thời Gian Trễ Buổi Chiều (Phút)', readonly=True)
    early_checkout_minutes_lunch = fields.Float(string='Thời Gian Về Sớm Buổi Trưa (Phút)', readonly=True)
    early_checkout_minutes_afternoon = fields.Float(string='Thời Gian Về Sớm Buổi Chiều (Phút)', readonly=True)

    @api.depends('checkin_time_morning')
    def _compute_tre_sang(self):
        time_in = fields.Datetime.from_string("08:00:00")
        for record in self:
            # checkin_datetime = fields.Datetime.from_string(record.checkin_time_morning)
            # record.late_minutes_morning = (record.checkin_time_morning.hour - time_in.hour)*60 + (record.checkin_time_morning.minute - time_in.minute)
            record.late_minutes_morning = 30.0
