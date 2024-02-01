# Generated by Django 5.0.1 on 2024-01-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('lastSeen', models.DateTimeField(auto_now=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phoneNumber', models.IntegerField(max_length=14)),
            ],
        ),
    ]
