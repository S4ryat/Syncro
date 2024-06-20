import React from 'react';
import { FaTwitterSquare } from "react-icons/fa";
import { BsFacebook } from "react-icons/bs";
import { AiFillInstagram } from "react-icons/ai";

const Footer = () => {
                const footerStyle = {
                                backgroundColor: 'black',
                                color: 'white',
                                padding: '20px',
                                width: '100%',
                                position: 'fixed',
                                bottom: '0',
                                left: '0',
                                display: 'flex',
                                justifyContent: 'space-between',
                                flexDirection: 'row-reverse', // Inverse l'ordre des éléments
                };

                const socialMediaSectionStyle = {
                                textAlign: 'right', // Aligne les icônes à droite
                };

                const socialIconsStyle = {
                                listStyleType: 'none',
                                padding: '0',
                                margin: '0',
                };

                const socialIconItemStyle = {
                                display: 'inline',
                                marginRight: '10px',
                };

                const iconStyle = {
                                color: 'white',
                                fontSize: '24px',
                                transition: 'color 0.3s ease',
                };

                const footerBottomStyle = {
                                textAlign: 'left', // Aligne le texte à gauche
                };

                const iconHoverStyle = (e) => {
                                e.target.style.color = 'gray';
                };

                const iconUnhoverStyle = (e) => {
                                e.target.style.color = 'white';
                };

                return (
                                <footer style={footerStyle}>
                                                <div style={socialMediaSectionStyle}>
                                                                <ul style={socialIconsStyle}>
                                                                                <li style={socialIconItemStyle}>
                                                                                                <a href="https://twitter.com">
                                                                                                                <FaTwitterSquare
                                                                                                                                style={iconStyle}
                                                                                                                                onMouseOver={iconHoverStyle}
                                                                                                                                onMouseOut={iconUnhoverStyle}
                                                                                                                />
                                                                                                </a>
                                                                                </li>
                                                                                <li style={socialIconItemStyle}>
                                                                                                <a href="https://facebook.com">
                                                                                                                <BsFacebook
                                                                                                                                style={iconStyle}
                                                                                                                                onMouseOver={iconHoverStyle}
                                                                                                                                onMouseOut={iconUnhoverStyle}
                                                                                                                />
                                                                                                </a>
                                                                                </li>
                                                                                <li style={socialIconItemStyle}>
                                                                                                <a href="https://instagram.com">
                                                                                                                <AiFillInstagram
                                                                                                                                style={iconStyle}
                                                                                                                                onMouseOver={iconHoverStyle}
                                                                                                                                onMouseOut={iconUnhoverStyle}
                                                                                                                />
                                                                                                </a>
                                                                                </li>
                                                                </ul>
                                                </div>

                                                <div style={footerBottomStyle}>
                                                                <p>&copy; 2024 Your Company. All rights reserved.</p>
                                                </div>
                                </footer>
                );
}

export default Footer;
