import axios from 'axios';
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { FaUser, } from 'react-icons/fa';
import { Link } from 'react-router-dom';

const useLoginUser = (credentials, setToken, setError) => {
  const loginUser = async () => {
    try {
      const response = await axios.post('http://localhost:3001/api/login', credentials);
      setToken(response.data.token);
    } catch (error) {
      setError('Une erreur s\'est produite lors de la connexion');
    }
  };

  return loginUser;
};

const Login = ({ setToken }) => {
  const [username, setUsername] = useState('');
  // const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  // const [rememberMe, setRememberMe] = useState(false);

  const loginUser = useLoginUser({ username, password }, setToken, setError);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await loginUser();
  };

  return (
    <div>
      <div className="form-box login">
        <form onSubmit={handleSubmit}>
          <h1>Login</h1>
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
          {/* <div className="input-box">
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <FaLock className="icon" />
          </div> */}
          <div className="remember-forgot">
            {/* <label>
              <input
                type="checkbox"
                checked={rememberMe}
                onChange={(e) => setRememberMe(e.target.checked)}
              />{' '}
              Remember me
            </label> */}
            <p className="forgot-password">
              <Link to="/forgot">Forgot password?</Link>
            </p>
          </div>
          {error && <p className="error-message">{error}</p>}
          <button type="submit">Login</button>
          <div className="register-link">
            <p>
              Don't have an account? <Link to="/register">Register</Link>
            </p>
          </div>
        </form>
      </div>
    </div>
  );
};

Login.propTypes = {
  setToken: PropTypes.func.isRequired,
};

export default Login;
