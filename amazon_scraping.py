#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import the necessary libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Function to scrape Amazon product details
def scrape_amazon_product(url):
    # Configure Selenium with ChromeDriver
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')  # Replace with the path to your ChromeDriver

    # Open the URL
    driver.get(url)

    # Allow time for the page to load
    time.sleep(5)

    # Get the page source
    page_source = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract product details (example: product name, price, etc.)
    # Adjust the selectors based on the structure of the Amazon product page
    product_name = soup.select_one('#productTitle').text.strip()
    product_price = soup.select_one('#priceblock_ourprice').text.strip()

    # You can extract other details like product reviews, ratings, etc. similarly

    # Return the product details as a dictionary
    product_details = {
        'name': product_name,
        'price': product_price,
        # Add other details as needed
    }

    return product_details

if __name__ == "__main__":
    # Provide the URL of the Amazon product you want to scrape
    product_url = 'https://www.amazon.com/s?k=activity+trackers+and+smartwatches&page=2&pd_rd_r=74e85078-91c4-4b00-a5f5-eb0713a9fe95&pd_rd_w=3bxLe&pd_rd_wg=Sz2m0&pf_rd_p=33f8f65b-b95c-44af-8b89-e59e69e79828&pf_rd_r=F1WHAGYZN7H3SEAFH6ZH&qid=1689846341&ref=sr_pg_1'

    # Scrape the product details
    scraped_product = scrape_amazon_product(product_url)

    # Print the results
    print("Product Name:", scraped_product['name'])
    print("Product Price:", scraped_product['price'])


# In[5]:


# Import the necessary libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Function to scrape product details from the Amazon search results page
def scrape_amazon_search_results(url):
    # Configure Selenium with ChromeDriver
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')  # Replace with the path to your ChromeDriver

    # Open the URL
    driver.get(url)

    # Allow time for the page to load
    time.sleep(5)

    # Get the page source
    page_source = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all product containers on the page
    product_containers = soup.select('.s-result-item')

    # Initialize an empty list to store product details
    products = []

    # Loop through each product container and extract title and price
    for container in product_containers:
        # Extract product title
        title_element = container.select_one('.a-text-normal')
        if title_element:
            product_title = title_element.text.strip()
        else:
            product_title = "N/A"

        # Extract product price
        price_element = container.select_one('.a-offscreen')
        if price_element:
            product_price = price_element.text.strip()
        else:
            product_price = "N/A"

        # Append product details to the products list
        products.append({
            'title': product_title,
            'price': product_price
        })

    return products

if __name__ == "__main__":
    # Provide the URL of the Amazon search results page
    search_results_url = 'https://www.amazon.com/s?k=activity+trackers+and+smartwatches&page=2&pd_rd_r=74e85078-91c4-4b00-a5f5-eb0713a9fe95&pd_rd_w=3bxLe&pd_rd_wg=Sz2m0&pf_rd_p=33f8f65b-b95c-44af-8b89-e59e69e79828&pf_rd_r=F1WHAGYZN7H3SEAFH6ZH&qid=1689846341&ref=sr_pg_1'

    # Scrape the product details from the search results page
    scraped_products = scrape_amazon_search_results(search_results_url)

    # Print the results
    for idx, product in enumerate(scraped_products, start=1):
        print(f"Product {idx}:")
        print("Title:", product['title'])
        print("Price:", product['price'])
        print("--------------------")


# In[ ]:




