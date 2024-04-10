from flask import Flask , jsonify, request
from bs4 import BeautifulSoup
from scrap1 import scrape_flipkart_search, scrape_amazon_search
app = Flask(__name__)

@app.route('/amazon/<keyword>')
def amazon_search(keyword):
    results = scrape_amazon_search(keyword)
    return jsonify(results)

@app.route('/flipkart/<keyword>')
def flipkart_search(keyword):
    results = scrape_flipkart_search(keyword)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
