from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from customer.models import *

@login_required
def dashboard(request):
    newest_customers = Customer.objects.all()
    return render(request, 'dashboard/dashboard.html', {
        'customers': newest_customers
    })