from odoo import models, fields, api


class ProjectTask(models.Model):
    _name = 'human_resource.project.task'
    _description = 'Công việc trong dự án'

    task_id = fields.Char(string='Mã Công việc', required=True)
    name = fields.Char(string='Tên Công việc', required=True)
    description = fields.Text(string='Mô tả công việc')
    project_id = fields.Many2one('human_resource.project', string='Mã dự án', required=True,
                                  help="Chọn mã dự án cho task này")
    start_date = fields.Date(string='Ngày Bắt đầu')
    end_date = fields.Date(string='Ngày Kết thúc Dự kiến')
    status = fields.Selection([
        ('todo', 'Chưa thực hiện'),
        ('in_progress', 'Đang thực hiện'),
        ('done', 'Hoàn thành'),
    ], string='Trạng thái', default='todo')
