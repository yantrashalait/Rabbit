# Generated by Django 2.2.9 on 2020-01-15 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0066_companyintroduction_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='place_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='stories',
            name='profession',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
