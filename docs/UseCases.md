# Use Case Descriptions — Invoice Reminder App

---

## UC1 — Register New User

**Actor:** Visitor  
**Preconditions:** Visitor is not logged in.  

**Basic Flow:**

1. Visitor navigates to `/register/`.
2. Visitor fills in registration form.
3. Visitor clicks "Register".
4. System creates new User.
5. System logs in User automatically.
6. System redirects User to Invoices page.

**Postconditions:**  
User is logged in and viewing Invoices.

---

## UC2 — Login

**Actor:** Registered User  
**Preconditions:** User exists, not logged in.  

**Basic Flow:**

1. User navigates to `/login/`.
2. User enters username/password.
3. User clicks "Login".
4. System authenticates User.
5. System redirects User to Invoices page.

**Postconditions:**  
User is logged in and can access protected views.

---

## UC3 — Logout

**Actor:** Logged-in User  
**Preconditions:** User is logged in.  

**Basic Flow:**

1. User clicks "Logout" link.
2. System logs out User.
3. System redirects to Home page.

**Postconditions:**  
User is logged out.

---

## UC4 — View Invoices

**Actor:** Logged-in User  
**Preconditions:** User is logged in.  

**Basic Flow:**

1. User navigates to `/invoices/`.
2. System displays list of Invoices for that User.

**Postconditions:**  
User views their own Invoices.

---

## UC5 — View Customers

**Actor:** Logged-in User  
**Preconditions:** User is logged in.  

**Basic Flow:**

1. User navigates to `/customers/`.
2. System displays list of Customers for that User.

**Postconditions:**  
User views their own Customers.

---

## UC6 — Send Reminder Email (Admin)

**Actor:** Admin User  
**Preconditions:** Admin is logged in.  

**Basic Flow:**

1. Admin navigates to Invoices in Admin panel.
2. Admin selects unpaid Invoices.
3. Admin chooses "Send Reminder Email" action.
4. System sends reminder emails to selected Customers.

**Postconditions:**  
Reminder emails are sent.

---

## UC7 — Mark Invoice as Paid (Admin)

**Actor:** Admin User  
**Preconditions:** Admin is logged in.  

**Basic Flow:**

1. Admin navigates to Invoices in Admin panel.
2. Admin selects Invoice(s).
3. Admin chooses "Mark as Paid" action.
4. System updates Invoice status to "Paid".

**Postconditions:**  
Invoice status is updated.

---
