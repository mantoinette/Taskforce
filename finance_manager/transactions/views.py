from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from .models import Account, Transaction, Budget, Category
from .forms import TransactionForm, BudgetForm, ReportForm



# View to track transactions
def track_transactions(request):
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    else:
        transactions = []  # Empty list for unauthenticated users

    return render(request, 'track.html', {
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
    # Handle both authenticated and unauthenticated users
    if request.user.is_authenticated:
        budgets = Budget.objects.filter(user=request.user)
    else:
        budgets = Budget.objects.none()  # No budgets for unauthenticated users

    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                form.instance.user = request.user
                form.save()
                messages.success(request, "Budget added successfully!")
            else:
                messages.error(request, "You need to be logged in to add a budget.")
            return redirect('manage_budget')
    else:
        form = BudgetForm()

    return render(request, 'manage_budget.html', {
        'form': form,
        'budgets': budgets,
    })

def home(request):
    return render(request, 'home.html')