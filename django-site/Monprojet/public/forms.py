# forms.py
from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'date', 'description']  # Assurez-vous que les champs correspondent au modèle
