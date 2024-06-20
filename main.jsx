import React from 'react';
import { createRoot } from 'react-dom/client';  // Importer createRoot depuis react-dom/client

import './index.css';
import './App.css'
import App from './App';  // Assurez-vous d'importer correctement votre composant principal

const root = createRoot(document.getElementById('root'));  // Créer la racine avec createRoot
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
