import { Navbar, Nav, Container, Button } from 'react-bootstrap';
import { NavLink, useNavigate } from 'react-router-dom';
import { useAuth } from './AuthContext';

function AppNavbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <Navbar
      expand="md"
      className="mb-4 navbar-gradient shadow-lg py-2"
      style={{ minHeight: 70 }}
      variant="dark"
    >
      <Container fluid>
        <Navbar.Brand
          as={NavLink}
          to="/"
          className="mx-auto fw-bold fs-3 text-white text-center"
          style={{ letterSpacing: '0.08em' }}
        >
          <span style={{ fontWeight: 900, textShadow: '0 2px 8px #0002' }}>My Articles</span>
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="main-navbar-nav" className="border-0" />
        <Navbar.Collapse id="main-navbar-nav" className="justify-content-center">
          <Nav className="mx-auto align-items-center gap-2">
            <Nav.Link as={NavLink} to="/" end className="nav-pill text-white px-4">
              Home
            </Nav.Link>
            {!user && (
              <>
                <Nav.Link as={NavLink} to="/login" className="nav-pill text-white px-4">
                  Login
                </Nav.Link>
                <Nav.Link as={NavLink} to="/register" className="nav-pill text-white px-4">
                  Register
                </Nav.Link>
              </>
            )}
            {user && (
              <Button
                variant="light"
                onClick={handleLogout}
                className="ms-2 nav-pill px-4 fw-bold text-primary shadow-sm"
                style={{ borderRadius: 999, fontWeight: 700 }}
              >
                Logout
              </Button>
            )}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default AppNavbar; 