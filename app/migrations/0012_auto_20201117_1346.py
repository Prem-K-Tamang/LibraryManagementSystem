# Generated by Django 3.1.2 on 2020-11-17 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201117_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatepass',
            name='reason',
            field=models.CharField(max_length=1024),
        ),
        migrations.CreateModel(
            name='Issued',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('due_due', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]
