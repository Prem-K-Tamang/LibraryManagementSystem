# Generated by Django 3.1.2 on 2020-11-17 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20201116_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='GatePass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('faculty', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.faculty')),
                ('semester', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.semester')),
                ('student', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]
