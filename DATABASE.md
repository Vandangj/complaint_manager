# Complaint Management System - Database Structure

## Database Overview

The Complaint Management System uses **SQLite** for local development and **MySQL** for production. The database contains **6 tables** that manage users, categories, complaints, comments, status history, and attachments.

---

## Database Schema

```mermaid
erDiagram
    users ||--o{ complaints : "creates"
    users ||--o{ complaints : "assigned_to"
    users ||--o{ complaint_comments : "writes"
    complaint_categories ||--o{ complaints : "categorizes"
    complaints ||--o{ complaint_comments : "has"
    complaints ||--o{ complaint_status_history : "tracks"
    complaints ||--o{ complaint_attachments : "contains"
    
    users {
        int id PK
        string full_name
        string email UK
        string role
        datetime created_at
    }
    
    complaint_categories {
        int id PK
        string name UK
        text description
    }
    
    complaints {
        int id PK
        int user_id FK
        int category_id FK
        string title
        text description
        string status
        int assigned_to FK
        datetime created_at
        datetime updated_at
    }
    
    complaint_comments {
        int id PK
        int complaint_id FK
        int user_id FK
        text comment
        datetime created_at
    }
    
    complaint_status_history {
        int id PK
        int complaint_id FK
        string old_status
        string new_status
        int changed_by FK
        text remark
        datetime created_at
    }
    
    complaint_attachments {
        int id PK
        int complaint_id FK
        string file_name
        string file_path
        string file_type
        int uploaded_by FK
        datetime created_at
    }
```

---

## Table Details

### 1. **users**
Stores user accounts with role-based access control.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Unique user identifier |
| `full_name` | VARCHAR(255) | NOT NULL | User's full name |
| `email` | VARCHAR(255) | UNIQUE, NOT NULL | User's email address |
| `role` | VARCHAR(50) | NOT NULL | User role: `admin` or `user` |
| `created_at` | DATETIME | DEFAULT NOW | Account creation timestamp |

**Roles:**
- `admin` - Can update complaint status, assign complaints, manage system
- `user` - Can create complaints, add comments, view own complaints

---

### 2. **complaint_categories**
Organizes complaints into categories for better management.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Unique category identifier |
| `name` | VARCHAR(100) | UNIQUE, NOT NULL | Category name |
| `description` | TEXT | NULL | Category description |

**Default Categories:**
- Technical - Technical issues and bugs
- Billing - Billing and payment related issues
- Service - Service quality and delivery issues
- General - General inquiries and feedback

---

### 3. **complaints**
Main table storing all complaint records.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Unique complaint identifier |
| `user_id` | INTEGER | FK → users.id, NOT NULL | User who created the complaint |
| `category_id` | INTEGER | FK → complaint_categories.id, NOT NULL | Complaint category |
| `title` | VARCHAR(255) | NOT NULL | Complaint title |
| `description` | TEXT | NULL | Detailed complaint description |
| `status` | VARCHAR(50) | DEFAULT 'open' | Current complaint status |
| `assigned_to` | INTEGER | FK → users.id, NULL | Admin user assigned to handle |
| `created_at` | DATETIME | DEFAULT NOW | Complaint creation timestamp |
| `updated_at` | DATETIME | DEFAULT NOW, AUTO UPDATE | Last update timestamp |

**Status Values:**
- `open` - Newly created complaint
- `in_progress` - Being worked on
- `resolved` - Solution provided
- `closed` - Completed and closed

---

### 4. **complaint_comments**
Stores comments and updates on complaints.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Unique comment identifier |
| `complaint_id` | INTEGER | FK → complaints.id, NOT NULL | Associated complaint |
| `user_id` | INTEGER | FK → users.id, NOT NULL | User who wrote the comment |
| `comment` | TEXT | NOT NULL | Comment text |
| `created_at` | DATETIME | DEFAULT NOW | Comment creation timestamp |

---

