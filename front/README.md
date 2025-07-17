# React Frontend for Django Blog

A modern React app (Vite + React Bootstrap + Formik + Joi + React Router) for a blog platform with JWT authentication, article browsing, and commenting.

## Features
- Responsive UI with React Bootstrap
- JWT authentication (login/register)
- Article list with search and pagination
- View article details and comments
- Add, edit, and delete your own comments
- Admin/superuser can delete or edit any comment
- Only 3 latest articles shown by default, with "Show more" button

## Getting Started

### Prerequisites
- Node.js (v18+ recommended)
- Backend API running (see ../final/README.md)

### Setup

1. **Install dependencies**
   ```bash
   npm install
   ```

2. **Start the development server**
   ```bash
   npm run dev
   ```
   The app will be available at [http://localhost:5173](http://localhost:5173) by default.

3. **Configure API URL (if needed)**
   - By default, the frontend expects the backend at `http://localhost:8000/api`.
   - To change, edit `src/api.js`.

## Usage
- Register a new user or log in with an existing account.
- Browse articles, search by keyword, and click to view details.
- Add comments if logged in. Edit or delete your own comments.
- Admins/superusers can delete or edit any comment.
- Only 3 latest articles are shown by default; click "Show more" to see all.

## Project Structure
- `src/components/` — Reusable UI components (ArticleList, ArticleDetail, ArticleCard, Navbar, etc.)
- `src/components/pages/` — Page-level components (Login, Register)
- `src/context/` — Auth context provider
- `src/api.js` — API helpers (axios)

## Environment Variables
- No .env needed for frontend unless you want to customize the API URL.

## Linting
```bash
npm run lint
```

## Build for Production
```bash
npm run build
```

## Notes
- Make sure the backend is running and accessible at the configured API URL.
- JWT tokens are stored in localStorage and sent with every request.
- For admin features, log in as a user with `is_staff` or `is_superuser`.

---

For backend setup and API details, see `../final/README.md`.
