# app.py
from flask import Flask, request, make_response
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/proxy')
def proxy():
    query = request.args.get('query', '')
    bing_url = f'https://www.bing.com/search?q={query}'
    response = requests.get(bing_url)

    # Check if the response contains a blocked screen
    if 'Blocked' in response.text:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find and remove the blocked screen element
        blocked_element = soup.find('div', {'id': 'blocked-screen'})
        if blocked_element:
            blocked_element.decompose()
        # Create a new response without the blocked screen element
        modified_response = make_response(soup.prettify())
        modified_response.headers['Content-Type'] = 'text/html'
        return modified_response

    return response.content

if __name__ == '__main__':
    app.run(port=5000, debug=True)
