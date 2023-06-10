from django import forms
from django import forms as dj_forms

class ContactForm(forms.Form):
    name = dj_forms.CharField(
        min_length=20,
        widget = forms.TextInput(
       ##     attrs={'placeholder':'Ваше имя', 'style': 'border: 20px'}
        )
    )

    nomer = forms.IntegerField(min_value=11)

    email =forms.EmailField(
        widget=forms.EmailInput(
        ##    attrs={'placeholder': 'Ваш email'}
        )
    )

    date = forms.DateField(
        widget=forms.DateInput(
       ##     attrs={'placeholder': 'Дата'}
        )
    )

    time = forms.TimeField(
        widget=forms.TimeInput(
      ##      attrs={'placeholder': 'Время'}
        )
    )