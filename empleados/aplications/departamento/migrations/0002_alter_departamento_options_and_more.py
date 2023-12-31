# Generated by Django 4.2.4 on 2023-09-16 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['nombre'], 'verbose_name': 'Sector', 'verbose_name_plural': 'Sectores'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('nombre', 'sigla')},
        ),
    ]
