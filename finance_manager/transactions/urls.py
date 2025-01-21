# transactions/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/transactions', views.track_transactions, name='track_transactions'),  # Track transactions view (root of /transactions/)
    path('report/', views.generate_report, name='generate_report'),  # Generate report view
    path('budget/', views.manage_budget, name='manage_budget'),  # Manage budget view
]
