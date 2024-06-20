import React from 'react';
import { Outlet, Navigate } from 'react-router-dom';
import Header from '../components/Header';
import Footer from '../components/Footer';
import useToken from '../hooks/useToken';

function Layout() {
                const { token } = useToken();

                return (
                                <>
                                                <Header />
                                                <main>
                                                                {token ? <Outlet /> : <Navigate to="/login" />}
                                                </main>
                                                <Footer />
                                </>
                );
}

export default Layout;