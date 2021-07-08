from django import forms

from .models import Pictures, PictureUpgrade


class PictureForm(forms.ModelForm):
    name = forms.CharField(help_text='Название картинки',
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='',
                           )

    content = forms.ImageField(help_text='',
                               widget=forms.FileInput(attrs={'class': 'form-control'}),
                               label='',
                               )

    class Meta:
        model = Pictures
        fields = ('name', 'content')


class PictureFormUpgrade(forms.ModelForm):
    name = forms.CharField(help_text='Название',
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='',
                           )

    content = forms.ImageField(help_text='',
                               widget=forms.FileInput(attrs={'class': 'form-control'}),
                               label='',
                               )

    class Meta:
        model = PictureUpgrade
        fields = ('name', 'content', 'size_part', 'color_limit', 'width')

