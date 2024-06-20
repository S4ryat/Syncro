import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { FaUser, FaLock, FaEnvelope } from 'react-icons/fa';
import { Link } from 'react-router-dom';


// Utiliser la variable d'environnement REACT_APP_BACKEND_URL
// const backendUrl = import.meta.env.VITE_BACKEND_URL + "/api/login";

async function registerUser(credentials) {
  try {
    const response = await fetch(backendUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(credentials),
    });
    if (!response.ok) {
      throw new Error('Registration failed');
    }
    return await response.json();
  } catch (error) {
    console.error('Error during registration:', error);
    throw error;
  }
}

const Register = ({ setToken }) => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const token = await registerUser({ username, email, password });
      setToken(token);
    } catch (error) {
      setError('Une erreur s\'est produite lors de l\'inscription');
    }
  };

  return (
    <div>
      <div className="form-box register">
        <form onSubmit={handleSubmit}>
          <h1>Register</h1>
          <div className="input-box">
            <input
              type="text"
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
            <FaUser className="icon" />
          </div>
          <div className="input-box">
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <FaEnvelope className="icon" />
          </div>
          <div className="input-box">
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <FaLock className="icon" />
          </div>
          {error && <p className="error-message">{error}</p>}
          <button type="submit">Register</button>
          <div className="login-link">
            <p>
              Already have an account? <Link to="/login">Login</Link>
            </p>
          </div>
        </form>
      </div>
    </div>
  );
};

Register.propTypes = {
  setToken: PropTypes.func.isRequired,
};

export default Register;
