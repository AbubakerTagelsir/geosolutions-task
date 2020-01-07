from django import forms
from .models import History

class RequestForm(forms.ModelForm):
    # x = forms.FloatField()
    # y = forms.FloatField()
    # n = forms.IntegerField()
    # operation_type = forms.ChoiceField(choices=((1, "Nearest"), (2, "Furthest")))

    class Meta:
        model = History
        fields = "__all__"