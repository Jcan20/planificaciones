# Generated by Django 5.1.6 on 2025-02-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planificacion', '0005_remove_actividad_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='vivienda',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
