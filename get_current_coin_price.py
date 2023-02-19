from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options
import time    
import requests


def get_current_coin_price(coin_type):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f'https://www.pionex.com/zh-TW/trade/{coin_type}/Manual')
    time.sleep(10)
    soup = bs(driver.page_source, 'lxml')
    price = soup.find_all('title')
    for p in price:
        s = p.string
        
    driver.close()
    
    end = 0
    
    for i in range(len(s)):
        if s[i] == "|":
            end = i
            break
            
    return float(s[:end])

def get_coin_news_url(coin):
  
  url = f'https://news.bitcoin.com/?s={coin}'
  headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"}
  
  
  response = requests.get(url, headers = headers)
  response.encoding = 'utf-8'
  
  soup = bs(response.text, 'html.parser')
  
  a_tags = soup.find_all('a')
  
  url = ''
  for a in a_tags[23:39:3]:
    # print(a.get('href'))
    url += a.get('href') + '\n'
      
  return url