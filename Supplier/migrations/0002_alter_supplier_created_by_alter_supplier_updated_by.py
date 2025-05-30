# Generated by Django 5.0.6 on 2024-08-26 06:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='Created_By',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Supp_Created_By', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='Updated_By',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Supp_Updated_By', to=settings.AUTH_USER_MODEL),
        ),
    ]
