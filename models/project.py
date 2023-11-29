from odoo import models, fields


class Project(models.Model):
    _name = 'human_resource.project'
    _description = 'Quản lý Dự án Nhân sự'

    project_id = fields.Char(string='Mã Dự án', required=True, help="Mã xác định duy nhất cho dự án.")
    lead_id = fields.Many2one('human_resource.employee', string='Quản lý Dự án', required=True, help="Nhân viên quản lý dự án.")
    name = fields.Char(string='Tên Dự án', required=True, help="Tên của dự án.")
    start_date = fields.Date(string='Ngày Bắt đầu', required=True, help="Ngày dự kiến bắt đầu dự án.")
    end_date = fields.Date(string='Ngày Kết thúc Dự kiến', required=True, help="Ngày dự kiến kết thúc dự án.")
    status = fields.Selection([
        ('on_going', 'Đang tiến hành'),
        ('completed', 'Hoàn thành'),
        ('delayed', 'Trễ hạn'),
        ('other', 'Khác'),
    ], string='Trạng thái Dự án', default='on_going', help="Trạng thái hiện tại của dự án.")
    description = fields.Text(string='Mô tả Dự án', help="Mô tả ngắn về dự án và mục tiêu của nó.")
    project_manager = fields.Many2one('human_resource.employee', string='Người Quản lý Dự án',
                                      help="Người chịu trách nhiệm quản lý và điều hành dự án.")
    executing_department = fields.Many2one('human_resource.department', string='Bộ phận Thực hiện',
                                           help="Bộ phận hoặc nhóm công việc thực hiện dự án.")
    progress = fields.Float(string='Tiến độ (%)', help="Phần trăm tiến độ hoàn thành của dự án.")
    created_date = fields.Datetime(string='Ngày Tạo', help="Ngày tạo bản ghi dự án.")
    modified_date = fields.Datetime(string='Ngày Sửa đổi', help="Ngày cập nhật thông tin dự án lần cuối.")
    priority = fields.Selection([
        ('high', 'Cao'),
        ('medium', 'Trung bình'),
        ('low', 'Thấp'),
    ], string='Ưu tiên', default='medium', help="Ưu tiên của dự án.")
    project_type = fields.Char(string='Loại Dự án', help="Phân loại dự án theo loại công việc hoặc mục tiêu của dự án.")
    budget = fields.Float(string='Ngân sách (VNĐ)', help="Ngân sách hoặc kinh phí dự kiến cho dự án.")
    tasks = fields.One2many('human_resource.project.task', 'project_id', string='Danh sách Nhiệm vụ', help="Danh sách nhiệm vụ hoặc công việc con của dự án.")
    # related_documents = fields.Many2many('ir.attachment', string='Tài liệu Liên quan',
    #                                      help="Các tài liệu, hợp đồng hoặc tài liệu khác liên quan đến dự án.")
    change_log = fields.Html(string='Nhật ký Thay đổi', help="Lịch sử các thay đổi và sự kiện quan trọng trong dự án.")
    creator = fields.Many2one('human_resource.employee', string='Người Tạo', help="Người tạo dự án.")
    customer_code = fields.Char(string='Mã Khách hàng', help="Mã của khách hàng hoặc đối tác liên quan đến dự án.")
    contract_type = fields.Char(string='Loại Hợp đồng',
                                help="Loại hợp đồng hoặc giao dịch liên quan đến dự án (nếu có).")
    project_category = fields.Char(string='Phân loại Dự án',
                                   help="Phân loại dự án theo danh mục hoặc ngành công nghiệp.")
    expected_completion_time = fields.Date(string='Thời gian Hoàn thành Dự kiến',
                                           help="Thời gian dự kiến hoàn thành dự án.")
    actual_completion_time = fields.Date(string='Thời gian Hoàn thành Thực tế',
                                         help="Thời gian thực tế mà dự án hoàn thành.")