### 5. **complaint_status_history**
Tracks all status changes for audit trail.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Unique history record identifier |
| `complaint_id` | INTEGER | FK → complaints.id, NOT NULL | Associated complaint |
| `old_status` | VARCHAR(50) | NULL | Previous status |
| `new_status` | VARCHAR(50) | NOT NULL | New status |
| `changed_by` | INTEGER | FK → users.id, NOT NULL | User who changed the status |
| `remark` | TEXT | NULL | Optional remark about the change |
| `created_at` | DATETIME | DEFAULT NOW | Change timestamp |

---

### 6. **complaint_attachments**
Stores metadata for file attachments (files stored separately).

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Unique attachment identifier |
| `complaint_id` | INTEGER | FK → complaints.id, NOT NULL | Associated complaint |
| `file_name` | VARCHAR(255) | NOT NULL | Original file name |
| `file_path` | VARCHAR(500) | NOT NULL | Path to stored file |
| `file_type` | VARCHAR(100) | NULL | MIME type of the file |
| `uploaded_by` | INTEGER | FK → users.id, NOT NULL | User who uploaded the file |
| `created_at` | DATETIME | DEFAULT NOW | Upload timestamp |

---

## Relationships

### Foreign Key Constraints

1. **complaints.user_id** → users.id (CASCADE DELETE)
   - When a user is deleted, all their complaints are deleted

2. **complaints.category_id** → complaint_categories.id (CASCADE DELETE)
   - When a category is deleted, all complaints in that category are deleted

3. **complaints.assigned_to** → users.id (SET NULL)
   - When an admin is deleted, complaints are unassigned (not deleted)

4. **complaint_comments.complaint_id** → complaints.id (CASCADE DELETE)
   - When a complaint is deleted, all its comments are deleted

5. **complaint_comments.user_id** → users.id (CASCADE DELETE)
   - When a user is deleted, all their comments are deleted

6. **complaint_status_history.complaint_id** → complaints.id (CASCADE DELETE)
   - When a complaint is deleted, all its status history is deleted

7. **complaint_attachments.complaint_id** → complaints.id (CASCADE DELETE)
   - When a complaint is deleted, all its attachments are deleted

---

## Sample Data (Seeded on First Run)

### Users
| ID | Full Name | Email | Role |
|----|-----------|-------|------|
| 1 | Admin User | admin@example.com | admin |
| 2 | John Doe | john@example.com | user |
| 3 | Jane Smith | jane@example.com | user |
| 4 | Support Team | support@example.com | admin |

### Categories
| ID | Name | Description |
|----|------|-------------|
| 1 | Technical | Technical issues and bugs |
| 2 | Billing | Billing and payment related issues |
| 3 | Service | Service quality and delivery issues |
| 4 | General | General inquiries and feedback |

### Sample Complaints
| ID | User | Category | Title | Status |
|----|------|----------|-------|--------|
| 1 | John Doe | Technical | Website not loading | open |
| 2 | Jane Smith | Billing | Incorrect billing amount | open |

---

## Database Location

- **Development**: `complaint_manager/backend/db.sqlite3`
- **Production**: Configured via `DATABASE_URL` environment variable

---

## Accessing the Database

### Using SQLite CLI
```bash
cd complaint_manager/backend
sqlite3 db.sqlite3

# List all tables
.tables

# View table schema
.schema users

# Query data
SELECT * FROM users;
```

### Using Python Script
```bash
# View all database contents
python view_database.py
```

### Using the API
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

---

## Database Initialization

The database is automatically initialized when the backend starts for the first time:

1. **Tables Created**: All 6 tables are created via SQLAlchemy ORM
2. **Seed Data Inserted**: Default users, categories, and sample complaints
3. **Ready to Use**: Application is immediately usable

To manually reinitialize:
```bash
cd complaint_manager/backend
python -m app.main --init-db
```

---

## Database Management

### Backup
```bash
# SQLite backup
cp complaint_manager/backend/db.sqlite3 backup_$(date +%Y%m%d).sqlite3
```

### Reset Database
```bash
# Delete database file
rm complaint_manager/backend/db.sqlite3

# Restart backend to recreate
cd complaint_manager/backend
python -m uvicorn app.main:app
```

### Migration to MySQL
Update `.env` file:
```bash
DATABASE_URL=mysql+pymysql://username:password@hostname:3306/complaint_db
```

The application will automatically create tables in MySQL on first run.
