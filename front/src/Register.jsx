import { useState } from 'react';
import { Form, Button, Container, Alert, Card } from 'react-bootstrap';
import { FaUserPlus } from 'react-icons/fa';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from './AuthContext';
import { Formik } from 'formik';
import Joi from 'joi';

const registerSchema = Joi.object({
  username: Joi.string().min(3).required().messages({
    'string.empty': 'Username is required',
    'string.min': 'Username must be at least 3 characters',
  }),
  email: Joi.string().email({ tlds: { allow: false } }).required().messages({
    'string.empty': 'Email is required',
    'string.email': 'Email must be valid',
  }),
  password: Joi.string().min(8)
    .pattern(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/)
    .required()
    .messages({
      'string.empty': 'Password is required',
      'string.min': 'Password must be at least 8 characters',
      'string.pattern.base': 'Password must contain at least 8 characters, including one uppercase letter, one lowercase letter, and one number. Only letters and digits are allowed.'
    }),
});

function formatError(err) {
  if (!err) return '';
  if (typeof err === 'string') return err;
  if (Array.isArray(err)) return err.map(formatError).join(' ');
  if (typeof err === 'object') {
    return Object.values(err).map(formatError).join(' ');
  }
  return String(err);
}

function Register() {
  const navigate = useNavigate();
  const { register } = useAuth();
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  return (
    <div style={{ minHeight: '100vh', background: 'linear-gradient(135deg, #fdf6e3 0%, #f8fafc 100%)' }}>
      <Container style={{ maxWidth: 400 }} className="py-5 d-flex align-items-center justify-content-center" >
        <Card className="shadow-lg rounded-4 w-100">
          <Card.Body>
            <h3 className="mb-4 text-center fw-bold">Register</h3>
            {error && <Alert variant="danger">{error}</Alert>}
            {success && <Alert variant="success">Registration successful! Redirecting to login...</Alert>}
            <Formik
              initialValues={{ username: '', email: '', password: '' }}
              validate={values => {
                const { error } = registerSchema.validate(values, { abortEarly: false });
                if (!error) return {};
                const errors = {};
                error.details.forEach(detail => {
                  errors[detail.path[0]] = detail.message;
                });
                return errors;
              }}
              onSubmit={async (values, { setSubmitting }) => {
                setError('');
                setSuccess(false);
                setSubmitting(true);
                const result = await register(values);
                setSubmitting(false);
                if (result.success) {
                  setSuccess(true);
                  setTimeout(() => navigate('/login'), 1200);
                } else {
                  setError(formatError(result.error) || 'Registration failed');
                }
              }}
            >
              {({ values, errors, touched, handleChange, handleBlur, handleSubmit, isSubmitting }) => (
                <Form noValidate onSubmit={handleSubmit}>
                  <Form.Group className="mb-4" controlId="registerUsername">
                    <Form.Label className="fw-semibold">Username</Form.Label>
                    <Form.Control
                      type="text"
                      name="username"
                      placeholder="Enter username"
                      value={values.username}
                      onChange={handleChange}
                      onBlur={handleBlur}
                      autoComplete="username"
                      size="lg"
                      isInvalid={touched.username && !!errors.username}
                      disabled={isSubmitting}
                    />
                    <Form.Control.Feedback type="invalid">
                      {errors.username}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Form.Group className="mb-4" controlId="registerEmail">
                    <Form.Label className="fw-semibold">Email</Form.Label>
                    <Form.Control
                      type="email"
                      name="email"
                      placeholder="Enter email"
                      value={values.email}
                      onChange={handleChange}
                      onBlur={handleBlur}
                      autoComplete="email"
                      size="lg"
                      isInvalid={touched.email && !!errors.email}
                      disabled={isSubmitting}
                    />
                    <Form.Control.Feedback type="invalid">
                      {errors.email}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Form.Group className="mb-4" controlId="registerPassword">
                    <Form.Label className="fw-semibold">Password</Form.Label>
                    <Form.Control
                      type="password"
                      name="password"
                      placeholder="Enter password"
                      value={values.password}
                      onChange={handleChange}
                      onBlur={handleBlur}
                      autoComplete="new-password"
                      size="lg"
                      isInvalid={touched.password && !!errors.password}
                      disabled={isSubmitting}
                    />
                    <Form.Control.Feedback type="invalid">
                      {errors.password}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Button variant="success" type="submit" className="w-100 py-2 fs-5 d-flex align-items-center justify-content-center gap-2 rounded-pill shadow-sm" disabled={isSubmitting}>
                    <FaUserPlus /> {isSubmitting ? 'Registering...' : 'Register'}
                  </Button>
                </Form>
              )}
            </Formik>
            <div className="text-center mt-4">
              <span>Already have an account? </span>
              <Link to="/login">Login</Link>
            </div>
          </Card.Body>
        </Card>
      </Container>
    </div>
  );
}

export default Register; 