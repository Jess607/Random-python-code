import requests
import lxml
from bs4 import BeautifulSoup

name = "https://www.rottentomatoes.com/top/bestofrt/"
header = {
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
source = requests.get(name, headers = header).text

soup=BeautifulSoup(source, 'lxml')

print(soup.prettify())

