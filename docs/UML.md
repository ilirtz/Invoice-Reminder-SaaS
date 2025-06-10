## UML Class Diagram

```plantuml
@startuml

class User {
    +id : int
    +username : str
    +email : str
    +password : str
}

class Customer {
    +id : int
    +user_id : int (FK → User)
    +name : str
    +email : str
    +created_at : datetime
}

class Invoice {
    +id : int
    +user_id : int (FK → User)
    +customer_id : int (FK → Customer)
    +amount : decimal
    +due_date : date
    +is_paid : bool
    +created_at : datetime
}

class Reminder {
    +id : int
    +user_id : int (FK → User)
    +customer_id : int (FK → Customer)
    +invoice_id : int (FK → Invoice)
    +sent_at : datetime
}

' Relationships

User "1" -- "0..*" Customer : owns >
User "1" -- "0..*" Invoice : owns >
User "1" -- "0..*" Reminder : owns >

Customer "1" -- "0..*" Invoice : has >
Customer "1" -- "0..*" Reminder : has >

Invoice "1" -- "0..*" Reminder : related to >

@enduml
