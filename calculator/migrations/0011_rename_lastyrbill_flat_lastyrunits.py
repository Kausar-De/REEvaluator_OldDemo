# Generated by Django 3.2.8 on 2022-04-01 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0010_alter_flat_lastyrbill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='lastyrbill',
            new_name='lastyrunits',
        ),
    ]
