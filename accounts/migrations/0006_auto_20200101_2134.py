# Generated by Django 2.2.6 on 2020-01-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_custom_user_logged_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
