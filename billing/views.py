from django.shortcuts import render, redirect
from .models import Invoice, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'billing/invoice_list.html', {'invoices': invoices})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'billing/customer_list.html', {'customers': customers})

def home(request):
    return render(request, 'billing/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after register
            return redirect('home')  # or 'invoice_list' if you prefer
    else:
        form = UserCreationForm()
    return render(request, 'billing/register.html', {'form': form})