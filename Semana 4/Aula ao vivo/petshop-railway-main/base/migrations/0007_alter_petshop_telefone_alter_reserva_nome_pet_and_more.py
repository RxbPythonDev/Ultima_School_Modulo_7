# Generated by Django 4.2.3 on 2023-09-25 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_reserva_petshop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petshop',
            name='telefone',
            field=models.CharField(max_length=20, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='nome_pet',
            field=models.CharField(max_length=50, verbose_name='Nome do Pet'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='telefone',
            field=models.CharField(max_length=20, verbose_name='Telefone'),
        ),
    ]
