from django import forms
from .models import Pictures


class PictureForm(forms.ModelForm):
    name = forms.CharField(help_text='Название картинки',
                           widget=forms.TextInput(attrs={'class': 'form-control'})
                           )

    class Meta:
        model = Pictures
        fields = ('name', 'content')