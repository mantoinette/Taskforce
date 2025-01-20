from django import forms
from .models import Transaction, Budget

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'category', 'transaction_type', 'amount', 'description']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'amount']

class ReportForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
