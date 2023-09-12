from django import forms


class ChoiceForm(forms.ModelForm):
    selected = forms.ChoiceField(choices=[('完登', 'completed'), ('未完登', 'unfinished'), ('ゾーン', 'zone')])