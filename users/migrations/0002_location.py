# Generated by Django 5.1.5 on 2025-02-01 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress1', models.CharField(blank=True, max_length=140)),
                ('adress2', models.CharField(blank=True, max_length=140)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('State', models.CharField(blank=True, max_length=50)),
                ('pincode', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
