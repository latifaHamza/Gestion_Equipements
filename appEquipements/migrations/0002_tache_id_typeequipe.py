# Generated by Django 4.1.6 on 2023-06-28 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEquipements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tache',
            name='id_TypeEquipe',
            field=models.IntegerField(null=True),
        ),
    ]