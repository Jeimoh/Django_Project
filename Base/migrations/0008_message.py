# Generated by Django 5.0.1 on 2024-01-31 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0007_rooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=70)),
                ('dateModified', models.DateTimeField(auto_now=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Base.users')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.rooms')),
            ],
        ),
    ]
