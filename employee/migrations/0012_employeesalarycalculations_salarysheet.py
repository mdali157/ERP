# Generated by Django 3.1.4 on 2021-03-26 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_remove_employee_leave'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalarySheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.TextField(blank=True, default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSalaryCalculations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaves', models.TextField(blank=True, default=None, max_length=10)),
                ('addition', models.TextField(blank=True, default=None, max_length=10)),
                ('deducation', models.TextField(blank=True, default=None, max_length=10)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('salarysheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.salarysheet')),
            ],
        ),
    ]