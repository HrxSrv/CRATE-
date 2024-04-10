import requests
from bs4 import BeautifulSoup
product_amazon= []
product_flipkart=[]
def scrape_amazon_search(keyword):
    headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
   }

    
    try:
        search_url = f'https://www.amazon.in/s?k={keyword.replace(" ", "+")}'
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('div', class_="puisg-row")
        # print(products)
        for product in products:
           if(product): 
            title_element = product.find('span', class_='a-size-medium a-color-base a-text-normal')
            price_element = product.find('span', class_='a-price-whole')
            link_element = product.find('a', class_='a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal')
            img_element = product.find('img', class_='s-image') 
            if img_element and title_element:
                img = img_element.get('src', '')
                # print(f'Product Image: {img}')
            else:
                continue
            if title_element and price_element:
                product_title = title_element.get_text(strip=True)
                # print(f"Product Title: {product_title}")
            else:
                continue
            if title_element and price_element:
                product_price = price_element.get_text(strip=True)
                # print(f"Product Price: {product_price}")
            else:
                continue    

            if link_element and title_element:
                link = link_element.get('href', '')
                link = "Product Link:  https://www.amazon.in/{link}" 
            else:
                continue 
            product_amazon.append({"title":product_title,"price":product_price,"img":img,"link":link})          
            # print("----------------------")
        # print(product_amazon)        
        products1 = soup.find_all('div', class_="puis-card-container s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-vbok7i09ua2q62ek5q2l21tt78 s-latency-cf-section puis-card-border")    
        for product in products1:
          if(product):
            # print("cat2")
            title_element = product.find('span', class_='a-size-base-plus a-color-base a-text-normal')
            price_element = product.find('span', class_='a-price-whole')
            link_element = product.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
            img_element = product.find('img', class_='s-image') 
            if img_element and title_element:
                img = img_element.get('src', '')
                # print(f'Product Image: {img}')
            else:
                continue
            if title_element and price_element:
                product_title = title_element.get_text(strip=True)
                # print(f"Product Title: {product_title}")
            else:
                continue
            if title_element and price_element:
                product_price = price_element.get_text(strip=True)
                # print(f"Product Price: {product_price}")
            else:
                continue    

            if link_element and title_element:
                link = link_element.get('href', '')
                link = "Product Link:  https://www.amazon.in/{link}" 
            else:
                continue 
            product_amazon.append({"title":product_title,"price":product_price,"img":img,"link":link})          
            # print("----------------------")
        # print(product_amazon1) 
    
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
    return product_amazon    
def scrape_flipkart_search(keyword):
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
            img_element = product.find('img', class_='_396cs4')
            if img_element and title_element:
                img = img_element.get('src', '')
                # print(f'Product Image: {img}')
            else:
                continue
            if title_element and price_element:
                product_title = title_element.get_text(strip=True)
                # print(f"Product Title: {product_title}")
            else:
                continue
            if title_element and price_element:
                product_price = price_element.get_text(strip=True)
                product_price = product_price.replace("₹", "")
                # print(f"Product Price: {product_price}")
            else:
                continue    

            if link_element and title_element:
                link = link_element.get('href', '')
                link = f"Product Link:  https://flipkart.com/{link}" 
            else:
                continue 
            product_flipkart.append({"title":product_title,"price":product_price,"img":img,"link":link})          
            # print("----------------------")
        # print(product_flipkart)
        products1 = soup.find_all('div', class_="_4ddWXP")    
        for product in products1:
        #   print(product)
          if(product):
            # print("cat2")
            title_element = product.find('a', class_='s1Q9rs')
            price_element = product.find('div', class_='_30jeq3')
            link_element = product.find('a', class_='_2rpwqI')
            img_element = product.find('img', class_='_396cs4')
            if img_element and title_element:
                img = img_element.get('src', '')
                # print(f'Product Image: {img}')
            else:
                continue
            if title_element and price_element:
                product_title = title_element.get_text(strip=True)
                # print(f"Product Title: {product_title}")
            else:
                continue
            if title_element and price_element:
                product_price = price_element.get_text(strip=True)
                # print(f"Product Price: {product_price}")
            else:
                continue    

            if link_element and title_element:
                link = link_element.get('href', '')
                link = "Product Link:  https://flipkart.com/{link}" 
            else:
                continue 
            product_flipkart.append({"title":product_title,"price":product_price,"img":img,"link":link})          
            # print("----------------------")

        # print(product_flipkart1)

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
    return product_flipkart    
# search_keyword = 'laptop'
# print("results from flipkart")
# scrape_flipkart_search(search_keyword)
# print("results from amazon")
# scrape_amazon_search(search_keyword)
