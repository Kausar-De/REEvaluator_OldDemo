# Generated by Django 3.2.8 on 2022-03-28 05:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0007_flat_lastyrbill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='lastyrbill',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0, null=True), blank=True, null=True, size=12),
        ),
    ]
