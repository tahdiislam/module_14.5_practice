from django import forms
import datetime

BIRTH_YEAR_CHOICE = ["1981", "1982", "1983"]


class PracticeForm(forms.Form):
    name = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}), initial="Hello", disabled=True
    )
    agree = forms.BooleanField()
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICE))
    value = forms.DecimalField()
    email = forms.EmailField(required=False, label="Enter you email")
    message = forms.CharField(max_length=40, min_length=20)
    day = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLOR_CHOICE = [
        ("g", "green"),
        ("r", "red"),
        ("b", "blue"),
        ("y", "yellow"),
    ]
    favorite_color = forms.ChoiceField(
        choices=FAVORITE_COLOR_CHOICE, widget=forms.RadioSelect
    )
    SIZE_CHOICE = [("s", "short"), ("m", "medium"), ("l", "long")]
    size = forms.MultipleChoiceField(
        choices=SIZE_CHOICE, widget=forms.CheckboxSelectMultiple()
    )
