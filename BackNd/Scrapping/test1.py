import requests
from bs4 import BeautifulSoup
headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.amazon.com/',
    'Connection': 'keep-alive',
    }
response = requests.get('https://www.amazon.com/s?k="laptop"', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
title=soup.select_one('title')
products = soup.find_all('div', class_="puisg-col-inner")
# print(products)
for product in products:
           if(product): 
            # print(product)
            # print("cat1")
            title_element = product.find('span', class_='a-size-medium a-color-base a-text-normal')
            price_element = product.find('span', class_='a-offscreen')
            link_element = product.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
            img_element = product.find('img', class_='s-image') 
            if img_element and title_element:
                img = img_element.get('src', '')
                print(f'Product Image: {img}')
            else:
                continue
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
                print(f"Product Link:  https://www.amazon.in/{link}")  
            else:
                continue 
