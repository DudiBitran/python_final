
import './App.css'
import { Routes, Route } from 'react-router-dom';
import AppNavbar from './Navbar';
import ArticleList from './ArticleList';
import ArticleDetail from './ArticleDetail';
import Login from './Login';
import Register from './Register';
import { AuthProvider } from './AuthContext';

function App() {
  return (
    <AuthProvider>
      <AppNavbar />
      <Routes>
        <Route path="/" element={<ArticleList />} />
        <Route path="/article/:id" element={<ArticleDetail />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </AuthProvider>
  );
}

export default App;
