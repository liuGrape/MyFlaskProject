import requests
from bs4 import BeautifulSoup

Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get('https://github.com/liuGrape', headers=Headers)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.find_all("div"))
