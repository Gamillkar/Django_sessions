from django import forms

class GameForm(forms.Form):

    example_number = forms.IntegerField(widget=forms.TextInput, label='Введите число')

