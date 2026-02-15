from django import forms
from .models import Lead
from django.contrib.auth import get_user_model
from .models import LeadSource

User = get_user_model()


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            "lat",
            "lng",
            "name",
            "phone",
            "email",
            "address",
            "city",
            "state",
            "property_type",
            "roof_type",
            "electricity_bill",
            "budget_estimate",
            "source",
            "campaign",
            "score",
            "status",
            "assigned_to",
        ]
        # include new pipeline/forecast fields
        fields += [
            "stage",
            "next_follow_up",
            "opportunity_value",
            "probability",
            "expected_close",
        ]
        widgets = {
            "address": forms.Textarea(attrs={"rows": 3}),
            "assigned_to": forms.Select(attrs={"class": "form-control"}),
            "property_type": forms.Select(choices=[('Residential','Residential'),('Commercial','Commercial'),('Industrial','Industrial'),('Land','Land')]),
            "roof_type": forms.Select(choices=[('Flat','Flat'),('Pitched','Pitched'),('Shed','Shed'),('Roof','Roof')]),
        }
        # widget overrides for new fields
        widgets.update({
            "next_follow_up": forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            "expected_close": forms.DateInput(attrs={'type': 'date'}),
            "probability": forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'max': 100}),
            "opportunity_value": forms.NumberInput(attrs={'step': '0.01'}),
        })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # keep assigned_to choices limited to active users
        self.fields["assigned_to"].queryset = User.objects.filter(is_active=True)
        # make source a model choice field if LeadSource model exists
        try:
            # evaluate source choices into a simple list to avoid keeping DB server-side cursors open
            choices = [('', '(Choose source)')] + list(LeadSource.objects.values_list('id', 'name'))
            self.fields['source'] = forms.ChoiceField(choices=choices, required=False)
        except Exception:
            # fallback to plain text field
            self.fields['source'] = forms.CharField(required=False)
        # ensure all visible fields render with a neutral inline style so they're not hidden by global CSS
        default_style = "background:#fff;color:#111;border:1px solid #ccc;padding:6px;width:100%;"
        for name, field in self.fields.items():
            # don't override if user explicitly set attributes
            existing = field.widget.attrs.get('style', '')
            if existing:
                field.widget.attrs['style'] = existing + ";" + default_style
            else:
                field.widget.attrs['style'] = default_style

        # remove customer_id from form (we set it in view if needed)
        if 'customer_id' in self.fields:
            self.fields.pop('customer_id')

