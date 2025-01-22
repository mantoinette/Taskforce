from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from .models import Account, Transaction, Budget, Category
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm, BudgetForm, ReportForm



# View to track transactions
def track_transactions(request):
    return render(request, 'track.html', { 
    })

# View to generate a report
def generate_report(request):

    return render(request, 'generate_report.html') 
def manage_budget(request):

    return render(request, 'manage_budget.html', { 
    })

def home(request):
    return render(request, 'home.html')