from django import forms
from sitetatto.models import Painter
from .models import Comment


class PaintersFilterForm(forms.Form):
    painter = forms.ChoiceField(choices = [(0, 'все')] + [(i.id, i.name) for i in Painter.objects.all()])

class CommentForm(forms.ModelForm):
    author_id = forms.CharField(widget=forms.HiddenInput())
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta:
        model = Comment
        fields = ('text', 'author_id')

