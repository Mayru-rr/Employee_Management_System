from django.contrib import admin
from .models import Department, Employee, EmployeeSalary

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(EmployeeSalary)
