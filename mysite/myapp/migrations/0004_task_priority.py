# Generated by Django 4.2.6 on 2023-10-31 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_task_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('alta', 'Alta'), ('baja', 'Baja')], default='baja', max_length=4),
        ),
    ]
