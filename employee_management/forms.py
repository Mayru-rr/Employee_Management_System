

from django import forms
from .models import Department, Employee, EmployeeSalary

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'floor']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'address', 'designation', 'reporting_manager', 'department']


class EmployeeSalaryForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = ['employee', 'salary_amount', 'start_date', 'end_date']