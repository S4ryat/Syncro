import React, { useState } from 'react';


// const backendUrl = import.meta.env.VITE_BACKEND_URL + "/api/forgotPassword";

const Forgot = () => {
                const [email, setEmail] = useState('');
                const [newPassword, setNewPassword] = useState('');
                const [confirmPassword, setConfirmPassword] = useState('');
                const [error, setError] = useState('');
                const [message, setMessage] = useState('');
                const [isLoading, setIsLoading] = useState(false);

                const handleSubmit = async (e) => {
                                e.preventDefault();
                                if (newPassword !== confirmPassword) {
                                                setError('Les mots de passe ne correspondent pas');
                                                return;
                                }

                                const url = process.env.REACT_APP_BACKEND_URL + "/api/forgotPassword";

                                setIsLoading(true);
                                try {
                                                const response = await fetch(url, {
                                                                method: 'POST',
                                                                headers: {
                                                                                'Content-Type': 'application/json'
                                                                },
                                                                body: JSON.stringify({ email, newPassword })
                                                });

                                                if (!response.ok) {
                                                                const errorMessage = await response.text();
                                                                throw new Error(errorMessage || 'Une erreur est survenue');
                                                }

                                                const responseData = await response.json();
                                                if (responseData.success === false) {
                                                                setError(responseData.message);
                                                } else {
                                                                setMessage(responseData.message);
                                                }
                                } catch (error) {
                                                console.error('Erreur lors de la requête:', error.message);
                                                setError('Une erreur est survenue. Veuillez réessayer.');
                                } finally {
                                                setIsLoading(false);
                                }
                };

                return (
                                <div className="form-box login">
                                                <h2 style={{ color: 'white', textAlign: 'center' }}>Mot de passe oublié</h2>
                                                <form onSubmit={handleSubmit}>
                                                                <div className="input-box">
                                                                                <input
                                                                                                type="email"
                                                                                                value={email}
                                                                                                onChange={(e) => setEmail(e.target.value)}
                                                                                                placeholder="Entrez votre email"
                                                                                                required
                                                                                />
                                                                </div>
                                                                <div className="input-box">
                                                                                <input
                                                                                                type="password"
                                                                                                value={newPassword}
                                                                                                onChange={(e) => setNewPassword(e.target.value)}
                                                                                                placeholder="Nouveau mot de passe"
                                                                                                required
                                                                                                className="input"
                                                                                />
                                                                </div>
                                                                <div className="input-box">
                                                                                <input
                                                                                                type="password"
                                                                                                value={confirmPassword}
                                                                                                onChange={(e) => setConfirmPassword(e.target.value)}
                                                                                                placeholder="Confirmer le mot de passe"
                                                                                                required
                                                                                                className="input password-confirm"
                                                                                />
                                                                </div>
                                                                <button type="submit" disabled={isLoading}>
                                                                                {isLoading ? 'Réinitialisation...' : 'Réinitialiser le mot de passe'}
                                                                </button>
                                                </form>
                                                {error && <div className="error">{error}</div>}
                                                {message && <div className="message">{message}</div>}
                                </div>
                );
};

export default Forgot;
