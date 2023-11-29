from odoo import models, fields, api


class EmployeePerformance(models.Model):
    _name = 'human_resource.employee_performance'
    _description = 'Đánh giá hiệu suất nhân viên'

    employee_id = fields.Many2one('human_resource.employee', string='Nhân viên', required=True)
    evaluation_date = fields.Date(string='Ngày đánh giá', required=True, default=fields.Date.today())
    evaluator_id = fields.Many2one('human_resource.employee', string='Người đánh giá', required=True)
    job_knowledge = fields.Float(string='Kiến thức công việc', digits=(6, 2),
                                 help='Điểm đánh giá kiến thức và kỹ năng liên quan đến công việc.')
    work_quality = fields.Float(string='Chất lượng công việc', digits=(6, 2),
                                help='Điểm đánh giá chất lượng công việc.')
    productivity = fields.Float(string='Năng suất làm việc', digits=(6, 2),
                               help='Điểm đánh giá năng suất làm việc.')
    communication_skills = fields.Float(string='Kỹ năng giao tiếp', digits=(6, 2),
                                       help='Điểm đánh giá kỹ năng giao tiếp và làm việc nhóm.')
    punctuality = fields.Float(string='Đúng giờ', digits=(6, 2),
                              help='Điểm đánh giá độ chính xác về thời gian.')
    adaptability = fields.Float(string='Khả năng thích nghi', digits=(6, 2),
                               help='Điểm đánh giá khả năng thích nghi với thay đổi.')
    leadership = fields.Float(string='Khả năng lãnh đạo', digits=(6, 2),
                             help='Điểm đánh giá khả năng lãnh đạo và quản lý.')
    overall_rating = fields.Float(string='Tổng điểm đánh giá', compute='_compute_overall_rating', store=True)
    comments = fields.Text(string='Nhận xét')

    @api.depends('job_knowledge', 'work_quality', 'productivity', 'communication_skills', 'punctuality',
                 'adaptability', 'leadership')
    def _compute_overall_rating(self):
        for performance in self:
            total_rating = (performance.job_knowledge + performance.work_quality + performance.productivity +
                            performance.communication_skills + performance.punctuality + performance.adaptability +
                            performance.leadership)
            performance.overall_rating = total_rating / 7.0
