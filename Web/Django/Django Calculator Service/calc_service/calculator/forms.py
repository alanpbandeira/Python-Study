from django import forms
from .models import Operation


class CalcForm(forms.Form):
    OPERATION_CHOICES = (
        ('SUM', '+'),
        ('SUB', '-'),
        ('MUL', '*'),
        ('DIV', '/'),
        ('POW', '^')
    )

    x_value = forms.FloatField(label='x')
    y_value = forms.FloatField(label='y')
    op = forms.ChoiceField(label='Operation', choices=OPERATION_CHOICES)


class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = [
            'x_value',
            'y_value',
            'op'
        ]


