# Generated by Django 2.2.5 on 2019-11-06 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_auto_20191106_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='rabbitbreed',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='rabbit/'),
        ),
    ]
