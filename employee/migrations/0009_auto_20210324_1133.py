# Generated by Django 3.1.4 on 2021-03-24 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_employee_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='leave',
            field=models.TextField(default=None),
        ),
    ]