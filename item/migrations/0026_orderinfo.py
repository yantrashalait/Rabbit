# Generated by Django 2.2.5 on 2019-11-11 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0025_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('note', models.TextField()),
            ],
        ),
    ]
