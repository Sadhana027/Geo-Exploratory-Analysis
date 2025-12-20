const http = require('http');

// Institution data
const institutionData = {
    "IIT_Bombay": { name: "IIT Bombay", cafes: 5, gyms: 3 },
    "NITIE_Mumbai": { name: "NITIE Mumbai", cafes: 4, gyms: 2 },
    "IIT_Hyderabad": { name: "IIT Hyderabad", cafes: 6, gyms: 4 },
    "NIT_Warangal": { name: "NIT Warangal", cafes: 7, gyms: 5 },
    "IIT_Delhi": { name: "IIT Delhi", cafes: 8, gyms: 6 },
    "NIT_Delhi": { name: "NIT Delhi", cafes: 3, gyms: 2 },
};

// Create an HTTP server
const server = http.createServer((req, res) => {
    if (req.method === 'POST' && req.url === '/submit-preferences') {
        let body = '';
        
        // Collect data from the request
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', () => {
            const preferences = JSON.parse(body);
            const institution = institutionData[preferences.institution];
            
            if (institution) {
                const response = {
                    institution: institution.name,
                    cafes: institution.cafes,
                    gyms: institution.gyms,
                    preferences: {
                        sports: preferences.sports,
                        eating_out: preferences.eating_out,
                        income: preferences.income,
                    }
                };

                // Send the response
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify(response));
            } else {
                res.writeHead(404, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify({ error: 'Institution not found' }));
            }
        });
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Route not found');
    }
});

// Start the server
server.listen(3000, () => {
    console.log('Server running at http://localhost:3000/');
});
