# Generated by Django 4.2.10 on 2024-03-12 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_report_user_name_report_document_report_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='document',
        ),
        migrations.RemoveField(
            model_name='report',
            name='image',
        ),
        migrations.AddField(
            model_name='report',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='static'),
        ),
    ]
