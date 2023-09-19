from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from user.models import Profile

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import customer_technical_Details
from .models import Customer


from django import forms
from django.contrib.auth.models import User
from user.models import Profile
from django.db import models

from django import forms
from django.contrib.auth.models import User
from user.models import Profile
from django.db.models.fields.related import ManyToOneRel, ManyToManyRel



#
#
# class consumerGenerationForm(forms.Form):
#     # user_fields = forms.MultipleChoiceField(
#     #     choices=[
#     #         (field.name, field.verbose_name)
#     #         for field in User._meta.get_fields()
#     #         if field.name not in ['password', 'id', 'groups', 'user_permissions', 'profile']
#     #            and not isinstance(field, ManyToOneRel)
#     #     ],
#     #     widget=forms.CheckboxSelectMultiple
#     # )
#     #
#     # full_name = FullNameField()  # Add the custom full_name field
#
#     # Create the choices list without 'first_name' and 'last_name'
#     customer_choices = [
#         (field.name, field.verbose_name)
#         for field in Customer._meta.get_fields()
#         if field.name not in ['email']
#            and not isinstance(field, ManyToOneRel)
#     ]
#
#     # Add 'full_name' as a choice
#     #customer_choices.append(('username', 'Username'))
#     customer_choices.append(('full_name', 'Full Name'))
#     customer_choices.append(('email', 'Official Email'))
#
#     initial = ['first_name', 'username']
#
#     customer_fields = forms.MultipleChoiceField(
#         choices=customer_choices,
#         widget=forms.CheckboxSelectMultiple,
#         initial=initial  # Set 'Full Name' as initially selected
#     )
#
#
#     # user_fields = forms.MultipleChoiceField(
#     #     choices=user_choices,
#     #     widget=forms.CheckboxSelectMultiple
#     # )
#
#
#     # # profile_fields = forms.MultipleChoiceField(
#     # profile_choices = [
#     #     (field.name, field.verbose_name)
#     #     for field in Profile._meta.get_fields()
#     #     if field.name not in ['customer', 'pg', 'id', 'address', 'DOB', 'phone', 'department', 'designation', 'bg', 'city',
#     #                           'taluka', 'district', 'institution', 'yop', 'specili', 'last_updated_by', 'phone', 'emraddress', 'email',
#     #                           'image', 'workphone', 'name', 'phone']
#     # ]
#
#
#     def clean(self):
#         cleaned_data = super().clean()
#         customer_fields = cleaned_data.get('customer_fields', [])
#
#
#         first_name = cleaned_data.get('first_name')
#         last_name = cleaned_data.get('last_name')
#
#         if first_name and last_name:
#             cleaned_data['full_name'] = f"{first_name} {last_name}"
#
#         total_selected_fields = len(customer_fields)
#         if total_selected_fields > 6:
#             raise forms.ValidationError("You can select a maximum of 6 fields.")
#
#         if not customer_fields and not cleaned_data.get('full_name'):
#             raise forms.ValidationError("At least one field from each table or Full Name must be selected.")
#
#         return cleaned_data
#



# forms.py

from django import forms
from .models import Customer

class consumerGenerationForm(forms.Form):
    # Create the choices list without 'first_name' and 'last_name'
    customer_choices = [
        (field.name, field.verbose_name)
        for field in Customer._meta.get_fields()
        if field.name not in ['email']
           and not isinstance(field, ManyToOneRel)
    ]

    # Add 'full_name' as a choice
    customer_choices.append(('full_name', 'Full Name'))
    customer_choices.append(('email', 'Official Email'))

    initial = ['first_name', 'username']

    customer_fields = forms.MultipleChoiceField(
        choices=customer_choices,
        widget=forms.CheckboxSelectMultiple,
        initial=initial  # Set 'Full Name' as initially selected
    )

    userType = forms.ChoiceField(
        choices=(
            ('all', 'All Consumer Types'),
            ('Residential', 'Residential'),
            ('Commersial', 'Commercial'),
            ('Industrial', 'Industrial'),
            ('Goverment', 'Government'),
        ),
        required=False,  # Not required, as it's used for filtering
        widget=forms.RadioSelect,
        initial='all'  # Set the default option
    )

    def clean(self):
        cleaned_data = super().clean()
        customer_fields = cleaned_data.get('customer_fields', [])

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name and last_name:
            cleaned_data['full_name'] = f"{first_name} {last_name}"

        total_selected_fields = len(customer_fields)
        if total_selected_fields > 6:
            raise forms.ValidationError("You can select a maximum of 6 fields.")

        if not customer_fields and not cleaned_data.get('full_name'):
            raise forms.ValidationError("At least one field from the table or Full Name must be selected.")

        return cleaned_data
