# Generated by Django 4.1.5 on 2023-01-11 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0003_alter_pizzamodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzamodel',
            name='increments',
        ),
    ]
