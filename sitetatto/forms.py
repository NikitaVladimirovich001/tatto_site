from django import forms
from sitetatto.models import Painter
from .models import Comment


class PaintersFilterForm(forms.Form):
    painter = forms.ChoiceField(choices = ((i.id, i.name) for i in Painter.objects.all()))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)