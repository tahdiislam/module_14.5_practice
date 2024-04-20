from django import forms

BIRTH_YEAR_CHOICE = ['1981', '1982', '1983']
class PracticeForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows': 3 }))
    agree = forms.BooleanField()
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICE))