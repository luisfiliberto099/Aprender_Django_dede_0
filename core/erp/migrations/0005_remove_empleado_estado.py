# Generated by Django 3.0.4 on 2022-09-12 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_auto_20220911_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='estado',
        ),
    ]
