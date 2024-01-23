from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    designation = models.CharField(max_length=20, choices=[('Associate', 'Associate'), ('TL', 'TL'), ('Manager', 'Manager')])
    reporting_manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class EmployeeSalary(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    salary_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
