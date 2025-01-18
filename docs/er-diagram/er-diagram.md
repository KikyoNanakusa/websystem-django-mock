```mermaid
erDiagram
    Users {
        string UniqueID PK
        string name
        string email
        string password
        datetime created_at
        datetime updated_at
    }

    Categories {
        string UniqueID PK
        string name
        datetime created_at
        datetime updated_at
    }

    Products {
        string UniqueID PK
        string name
        string description
        string ISBN
        decimal price
        datetime created_at
        datetime updated_at
    }

    ProductCategories {
        string productId FK
        string categoryId FK
        datetime created_at
    }

    Review {
        string UniqueID PK
        string userId FK
        string productsId FK
        string title
        text content
        int evaluationPoint
        datetime created_at
        datetime updated_at
    }

    Users ||--o{ Review : "has"
    Products ||--o{ Review : "is reviewed by"
    Products ||--o{ ProductCategories : "belongs to"
    Categories ||--o{ ProductCategories : "includes"
```