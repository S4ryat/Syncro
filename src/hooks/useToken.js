import { useState } from 'react';

export function getToken() {
                const tokenString = sessionStorage.getItem('token');
                const userToken = JSON.parse(tokenString);
                return userToken?.token;
}

export function setToken(userToken) {
                sessionStorage.setItem('token', JSON.stringify(userToken));
}

export default function useToken() {
                const [token, setTokenState] = useState(getToken());

                const saveToken = (userToken) => {
                                setToken(userToken);
                                setTokenState(userToken?.token);
                };

                return {
                                token,
                                setToken: saveToken,
                };
}
