# Generated by Django 5.0.1 on 2024-01-21 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0002_alter_department_name_alter_employee_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeesalary',
            old_name='salary',
            new_name='salary_amount',
        ),
    ]
