# Generated by Django 4.2.10 on 2024-04-23 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_report_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='title',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]