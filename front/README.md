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
- Form validation with Formik and Joi
- Modern React 19 with Vite build system

## Technologies

- React 19.1.0
- Vite 7.0.4 (build tool)
- React Bootstrap 2.10.10 (UI components)
- React Router DOM 7.7.0 (routing)
- Formik 2.4.6 (form handling)
- Joi 17.13.3 (validation)
- Axios 1.10.0 (HTTP client)
- React Icons 5.5.0 (icons)

## Getting Started

### Prerequisites
- Node.js (v18+ recommended)
- Backend API running (see ../final/README.md)

### Quick Start

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
```
src/
├── components/          # Reusable UI components
│   ├── pages/          # Page-level components (Login, Register)
│   ├── ArticleList.jsx # Article listing component
│   ├── ArticleDetail.jsx # Article detail view
│   ├── ArticleCard.jsx # Individual article card
│   └── Navbar.jsx      # Navigation bar
├── context/            # React context providers
├── AuthContext.jsx     # Authentication context
├── api.js             # API helpers (axios configuration)
├── App.jsx            # Main application component
├── main.jsx           # Application entry point
└── App.css            # Global styles
```

## Environment Variables
- No .env needed for frontend unless you want to customize the API URL.
- API URL is configured in `src/api.js`

## Development

### Available Scripts
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run lint` - Run ESLint
- `npm run preview` - Preview production build

### Linting
```bash
npm run lint
```

### Build for Production
```bash
npm run build
```

## API Integration

The frontend communicates with the Django backend API:

- **Base URL**: `http://localhost:8000/api`
- **Authentication**: JWT tokens stored in localStorage
- **Endpoints**:
  - `/articles/` - Article listing and management
  - `/articles/{id}/` - Individual article details
  - `/articles/{id}/comments/` - Article comments
  - `/token/` - JWT authentication
  - `/register/` - User registration

## Notes
- Make sure the backend is running and accessible at the configured API URL.
- JWT tokens are stored in localStorage and sent with every request.
- For admin features, log in as a user with `is_staff` or `is_superuser`.
- The app is configured with CORS to work with the Django backend.
- Form validation is handled client-side with Formik and Joi.

---

For backend setup and API details, see `../final/README.md`.
