// server.js
const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

app.get('/proxy', async (req, res) => {
  const { query } = req.query;
  const bingUrl = `https://www.bing.com/search?q=${encodeURIComponent(query)}`;
  try {
    const response = await axios.get(bingUrl);
    res.send(response.data);
  } catch (error) {
    res.status(500).send('Error fetching data from Bing.');
  }
});

app.listen(PORT, () => {
  console.log(`Proxy server running on port ${PORT}`);
});
