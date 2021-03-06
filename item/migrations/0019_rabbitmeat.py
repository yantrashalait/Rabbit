# Generated by Django 2.2.5 on 2019-11-08 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0018_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='RabbitMeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, help_text='short description', null=True)),
                ('price', models.IntegerField(blank=True, help_text='Rs. per kg', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='meat/')),
            ],
        ),
    ]
