# Generated by Django 3.0.4 on 2022-09-12 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0007_remove_empleado_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='categoria',
            new_name='nombre',
        ),
    ]