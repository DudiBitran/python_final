# Django Blog API

A Django REST API for a blogging system with articles, comments, JWT authentication, and role-based permissions.

## Features
- Article management (CRUD for admins)
- Commenting system (for registered users)
- JWT-based authentication
- Browsable API interface
- Search/filter articles by title, content, tags, author
- Initial data: 2 users, 2 articles, 2 comments per article

## Technologies
- Django
- Django REST Framework
- djangorestframework-simplejwt
- django-filter
- django-cors-headers
- python-dotenv

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

7. **Load initial data**
   ```bash
   python manage.py loaddata api/fixtures/initial_data.json
   ```

8. **Set up user passwords**
   ```bash
   python manage.py setup_passwords
   ```

9. **Run the development server**
   ```bash
   python manage.py runserver
   ```

10. **Access the application**
    - Django Admin: http://127.0.0.1:8000/admin/
    - API Interface: http://127.0.0.1:8000/api/

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
<code_block_to_apply_changes_from>
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

---

The password for `newUser` (or any user you registered via the `/api/register/` endpoint) is the password you provided during registration.

For example, if you ran:
```bash
curl -X POST http://localhost:8000/api/register/ \
  -d '{"username": "newUser", "email": "newuser@example.com", "password": "Password123"}' \
  -H "Content-Type: application/json"
```
then the password for `newUser` is:
- **Username:** newUser
- **Password:** Password123

If you used a different password during registration, that is the password for `newUser`.

---

**If you forgot the password or want to reset it:**

1. Open the Django shell:
   ```bash
   python manage.py shell
   ```
2. Run:
   ```python
   from django.contrib.auth.models import User
   user = User.objects.get(username='newUser')
   user.set_password('NewPassword123')
   user.save()
   exit()
   ```
Now, the password for `newUser` will be `NewPassword123`.

Let me know if you need help resetting the password or if you want to check another user! 

---

Your initial data fixture is ready!  
You can now load it with:

```bash
python manage.py loaddata api/fixtures/initial_data.json
```

**What this fixture includes:**
- 3 groups: `admins`, `editors`, `users`
- 1 admin user (in `admins` group, is_staff, is_superuser)
- 2 regular users (in `users` group)
- 2 articles (by admin)
- 2 comments per article (by regular users)
- UserProfiles for all users

**Important:**  
Django fixtures cannot store raw passwords.  
**After loading the fixture, you must set the passwords manually.**  
Here’s how:

```python
# Run this in the Django shell:
python manage.py shell
```
Then:
```python
<code_block_to_apply_changes_from>
```
Now you can log in as:
- **adminuser / password123**
- **user1 / password123**
- **user2 / password123**

Let me know if you want to customize group assignments or permissions further! 

---

To load your initial data fixture into your Django project, follow these steps:

---

## **1. Make Sure Migrations Are Applied**

Before loading data, ensure your database and tables are ready:
```bash
python manage.py migrate
```

---

## **2. Load the Fixture**

Run:
```bash
python manage.py loaddata api/fixtures/initial_data.json
```
- This will create the groups, users, articles, comments, and user profiles as defined in the fixture.

---

## **3. Set User Passwords**

Django fixtures cannot store raw passwords, so you must set them manually after loading the data.

Run:
```bash
python manage.py shell
```
Then, in the shell:
```python
<code_block_to_apply_changes_from>
```

---

## **4. Done!**

You can now log in as:
- **adminuser / password123**
- **user1 / password123**
- **user2 / password123**

---

## **Summary Table**

| Step                | Command                                               |
|---------------------|------------------------------------------------------|
| Apply migrations    | `python manage.py migrate`                           |
| Load fixture        | `python manage.py loaddata api/fixtures/initial_data.json` |
| Set passwords       | Use Django shell as shown above                      |

---

Let me know if you run into any issues or need help with the process! 

---

Great choice! PostgreSQL is a robust, production-ready database for Django.

Here’s how to switch your Django project from SQLite to PostgreSQL:

---

## **1. Install PostgreSQL and psycopg2**

- Make sure PostgreSQL is installed on your system.
- Install the Python driver:
  ```bash
  pip install psycopg2-binary
  ```

---

## **2. Create a PostgreSQL Database and User**

- Open the PostgreSQL command line (psql) or use a GUI like pgAdmin.
- Run:
  ```sql
  CREATE DATABASE blogdb;
  CREATE USER bloguser WITH PASSWORD 'blogpassword';
  ALTER ROLE bloguser SET client_encoding TO 'utf8';
  ALTER ROLE bloguser SET default_transaction_isolation TO 'read committed';
  ALTER ROLE bloguser SET timezone TO 'UTC';
  GRANT ALL PRIVILEGES ON DATABASE blogdb TO bloguser;
  ```

---

## **3. Update `final/settings.py`**

Find the `DATABASES` section and change it to:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blogdb',
        'USER': 'bloguser',
        'PASSWORD': 'blogpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
- Adjust `NAME`, `USER`, and `PASSWORD` as needed.

---

## **4. Apply Migrations to PostgreSQL**

```bash
python manage.py migrate
```

---

## **5. Load Your Initial Data**

```bash
python manage.py loaddata api/fixtures/initial_data.json
```

---

## **6. Set User Passwords (as before)**

```bash
python manage.py shell
```
Then:
```python
from django.contrib.auth.models import User
User.objects.get(username='adminuser').set_password('password123'); User.objects.get(username='adminuser').save()
User.objects.get(username='user1').set_password('password123'); User.objects.get(username='user1').save()
User.objects.get(username='user2').set_password('password123'); User.objects.get(username='user2').save()
exit()
```

---

## **Summary Table**

| Step                | Command/Action                                      |
|---------------------|-----------------------------------------------------|
| Install driver      | `pip install psycopg2-binary`                       |
| Create DB & user    | Use psql or pgAdmin                                 |
| Update settings     | Edit `DATABASES` in `final/settings.py`             |
| Migrate             | `python manage.py migrate`                          |
| Load data           | `python manage.py loaddata ...`                     |
| Set passwords       | Use Django shell                                    |

---

Let me know if you need help with any step, or want the exact settings for your environment! 