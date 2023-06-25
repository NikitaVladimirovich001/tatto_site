from django import forms
from sitetatto.models import Painter


class PaintersFilterForm(forms.Form):
    painter = forms.ChoiceField(choices = [(0, 'все')] + [(i.id, i.name) for i in Painter.objects.all()])


