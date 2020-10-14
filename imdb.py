import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls055386972/"

response = requests.get(url, headers={"Accept-Language":"en-US"})
# response contains some HTML
# print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.title.string)

movies = soup.find_all('div', class_='lister-item-content')
# print(movie)

for movie in movies:
    print(movie.find('h3').find('a').string)
    print(movie.find('span', class_='runtime').string.strip(' min'))
