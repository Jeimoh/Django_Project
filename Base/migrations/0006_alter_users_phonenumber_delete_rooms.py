# Generated by Django 5.0.1 on 2024-01-30 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0005_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phoneNumber',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Rooms',
        ),
    ]
