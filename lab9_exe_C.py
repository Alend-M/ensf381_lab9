import requests
import json

url = 'https://dummyjson.com/products'

def fetch_product_data(url):
    try:
        response = requests.get(url)
        
        response.raise_for_status()
        
        return response.json()['products']

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    
def list_all_products(products):
    for product in products:
        print(f"Product: {product['title']}, Price: ${product['price']}, Stock: {product['stock']}")
    
    
        
        