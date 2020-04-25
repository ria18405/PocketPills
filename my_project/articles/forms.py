from django import forms
class QueryForm(forms.Form):
    drug=forms.CharField(label='')

class QueryForm_2input(forms.Form):
    symptoms=forms.CharField()
    sickness=forms.CharField()

