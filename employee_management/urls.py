from django.urls import path
from .views import *

urlpatterns = [
    path('employees/', employees_list, name='employees_list'), 
    path('add_employee/', add_employee, name='add_employee'),
     path('delete_employee/<int:employee_id>/', delete_employee, name='delete_employee'),
    path('department_hierarchy/', department_hierarchy, name='department_hierarchy'),
    path('departments/', departments_list, name='departments_list'),
    path('add_department/', add_department, name='add_department'),
    path('update_department/<int:department_id>/', update_department, name='update_department'),
    path('delete_department/<int:department_id>/', delete_department, name='delete_department'),
    path('update_employee/<int:employee_id>/', update_employee, name='update_employee'),
    path('department_salary_costs/', department_salary_costs, name='department_salary_costs'),
    path('add_salary/', add_salary, name='add_salary'),
    path('update_salary/<int:salary_id>/', update_salary, name='update_salary'),
    path('salaries/', salaries_list, name='salaries_list'),
]
