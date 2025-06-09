from django.db import models
from django.core.mail import send_mail

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice #{self.id} for {self.customer.name}"

class Reminder(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f"Reminder for Invoice #{self.invoice.id} sent at {self.sent_at}"
    def send_reminder_email(self):
        subject = f"Reminder: Invoice #{self.invoice.id} is due"
        body = self.message
        recipient = self.invoice.customer.email

        send_mail(
            subject,
            body,
            'noreply@example.com',
            [recipient],
            fail_silently=False,
        )