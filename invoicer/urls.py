"""
URL configuration for invoicer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from billing import views as billing_views
from billing.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', billing_views.home, name='home'),
    path('invoices/', billing_views.invoice_list, name='invoice_list'),
    path('customers/', billing_views.customer_list, name='customer_list'),
    path('login/', CustomLoginView.as_view(template_name='billing/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', billing_views.register, name='register'),
    path('pricing/', billing_views.pricing, name='pricing'),  # if you added pricing page

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'), #password reset
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('account/', billing_views.account_profile, name='account_profile'), # my account menu
]    