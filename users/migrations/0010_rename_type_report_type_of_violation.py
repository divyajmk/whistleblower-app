# Generated by Django 4.2.11 on 2024-03-25 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_report_type_alter_report_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='type',
            new_name='type_of_violation',
        ),
    ]
