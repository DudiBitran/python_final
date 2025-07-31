# Django Blog API

A Django REST API for a blogging system with articles, comments, JWT authentication, and role-based permissions.

## Features

- Article management (CRUD for admins)
- Commenting system (for registered users)
- JWT-based authentication
- Browsable API interface
- Search/filter articles by title, content, tags, author
- User profiles and role-based permissions
- Tag system for articles
- Initial data: 7 users, multiple articles, and comments

## Technologies

- Django 5.2.3
- Django REST Framework 3.16.0
- djangorestframework-simplejwt 5.5.0
- django-filter 25.1
- django-cors-headers 4.7.0
- python-dotenv 1.1.1
- PostgreSQL (psycopg2-binary 2.9.10)

## Quick Start

If you want to get up and running quickly:

1. **Set up database and environment**
   ```bash
   # Create .env file with your PostgreSQL credentials
   echo "DB_NAME=blog
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432" > .env
   ```

2. **Install and setup**
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py create_full_sample_data
   python manage.py runserver
   ```

3. **Access the API**
   - API: http://localhost:8000/api/
   - Admin: http://localhost:8000/admin/ (adminuser/AdminPass123)

## Setup Instructions

### Prerequisites

- Python 3.8+ installed
- PostgreSQL installed and running
- Git installed

### Step-by-Step Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd python_final/final
   ```

2. **Create and activate virtual environment**

   ```bash
   # Create virtual environment
   python -m venv .venv

   # Activate virtual environment
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database**

   - Create a database named `blog` (or any name you prefer)
   - Create a user with access to the database
   - Note down the database name, username, and password

5. **Configure environment variables**

   - Create a `.env` file in the `final/` directory
   - Add your database configuration:

   ```
   DB_NAME=blog
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

6. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

## Initial Data Setup (Recommended)

To set up all sample users, profiles, articles, tags, and comments in one go, use the unified management command:

```bash
python manage.py create_full_sample_data
```

This will:

- Create all users (admin, regular users)
- Set their passwords
- Create user profiles
- Create tags, articles, and comments
- Ensure all relationships are correct

**Default users and passwords:**

- adminuser / AdminPass123
- admin / AdminPass123
- user1 / UserPass123
- user2 / UserPass123
- john_doe / UserPass123
- jane_smith / UserPass123
- mike_wilson / UserPass123

**Summary Table:**

| Step               | Command                                    |
| ------------------ | ------------------------------------------ |
| Apply migrations   | `python manage.py migrate`                 |
| Create sample data | `python manage.py create_full_sample_data` |
| Run server         | `python manage.py runserver`               |

---

## API Endpoints

### Authentication

- `POST /api/register/` — Register a new user
- `POST /api/token/` — Obtain JWT token
- `POST /api/token/refresh/` — Refresh JWT token

### Articles

- `GET /api/articles/` — List all articles
- `GET /api/articles/?search=<query>` — Search articles
- `GET /api/articles/<id>/` — Retrieve an article
- `POST /api/articles/` — Create article (admin only)
- `PUT /api/articles/<id>/` — Edit article (admin only)
- `DELETE /api/articles/<id>/` — Delete article (admin only)

### Comments

- `GET /api/articles/<id>/comments/` — List comments for an article
- `POST /api/articles/<id>/comments/` — Post a comment (authenticated users)
- `DELETE /api/comments/<id>/` — Delete a comment (admin only)

## Development

### Running Tests
```bash
python manage.py test
```

### Creating a Superuser
```bash
python manage.py createsuperuser
```

### Available Management Commands
- `python manage.py create_full_sample_data` - Create all sample data
- `python manage.py create_sample_data` - Create basic sample data
- `python manage.py setup_passwords` - Set passwords for existing users
- `python manage.py clean_orphaned_comments` - Clean up orphaned comments

## Notes

- **Superuser accounts:**
  - `adminuser` / `AdminPass123`
  - `admin` / `AdminPass123`
- **Regular user accounts:**
  - `user1` / `UserPass123`
  - `user2` / `UserPass123`
  - `john_doe` / `UserPass123`
  - `jane_smith` / `UserPass123`
  - `mike_wilson` / `UserPass123`
- **Database:** PostgreSQL (configured in `final/settings.py`)
- **API Testing:** Use the browsable API at `/api/` for easy testing
- **Admin Interface:** Access at `/admin/` with any superuser credentials
- **CORS:** Enabled for frontend integration (localhost:5173)

---

## **How to Use curl in Windows PowerShell**

You must write the entire `curl` command on one line, like this:

```powershell
curl -X POST "http://localhost:8000/api/comments/article/1/comments/" `
  -H "Authorization: Bearer <your_access_token>" `
  -H "Content-Type: application/json" `
  -d '{"text": "This is my comment!"}'
```

**Notes:**

- In PowerShell, use backticks (`) at the end of each line for line continuation, or just write the whole command on one line.
- Replace `<your_access_token>` with your actual JWT access token.

**Example (all on one line):**

```powershell
curl -X POST "http://localhost:8000/api/comments/article/1/comments/" -H "Authorization: Bearer <your_access_token>" -H "Content-Type: application/json" -d '{"text": "This is my comment!"}'
```

---

## **For GET requests (no token needed):**

```powershell
curl "http://localhost:8000/api/comments/article/1/comments/"
```

---

## **Summary**

- Always start with `curl ...` in PowerShell.
- Use double quotes for URLs and headers.
- Use backticks (`) for line continuation, or put the command on one line.

---

If you want to use a GUI, you can also use [Postman](https://www.postman.com/) for easier API testing!

Let me know if you need a ready-to-copy command for your specific token or want to see a Postman example!
