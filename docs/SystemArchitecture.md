## System Architecture Diagram

```plantuml
@startuml
!theme plain

actor Browser

package "Django Web App" {
    component "Views / Templates" as Views
    component "Business Logic" as Logic
    component "Models" as Models
}

database "Database\n(SQLite → PostgreSQL)" as DB

component "Email Service\n(SMTP → Gmail / SendGrid)" as Email

Browser --> Views : HTTP Requests
Views --> Browser : HTML Responses

Views --> Logic
Logic --> Models
Models --> DB : ORM (Django Models → DB)

Logic --> Email : Sends Reminder Emails

@enduml

