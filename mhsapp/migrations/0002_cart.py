# Generated by Django 5.0.10 on 2025-04-23 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mhsapp.customer')),
            ],
        ),
    ]
