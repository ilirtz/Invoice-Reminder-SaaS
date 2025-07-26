from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Invoice, Customer

# Custom LoginView to redirect if already logged in
class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

# Rest of your views:
def home(request):
    return render(request, 'billing/home.html')

@login_required
def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'billing/invoice_list.html', {'invoices': invoices})

@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'billing/customer_list.html', {'customers': customers})

<<<<<<< HEAD
@login_required
def account_profile(request):
    return render(request, 'billing/account_profile.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'billing/register.html', {'form': form})

def pricing(request):
    return render(request, 'billing/pricing.html')
