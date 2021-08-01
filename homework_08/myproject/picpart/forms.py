from django import forms

from .models import Pictures, PictureUpgrade


class PictureForm(forms.ModelForm):
    name = forms.CharField(help_text='Название картинки',
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='',
                           initial="Моя картинка "
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
                           widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px'}),
                           label='',
                           initial="Новая обработка "
                           )

    size_part = forms.IntegerField(help_text='Размер ячейки (px)',
                                   widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
                                   label='',
                                   initial=12

                                   )
    color_limit = forms.IntegerField(help_text='Цветовой порог (0-255)',
                                     widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
                                     label='',
                                     initial=120
                                     )

    width = forms.IntegerField(help_text='Ширина изображения (px)',
                               widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
                               label='',
                               initial=800
                               )

    hard = forms.IntegerField(help_text='Сложность (0-100%)',
                              widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:200px'}),
                              label='',
                              initial=0
                              )

    favorite = forms.BooleanField(help_text='Избранное',
                                  widget=forms.CheckboxInput(attrs={'class': 'checkbox-inline'}),
                                  label='',
                                  initial=False,
                                  required=False
                                  )

    #
    # content = forms.ImageField(help_text='',
    #                            widget=forms.FileInput(attrs={'class': 'form-control'}),
    #                            label='',
    #                            )

    class Meta:
        model = PictureUpgrade
        fields = ('name', 'size_part', 'color_limit', 'width', 'hard', 'favorite')
