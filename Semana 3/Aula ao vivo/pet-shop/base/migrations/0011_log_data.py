# Generated by Django 4.2.3 on 2023-09-25 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_log_options_reserva_finalizado'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
    ]
