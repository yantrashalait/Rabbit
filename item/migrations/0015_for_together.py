# Generated by Django 2.2.5 on 2019-11-07 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0014_auto_20191107_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Together',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='together/')),
            ],
        ),
        migrations.CreateModel(
            name='For',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('together', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='together', to='item.Together')),
            ],
        ),
    ]
