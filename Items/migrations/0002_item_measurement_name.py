# Generated by Django 5.0.6 on 2024-06-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='measurement_name',
            field=models.CharField(choices=[('Pcs', 'Pcs'), ('Box', 'Box')], default='Pcs', max_length=3),
        ),
    ]
