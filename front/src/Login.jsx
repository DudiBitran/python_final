import { useState } from 'react';
import { Form, Button, Container, Alert, Card } from 'react-bootstrap';
import { FaSignInAlt } from 'react-icons/fa';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from './AuthContext';
import { Formik } from 'formik';
import Joi from 'joi';

const loginSchema = Joi.object({
  username: Joi.string().required().messages({
    'string.empty': 'Username is required',
  }),
  password: Joi.string().required().messages({
    'string.empty': 'Password is required',
  }),
});

function Login() {
  const navigate = useNavigate();
  const { login } = useAuth();
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  return (
    <div style={{ minHeight: '100vh', background: 'linear-gradient(135deg, #e0e7ff 0%, #f8fafc 100%)' }}>
      <Container style={{ maxWidth: 400 }} className="py-5 d-flex align-items-center justify-content-center" >
        <Card className="shadow-lg rounded-4 w-100">
          <Card.Body>
            <h3 className="mb-4 text-center fw-bold">Login</h3>
            {error && <Alert variant="danger">{error}</Alert>}
            {success && <Alert variant="success">Login successful! Redirecting...</Alert>}
            <Formik
              initialValues={{ username: '', password: '' }}
              validate={values => {
                const { error } = loginSchema.validate(values, { abortEarly: false });
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
                const result = await login(values.username, values.password);
                setSubmitting(false);
                if (result.success) {
                  setSuccess(true);
                  setTimeout(() => navigate('/'), 1200);
                } else {
                  setError(result.error || 'Login failed');
                }
              }}
            >
              {({ values, errors, touched, handleChange, handleBlur, handleSubmit, isSubmitting }) => (
                <Form noValidate onSubmit={handleSubmit}>
                  <Form.Group className="mb-4" controlId="loginUsername">
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
                  <Form.Group className="mb-4" controlId="loginPassword">
                    <Form.Label className="fw-semibold">Password</Form.Label>
                    <Form.Control
                      type="password"
                      name="password"
                      placeholder="Enter password"
                      value={values.password}
                      onChange={handleChange}
                      onBlur={handleBlur}
                      autoComplete="current-password"
                      size="lg"
                      isInvalid={touched.password && !!errors.password}
                      disabled={isSubmitting}
                    />
                    <Form.Control.Feedback type="invalid">
                      {errors.password}
                    </Form.Control.Feedback>
                  </Form.Group>
                  <Button variant="primary" type="submit" className="w-100 py-2 fs-5 d-flex align-items-center justify-content-center gap-2 rounded-pill shadow-sm" disabled={isSubmitting}>
                    <FaSignInAlt /> {isSubmitting ? 'Logging in...' : 'Login'}
                  </Button>
                </Form>
              )}
            </Formik>
            <div className="text-center mt-4">
              <span>Don't have an account? </span>
              <Link to="/register">Register</Link>
            </div>
          </Card.Body>
        </Card>
      </Container>
    </div>
  );
}

export default Login; 