# Generated by Django 4.2.4 on 2023-10-16 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='localidad',
            field=models.ForeignKey(blank=True, limit_choices_to={'localidad_nombre': models.CharField(blank=True, choices=[('0', 'Provincia de Buenos Aires'), ('1', 'Ciudad Autónoma de Buenos Aires')], max_length=2, verbose_name='Distrito')}, on_delete=django.db.models.deletion.CASCADE, to='location.location'),
        ),
    ]
