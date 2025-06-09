from django.contrib import admin
from .models import Customer, Invoice, Reminder


@admin.action(description='Send reminder email')
def send_reminder_email_action(modeladmin, request, queryset):
    for reminder in queryset:
        reminder.send_reminder_email()

@admin.action(description='Mark selected invoices as PAID')
def mark_invoices_as_paid(modeladmin, request, queryset):
    queryset.update(is_paid=True)


admin.site.register(Customer)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'amount', 'due_date', 'is_paid')
    actions = [mark_invoices_as_paid]



@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'sent_at', 'message')
    actions = [send_reminder_email_action]