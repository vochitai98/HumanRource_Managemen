{
    'name': 'Human Resource Management',
    'version': '16.0.1.0.0',  # Phiên bản của module
    'summary': 'Odoo 16 Development',
    'description': """
        This module extends the HRM functionality in Odoo 16.
        It adds additional fields to the Employee model.
    """,
    'author': 'Odoo Mates',
    'website': 'www.odoomates.tech',
    'category': 'Human Resources',
    'depends': ['base', 'hr'],
    'data': [
        'views/menu.xml',
        'views/employee.xml',
        'views/employment_contract.xml',
        'views/project_view.xml',
        'views/task.xml',
        'views/department.xml',
        'views/attendance.xml',
        'views/leave_request.xml',
        'security/ir.model.access.csv',
        'views/salary.xml',
        'views/employee_performance.xml',
        'views/applicant.xml',
        'views/recruitment.xml',
        'views/resignation.xml',
    ],
    # 'installable': True,
    # 'application': False,
    # 'auto_install': True,
}
