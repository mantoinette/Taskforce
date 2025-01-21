from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('transactions/', include('transactions.urls')),
    path('', include('transactions.urls')),  # Redirect root URL to 'transactions'
]
