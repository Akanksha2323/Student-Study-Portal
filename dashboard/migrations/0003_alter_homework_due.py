# Generated by Django 3.2.4 on 2021-08-06 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20210806_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='due',
            field=models.DateTimeField(),
        ),
    ]
