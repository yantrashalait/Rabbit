# Generated by Django 2.2.9 on 2020-01-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0064_auto_20200103_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='detail_image',
            field=models.ImageField(blank=True, null=True, upload_to='image/detail_img'),
        ),
    ]
