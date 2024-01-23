from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.db import models
from .models import Department, Employee, EmployeeSalary
from .forms import *
from django.db.models import Sum
from django.utils.timezone import make_aware
from datetime import datetime




def index(request):
    return render(request, "index.html")


def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employees_list")
    else:
        form = EmployeeForm()

    managers = Employee.objects.filter(designation__in=["TL", "Manager"])

    return render(
        request,
        "add_employee.html",
        {"form": form, "departments": Department.objects.all(), "managers": managers},
    )


def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect("employees_list")


def department_hierarchy(request):
    departments = Department.objects.all()
    return render(request, "department_hierarchy.html", {"departments": departments})


def department_salary_costs(request):
    if request.method == "POST":
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        salary_costs = (
            EmployeeSalary.objects.filter(
                start_date__lte=end_date, end_date__gte=start_date
            )
            .values("employee__department__name")
            .annotate(total_salary=models.Sum("salary"))
        )
        return render(
            request, "department_salary_costs.html", {"salary_costs": salary_costs}
        )
    return render(request, "department_salary_costs.html")


def departments_list(request):
    departments = Department.objects.all()
    return render(request, "departments_list.html", {"departments": departments})


def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("departments_list")
    else:
        form = DepartmentForm()
    return render(request, "add_department.html", {"form": form})


def update_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect("departments_list")
    else:
        form = DepartmentForm(instance=department)
    return render(
        request, "update_department.html", {"form": form, "department": department}
    )


def delete_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    department.delete()
    return redirect("departments_list")


def employees_list(request):
    employees = Employee.objects.all()
    return render(request, "employees_list.html", {"employees": employees})


def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employees_list")
    else:
        form = EmployeeForm(instance=employee)
    return render(
        request,
        "update_employee.html",
        {"form": form, "employee": employee, "departments": Department.objects.all()},
    )


def add_salary(request):
    if request.method == "POST":
        form = EmployeeSalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("salaries_list")
    else:
        form = EmployeeSalaryForm()

    return render(
        request, "add_salary.html", {"form": form, "employees": Employee.objects.all()}
    )
    
def update_salary(request, salary_id):
    salary = EmployeeSalary.objects.get(id=salary_id)

    if request.method == 'POST':
        form = EmployeeSalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            return redirect('salaries_list')
    else:
        form = EmployeeSalaryForm(instance=salary)

    return render(request, 'update_salary.html', {'form': form, 'salary': salary})



def salaries_list(request):
    employee_salaries = EmployeeSalary.objects.all()
    employee_wise_salaries = {}
    for salary in employee_salaries:
        if salary.employee.name not in employee_wise_salaries:
            employee_wise_salaries[salary.employee.name] = []

        employee_wise_salaries[salary.employee.name].append(
            {
                "salary_amount": salary.salary_amount,
                "start_date": salary.start_date,
                "end_date": salary.end_date,
                "salary_id" : salary.id
            }
        )
    return render(
        request,
        "salaries_list.html",
        {"employee_wise_salaries": employee_wise_salaries},
    )

def department_salary_costs(request):
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if start_date and end_date:
            # Group by department and calculate total salary for each department
            queryset = EmployeeSalary.objects.filter(
                start_date__range=[start_date, end_date],
                end_date__range=[start_date, end_date]
            ).values('employee__department__name').annotate(total_salary=Sum('salary_amount'))

            context = {
                'queryset': queryset,
                'start_date': start_date,
                'end_date': end_date,
            }
            return render(request, 'department_salary_costs.html', context)

    return render(request, 'department_salary_costs.html')