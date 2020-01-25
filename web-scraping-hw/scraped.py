from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 
import time
import re

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=True)

def pyscript ():
    url1 = 'https://mars.nasa.gov/news/'
    browser.visit(url1)
    time.sleep(3)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(1)

    headlines = soup.find_all(class_="content_title")
    bodys = soup.find_all(class_="article_teaser_body")
    time.sleep(1)

    nasa_headline = headlines[0].a.text
    news_body = bodys[0].text

    print(nasa_headline)
    print(news_body)
    
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    time.sleep(3)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find(class_='carousel_item')['style']
    time.sleep(1)

    start = image.find("url('")
    end = image.find("');") 
    url = image[start+len("url('"):end]
    image_url = ('https://www.jpl.nasa.gov'+url) 
    print(image_url)

    url4 = 'https://space-facts.com/mars/'
    tables = pd.read_html(url4)
    time.sleep(2)
    
    table1 = tables[0]
    mars_table = table1.to_html()
    print(mars_table)
    time.sleep(1)

    final = {
        "headline": nasa_headline,
        "body": news_body,
        "image": image_url,
        "table": mars_table
    }
    
    browser.quit()
    
    return final