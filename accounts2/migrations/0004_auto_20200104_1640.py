# Generated by Django 2.2.9 on 2020-01-04 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts2', '0003_auto_20200104_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='custom_user',
            name='is_staff',
        ),
    ]
