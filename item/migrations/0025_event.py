# Generated by Django 2.2.5 on 2019-11-11 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0024_auto_20191111_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event/')),
                ('slogan', models.CharField(blank=True, max_length=300, null=True)),
                ('venue', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventserv', to='item.Service')),
            ],
        ),
    ]
