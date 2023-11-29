from odoo import models, fields

class Applicant(models.Model):
    _name = 'human_resource.applicant'
    _description = 'Bảng ứng viên'

    name = fields.Char(string='Họ và tên', required=True)
    email = fields.Char(string='Email', required=True)
    phone_number = fields.Char(string='Số điện thoại')
    cover_letter = fields.Text(string='Thư xin việc')
    resume = fields.Binary(string='Hồ sơ')
    status = fields.Selection([
        ('new', 'Mới'),
        ('review', 'Đang xem xét'),
        ('interview', 'Phỏng vấn'),
        ('offer', 'Làm đề nghị'),
        ('hired', 'Đã tuyển'),
        ('rejected', 'Từ chối'),
    ], string='Trạng thái', default='new')

    recruitment_id = fields.Many2one('human_resource.recruitment', string='Tuyển dụng')