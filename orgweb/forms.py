from django.forms import ModelForm
from .models import OrgModel


class OrgForm(ModelForm):
    class Meta:
        model = OrgModel
        fields = ['title', 'description']
