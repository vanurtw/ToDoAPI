# Generated by Django 5.0.3 on 2024-03-13 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Выполнена'),
        ),
    ]
