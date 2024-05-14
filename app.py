# app.py
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/proxy')
def proxy():
    query = request.args.get('query', '')
    bing_url = f'https://www.bing.com/search?q={query}'
    response = requests.get(bing_url)
    return response.content

if __name__ == '__main__':
    app.run(port=5000, debug=True)
