# Generated by Django 3.2.8 on 2022-01-01 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')], default='Choose BHK...', max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('area', models.IntegerField(default=0, null=True)),
                ('rooms', models.IntegerField(default=0, null=True)),
                ('occupants', models.IntegerField(default=0, null=True)),
                ('appliances', models.IntegerField(default=0, null=True)),
                ('appltypes', multiselectfield.db.fields.MultiSelectField(choices=[('Air Conditioner', 'Air Conditioner'), ('Computer', 'Computer'), ('LED', 'LED'), ('CFL', 'CFL'), ('Microwave', 'Microwave'), ('Washing Machine', 'Washing Machine'), ('Ceiling Fan', 'Ceiling Fan'), ('Refrigerator', 'Refrigerator'), ('Air Fryer', 'Air Fryer'), ('Chimney', 'Chimney'), ('Geyser', 'Geyser'), ('OTG', 'OTG'), ('Oven', 'Oven'), ('Electric Stove', 'Electric Stove'), ('BEV Charger', 'BEV Charger'), ('Television', 'Television'), ('Room Heater', 'Room Heater'), ('Electric Kettle', 'Electric Kettle')], max_length=183)),
                ('units', models.IntegerField(default=0, null=True)),
                ('billamt', models.IntegerField(default=0, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('append_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BuildingData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepic', models.ImageField(blank=True, default='ProfileDefault.jpg', null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
