# Generated by Django 5.0.1 on 2024-01-31 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0008_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.DeleteModel(
            name='Rooms',
        ),
    ]