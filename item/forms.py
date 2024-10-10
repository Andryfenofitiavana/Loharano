from django import forms
from .models import Entambarotra



STYLE = 'w-full py-4 px-6 rounded-xl border '
CSS = 'background-color: #121417;'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Entambarotra
        fields = ('sokajy', 'anarana', 'fanazavana', 'vidiny', 'sary')
        widgets = {
            'sokajy' : forms.Select(attrs={
                'class' : STYLE,
                'style' : CSS
            }),
            'anarana' : forms.TextInput(attrs={
                'class' : STYLE,
                'style':CSS
            }),
             'fanazavana' : forms.Textarea(attrs={
                'class' : STYLE,
                'style':CSS
                
            }),
             'vidiny' : forms.TextInput(attrs={
                'class' : STYLE,
                'style': CSS
            }),
              'sariny' : forms.FileInput(attrs={
                'class' : STYLE,
                'style': CSS
            }),
        }

class FormEdit(forms.ModelForm):
    class Meta:
        model = Entambarotra
        fields = ('sokajy', 'anarana', 'fanazavana', 'vidiny', 'sary', 'lafo_ve')
        widgets = {
            'sokajy' : forms.Select(attrs={
                'class' : STYLE,
                'style' : CSS
            }),
            'anarana' : forms.TextInput(attrs={
                'class' : STYLE,
                'style' : CSS
            }),
             'fanazavana' : forms.Textarea(attrs={
                'class' : STYLE,
                'style' : CSS
            }),
             'vidiny' : forms.TextInput(attrs={
                'class' : STYLE,
                'style' : CSS
            }),
              'sariny' : forms.FileInput(attrs={
                'class' : STYLE,
                'style' : CSS
            }),
        }
 