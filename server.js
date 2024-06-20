const express = require('express');
const app = express();
const port = 3001;

app.use(express.json());

app.post('/api/login', (req, res) => {
                const { username, password } = req.body;
                if (username === 'testuser' && password === 'testpassword') {
                                res.json({ token: 'mock-token' });
                } else {
                                res.status(401).json({ message: 'Login failed' });
                }
});

app.listen(port, () => {
                console.log(`Mock server running at http://localhost:${port}`);
});
