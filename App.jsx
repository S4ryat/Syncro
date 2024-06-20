import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './src/page/Login';
import Register from './src/page/Register';
import Profile from './src/page/Profile';
import Forgot from './src/page/Forgot';
import Home from './src/page/Home';
import Header from './src/components/Header';
import Footer from './src/components/Footer';
import useToken from './src/hooks/useToken';
import Favorites from './src/page/Favorites';
import Player from './src/page/Player';
import Layout from './src/components/Layout';

function App() {
                const { token, setToken } = useToken();

                return (
                                <Router>
                                                <div className="App">
                                                                <Routes>
                                                                                <Route path="/" element={<Layout><Home /></Layout>} />
                                                                                <Route path="/favorites" element={<Favorites />} />
                                                                                <Route path="/player" element={<Player />} />
                                                                                <Route path="/login" element={<Login setToken={setToken} />} />
                                                                                <Route path="/register" element={<Register setToken={setToken} />} />
                                                                                <Route path="/profile" element={<Profile />} />
                                                                                <Route path="/forgot" element={<Forgot />} />
                                                                </Routes>
                                                </div>
                                </Router>
                );
}

export default App;