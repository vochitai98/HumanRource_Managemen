from odoo import models, fields, api


class Salary(models.Model):
    _name = 'human_resource.salary'
    _description = 'Bảng lương nhân viên'

    employee_id = fields.Many2one('human_resource.employment_contract', string='Mã nhân viên', required=True, help="Chọn mã nhân viên!")

    employee_name = fields.Char(string='Họ và tên', help="Nhập họ và tên", related='employee_id.employee_name', store=True)

    contract_code = fields.Char(string='Mã hợp đồng', help="Nhập mã hợp đồng hoặc tham chiếu.",
                                related='employee_id.contract_code', store=True)

    month = fields.Char(string='Tháng', required=True)
    basic_salary = fields.Float(string='Mức lương cơ bản', related='employee_id.basic_salary')
    responsibility_allowance = fields.Float(string='Phụ cấp trách nhiệm',
                                            related='employee_id.responsibility_allowance')
    performance_allowance = fields.Float(string='Phụ cấp hiệu suất', related='employee_id.performance_allowance')
    travel_allowance = fields.Float(string='Công tác phí', related='employee_id.travel_allowance')
    rewards = fields.Float(string='Khen thưởng', related='employee_id.rewards')
    social_insurance = fields.Float(string='Bảo hiểm xã hội', related='employee_id.social_insurance')
    other_benefits = fields.Float(string='Các chế độ được hưởng', related='employee_id.other_benefits')
    termination_agreement = fields.Float(string='Thỏa thuận khác', related='employee_id.termination_agreement')
    overtime_hours = fields.Float(string='Số giờ làm thêm', help='Số giờ làm thêm trong tháng.')
    overtime_rate = fields.Float(string='Mức lương làm thêm', help='Mức lương được trả cho giờ làm thêm (VNĐ/giờ).')
    overtime_income = fields.Float(string='Thu nhập từ làm thêm', compute='_compute_overtime_income', store=True)

    @api.depends('overtime_hours', 'overtime_rate')
    def _compute_overtime_income(self):
        for salary in self:
            salary.overtime_income = salary.overtime_hours * salary.overtime_rate

    total_income = fields.Float(string='Tổng thu nhập', compute='_compute_total_income', store=True)

    @api.depends('basic_salary', 'responsibility_allowance', 'performance_allowance', 'travel_allowance', 'rewards',
                 'social_insurance', 'other_benefits', 'termination_agreement', 'overtime_income')
    def _compute_total_income(self):
        for salary in self:
            salary.total_income = (
                        salary.basic_salary + salary.responsibility_allowance + salary.performance_allowance +
                        salary.travel_allowance + salary.rewards + salary.social_insurance +
                        salary.other_benefits + salary.termination_agreement + salary.overtime_income)

    deductions = fields.Float(string='Khấu trừ', help='Tổng số tiền được khấu trừ từ thu nhập.',
                              compute='_compute_deductions', store=True)
    net_income = fields.Float(string='Thu nhập ròng', compute='_compute_net_income', store=True)

    @api.depends('deductions', 'total_income')
    def _compute_net_income(self):
        for salary in self:
            salary.net_income = salary.total_income - salary.deductions
