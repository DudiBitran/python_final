import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

// Set up axios default instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Set default Authorization header if token exists
const token = localStorage.getItem('token');
if (token) {
  api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

// Add token to requests if available (keep this for dynamic updates)
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Helper to update axios default header after login/logout
export function setAuthToken(token) {
  if (token) {
    api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  } else {
    delete api.defaults.headers.common['Authorization'];
  }
}

// Auth API calls
export const authAPI = {
  register: (userData) => api.post('/register/', userData),
  login: (credentials) => api.post('/token/', credentials),
  refreshToken: (refresh) => api.post('/token/refresh/', { refresh }),
};

// Articles API calls
export const articlesAPI = {
  getAll: (params) => api.get('/articles/', { params }),
  getById: (id) => api.get(`/articles/${id}/`),
  create: (data) => api.post('/articles/', data),
  update: (id, data) => api.put(`/articles/${id}/`, data),
  delete: (id) => api.delete(`/articles/${id}/`),
};

// Comments API calls
export const commentsAPI = {
  getForArticle: (articleId) => api.get(`/articles/${articleId}/comments/`),
  create: (articleId, data) => api.post(`/articles/${articleId}/comments/`, data),
  delete: (id) => api.delete(`/comments/${id}/`),
  update: (id, data) => api.put(`/comments/${id}/`, data),
};

export default api; 