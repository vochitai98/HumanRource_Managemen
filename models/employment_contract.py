from odoo import models, fields, api


class EmploymentContract(models.Model):
    _name = 'human_resource.employment_contract'
    _description = 'Quản lý Hợp đồng lao động'

    employee_id = fields.Many2one('human_resource.employee', string='Mã nhân viên', required=False,
                                  help="Chọn nhân viên cho hợp đồng này")

    employee_name = fields.Char(string='Họ và tên', help="Nhập họ và tên", related='employee_id.full_name', store=True)

    contract_code = fields.Char(string='Mã hợp đồng', help="Nhập mã hợp đồng hoặc tham chiếu.",
                                related='employee_id.contract_code', store=True)

    _sql_constraints = [
        ('employee_id_uniq', 'unique (employee_id)', 'Mã Nhân viên phải là duy nhất!'),
    ]

    _order = 'employee_id'

    _rec_name = 'employee_id'

    start_date = fields.Date(string='Ngày bắt đầu', help="Nhập ngày bắt đầu của hợp đồng.")
    end_date = fields.Date(string='Ngày kết thúc', help="Nhập ngày kết thúc của hợp đồng, nếu có.")
    job_position = fields.Char(string='Vị trí công việc', help="Nhập vị trí công việc cho nhân viên.", related='employee_id.job_position', store=True)
    department_code = fields.Char(string='Mã bộ phận', help="Nhập mã bộ phận, nếu có.", related='employee_id.department_code', store=True)
    termination_date = fields.Date(string='Ngày chấm dứt',
                                   help="Nhập ngày chấm dứt hợp đồng, nếu có.")
    termination_reason = fields.Text(string='Lý do chấm dứt',
                                     help="Nhập lý do chấm dứt hợp đồng, nếu có.")

    contract_type = fields.Selection([
        ('full_time', 'Toàn thời gian'),
        ('part_time', 'Bán thời gian'),
        ('fixed_term', 'Thời hạn cố định'),
        ('indefinite_term', 'Thời hạn không xác định')],
        string='Loại Hợp đồng lao động', help="Chọn loại hợp đồng lao động.")
    work_location = fields.Char(string='Địa điểm làm việc', help="Nhập địa điểm làm việc của nhân viên.")
    job_description = fields.Text(string='Nhiệm vụ công việc', help="Mô tả nhiệm vụ công việc của nhân viên.")

    morning_start_time = fields.Float(string='Giờ bắt đầu làm buổi sáng',
                                      help="Giờ bắt đầu làm việc vào buổi sáng (VD: 7.00).")
    lunch_break_time = fields.Float(string='Giờ nghỉ trưa', help="Giờ nghỉ trưa (VD: 11.30).")
    afternoon_start_time = fields.Float(string='Giờ bắt đầu làm buổi chiều',
                                        help="Giờ bắt đầu làm việc vào buổi chiều (VD: 13.30).")
    evening_end_time = fields.Float(string='Giờ tan làm buổi chiều',
                                    help="Giờ kết thúc làm việc vào buổi chiều (VD: 17.30).")

    # salary
    basic_salary = fields.Float(string='Mức lương chính', help='Nhập mức lương chính (VNĐ/tháng).')
    responsibility_allowance = fields.Float(string='Phụ cấp trách nhiệm', help='Nhập phụ cấp trách nhiệm (VNĐ/tháng).')
    performance_allowance = fields.Float(string='Phụ cấp hiệu suất công việc',
                                         help='Nhập thông tin phụ cấp hiệu suất công việc.')
    effective_salary = fields.Float(string='Lương hiệu quả',
                                    help='Nhập thông tin về lương hiệu quả theo quy định của phòng ban, công ty.')
    travel_allowance = fields.Float(string='Công tác phí',
                                    help='Nhập thông tin về công tác phí tùy từng vị trí, theo quy định của công ty.')
    payment_method = fields.Selection([
        ('bank_transfer', 'Chuyển khoản'),
        ('cash', 'Tiền mặt')],
        string='Hình thức trả lương', help='Chọn hình thức trả lương.')

    # Trường chế độ và quyền lợi
    rewards = fields.Float(string='Khen thưởng', help="Số tiền khen thưởng (VNĐ).")
    salary_increase_frequency = fields.Integer(string='Tần suất nâng lương', help="Số năm giữa các lần nâng lương.")
    salary_increase_amount = fields.Float(string='Số tiền nâng lương',
                                          help="Số tiền được nâng lương sau mỗi kỳ nâng lương (VNĐ).")
    weekly_leave = fields.Float(string='Nghỉ hàng tuần',
                                help="Số ngày nghỉ hàng tuần (ví dụ: 1.5 nghỉ chiều thứ 7 và cả ngày chủ nhật).")
    annual_leave = fields.Float(string='Nghỉ hàng năm',
                                help="Số ngày nghỉ phép hàng năm có lương (VD: 5 ngày phép/1 năm).")
    annual_unpaid_leave = fields.Float(string='Nghỉ hàng năm (Không Lương)',
                                       help="Số ngày nghỉ phép hàng năm không lương (VD: 12 ngày phép/1 năm).")
    public_holidays = fields.Float(string='Nghỉ ngày Lễ', help="Số ngày nghỉ các ngày Lễ pháp định.")
    social_insurance = fields.Float(string='Bảo hiểm xã hội', help="Số tiền bảo hiểm xã hội (VNĐ).")
    other_benefits = fields.Float(string='Các chế độ được hưởng',
                                  help="Số tiền hoặc các giá trị khác liên quan đến chế độ và quyền lợi.")
    termination_agreement = fields.Float(string='Thỏa thuận khác',
                                         help="Số tiền hoặc các giá trị khác liên quan đến thỏa thuận chấm dứt hợp đồng lao động.")
