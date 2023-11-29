from odoo import models, fields


class Recruitment(models.Model):
    _name = 'human_resource.recruitment'
    _description = 'Bảng tuyển dụng'

    job_title = fields.Char(string='Vị trí công việc', required=True)
    department = fields.Many2one('human_resource.department', string='Phòng ban')
    number_of_openings = fields.Integer(string='Số lượng cần tuyển', required=True)
    job_description = fields.Text(string='Mô tả công việc')
    application_deadline = fields.Date(string='Hạn nộp hồ sơ')

    contact_person = fields.Many2one('res.partner', string='Người liên hệ', required=True)
    address = fields.Text(string='Địa chỉ công ty')
    required_experience = fields.Integer(string='Kinh nghiệm yêu cầu (năm)')
    required_education = fields.Selection([
        ('high_school', 'Trung học'),
        ('bachelor', 'Cử nhân'),
        ('master', 'Thạc sĩ'),
        ('phd', 'Tiến sĩ'),
    ], string='Trình độ học vấn yêu cầu')

    application_ids = fields.One2many('human_resource.applicant', 'recruitment_id', string='Danh sách ứng viên')
