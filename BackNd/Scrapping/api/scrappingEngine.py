import json 
from flask import Flask , jsonify, request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'YES'
if __name__ == "__main__":
    app.run(debug=True)

@app.route('/find/<string:n>')
def scrape_flipkart_search(n):
    headers = {
        'authority': 'www.flipkart.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    try:
        search_url = f'https://www.flipkart.com/search?q={keyword.replace(" ", "+")}'
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('div', class_="_2kHMtA")
        for product in products:
           if(product): 
            # print(product)
            # print("cat1")
            title_element = product.find('div', class_='_4rR01T')
            price_element = product.find('div', class_='_30jeq3 _1_WHN1')
            link_element = product.find('a', class_='_1fQZEK')
            
            if title_element and price_element:
                product_title = title_element.get_text(strip=True)
                print(f"Product Title: {product_title}")
            else:
                continue
            if title_element and price_element:
                product_price = price_element.get_text(strip=True)
                print(f"Product Price: {product_price}")
            else:
                continue    

            if link_element and title_element:
                link = link_element.get('href', '')
                print(f"Product Link:  https://www.flipkart.com{link}")  
            else:
                continue      

            print("----------------------")
        products1 = soup.find_all('div', class_="_4ddWXP")    
        for product in products1:
        #   print(product)
          if(product):
            # print("cat2")
            title_element = product.find('a', class_='s1Q9rs')
            price_element = product.find('div', class_='_30jeq3')
            link_element = product.find('a', class_='_2rpwqI')
            if title_element and price_element:
                product_title = title_element.get_text(strip=True)
                print(f"Product Title: {product_title}")
            else:
                continue  
            if title_element and price_element:
                product_price = price_element.get_text(strip=True)
                print(f"Product Price: {product_price}")
            else:
                continue
            if link_element and title_element:
                link = link_element.get('href', '')
                print(f"Product Link:  https://www.flipkart.com{link}")    
            else:
                continue
            print("----------------------")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")