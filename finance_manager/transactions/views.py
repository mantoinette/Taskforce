from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from .models import Account, Transaction, Budget, Category
from .forms import TransactionForm, BudgetForm, ReportForm

# View to track transactions
def track_transactions(request):
    accounts = Account.objects.filter(user=request.user)
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'track.html', {  # No 'transactions/' prefix here
        'accounts': accounts,
        'transactions': transactions,
    })

# View to generate a report
def generate_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            transactions = Transaction.objects.filter(
                user=request.user, date__range=[start_date, end_date]
            )
            return render(request, 'report.html', {  # No 'transactions/' prefix here
                'transactions': transactions,
            })
    else:
        form = ReportForm()
    return render(request, 'generate_report.html', {'form': form})  # Updated path

# View to manage the user's budget
def manage_budget(request):
    budgets = Budget.objects.filter(user=request.user)
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Budget added successfully!")
            return redirect('manage_budget')
    else:
        form = BudgetForm()
    return render(request, 'manage_budget.html', {  # Updated path
        'form': form,
        'budgets': budgets,
    })
