from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Flat, BuildingData, ApplianceData
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FlatForm(ModelForm):
    class Meta:
        model = Flat
        exclude = ['building']
        labels = {
            'name': _('Flat Name'),
            'area': _('Area (Sq. Ft.)'),
            'category': _('Category (BHK)'),
            'rooms': _('No. of Rooms'),
            'occupants': _('No. of Occupants'),
            'appliances': _('No. of Appliances'),
            'units': _('Units Consumed (Annual)'),
            'billamt': _('Energy Bill (Annual)'),
            'lastyr_units': _("Last Year's Units Monthwise (Comma Separated from JAN to DEC)"),
            'twoyrbfr_units': _("(OPTIONAL) Monthwise Units 2 Years Prior (Comma Separated from JAN to DEC)"),
            'threeyrbfr_units': _("(OPTIONAL) Monthwise Units 3 Years Prior (Comma Separated from JAN to DEC)"),
            'created_date': _('Submission Date'),
        }

class ApplianceForm(ModelForm):
    class Meta:
        model = ApplianceData
        exclude = ['flat']
        labels = {
            'appltype': _('Appliance Type'),
            'modelname': _('Model Name/No.'),
            'rating': _('Power Rating (Kilowatts)'),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password1', 'password2']
        labels = {
            'username': _('Account Username'),
            'email': _('Email Address'),
            'first_name': _('Building Name'),
        }

class BuildingForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email']
        labels = {
            'email': _('Email Address'),
            'first_name': _('Building Name'),
        }

class PictureForm(ModelForm):
    class Meta:
        model = BuildingData
        fields = '__all__'
        exclude = ['user']
        labels ={
            'profilepic': _('(Optional) Building Photo'),
        }