# Generated by Django 5.0.6 on 2024-06-20 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer', '0008_alter_customer_created_by_alter_customer_updated_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tot_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.customer')),
            ],
        ),
    ]
