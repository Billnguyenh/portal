# Generated by Django 3.1.4 on 2021-01-09 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('win_parser', '0006_auto_20201230_2022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='windowsconfigmodel',
            old_name='txt',
            new_name='config_file',
        ),
    ]
