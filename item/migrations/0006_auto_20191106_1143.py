# Generated by Django 2.2.5 on 2019-11-06 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20191105_1229'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='BlogCategory',
        ),
    ]
