// Header.jsx
import { useState } from "react";
import { Link } from "react-router-dom";
import { FaTimes, FaSearch, FaUser } from 'react-icons/fa';

const Header = ({ handleSearch }) => {
                const [searchTerm, setSearchTerm] = useState("");

                const handleChange = (e) => {
                                setSearchTerm(e.target.value);
                };

                const handleSubmit = (e) => {
                                e.preventDefault();
                                handleSearch(searchTerm);
                                setSearchTerm("");
                };

                const handleKeyPress = (e) => {
                                if (e.key === "Enter") {
                                                handleSubmit(e);
                                }
                };

                const clearSearch = (e) => {
                                setSearchTerm("");
                                e.stopPropagation(); // Empêche la propagation de l'événement de clic
                };

                return (
                                <nav className="navbar">
                                                <ul>
                                                                <li className="left"><Link to="/">Accueil</Link></li>
                                                                <div className="center">
                                                                                <li>
                                                                                                <form onSubmit={handleSubmit}>
                                                                                                                <div className="search-container">
                                                                                                                                <input
                                                                                                                                                type="text"
                                                                                                                                                placeholder="Que souhaitez-vous écouter ?"
                                                                                                                                                value={searchTerm}
                                                                                                                                                onChange={handleChange}
                                                                                                                                                onKeyPress={handleKeyPress}
                                                                                                                                />
                                                                                                                                {searchTerm && (
                                                                                                                                                <div className="clear-icon-container" onClick={clearSearch}>
                                                                                                                                                                <FaTimes className="clear-icon" />
                                                                                                                                                </div>
                                                                                                                                )}
                                                                                                                                {!searchTerm && (
                                                                                                                                                <div className="search-icon-container" onClick={handleSubmit}>
                                                                                                                                                                <FaSearch className="search-icon" />
                                                                                                                                                </div>
                                                                                                                                )}
                                                                                                                </div>
                                                                                                </form>
                                                                                </li>
                                                                </div>
                                                                <div className="right">
                                                                                <li><Link to="/Login">Se connecter</Link></li>
                                                                                <li><Link to="/Register">S'inscrire</Link></li>
                                                                                <li className="UserProfil"><Link to="/profile"><FaUser /></Link></li>
                                                                </div>
                                                </ul>
                                </nav>
                );
};

export default Header;