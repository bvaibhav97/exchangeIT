# Generated by Django 2.2.9 on 2020-01-02 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_custom_user_timestamd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='timestamd',
            field=models.DateTimeField(),
        ),
    ]
