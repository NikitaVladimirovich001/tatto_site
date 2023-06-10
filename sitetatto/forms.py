from django import forms
from sitetatto.models import Painter


class PaintersFilterForm(forms.Form):
    painter = forms.ChoiceField(choices= Painter.objects.all())