# Generated by Django 3.1.2 on 2020-11-17 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_gatepass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gatepass',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='gatepass',
            name='semester',
        ),
    ]