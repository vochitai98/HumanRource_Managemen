from odoo import models, fields

class Employee(models.Model):
    _name = 'human_resource.employee'
    _description = 'Employee'

    employee_id = fields.Integer(string='Mã Nhân viên', help="Nhập mã nhân viên.", required=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('employee.sequence'))

    _sql_constraints = [
        ('employee_id_uniq', 'unique (employee_id)', 'Mã Nhân viên phải là duy nhất!'),
        ('contract_code_uniq', 'unique (contract_code)', 'Mã Hợp đồng phải là duy nhất!'),
    ]

    _order = 'employee_id'

    _rec_name = 'employee_id'

    # Các trường thông tin khác của nhân viên
    full_name = fields.Char(string='Họ và Tên', help="Nhập họ và tên đầy đủ của nhân viên.")
    date_of_birth = fields.Date(string='Ngày Sinh', required=True, help="Nhập ngày sinh của nhân viên.")
    citizen_id = fields.Char(string='Số CMND', required=True, help="Nhập số CMND của nhân viên.")
    job_position = fields.Char(string='Chức vụ', required=True, help="Nhập chức vụ của nhân viên.")
    address = fields.Text(string='Địa chỉ', required=True, help="Nhập địa chỉ thường trú của nhân viên.")
    email = fields.Char(string='Email', required=True, help="Nhập địa chỉ email của nhân viên.")
    mobile = fields.Char(string='Số Điện thoại di động', required=True, help="Nhập số điện thoại di động của nhân viên.")
    bank_account = fields.Char(string='Số Tài khoản ngân hàng', help="Nhập số tài khoản ngân hàng của nhân viên.")
    image = fields.Binary(string='Hình ảnh', help="Tải lên hình ảnh của nhân viên.")
    department_code = fields.Char(string='Mã Bộ phận', required=True, help="Nhập mã bộ phận của nhân viên.")
    contract_code = fields.Char(string='Mã Hợp đồng', required=True, help="Nhập mã hợp đồng của nhân viên.")
    project_code = fields.Char(string='Mã Dự án', help="Nhập mã dự án của nhân viên.")
    remaining_paid_leave = fields.Float(string='Ngày nghỉ phép có lương còn lại')
    remaining_unpaid_leave = fields.Float(string='Ngày nghỉ không lương còn lại')
