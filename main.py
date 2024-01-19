# top movies web scrap(title)
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
web_data = response.text
# print(web_data)
soup = BeautifulSoup(web_data, "html.parser")

title_data = soup.find_all(name="h3", attrs={"class": "title"})
release_year_tag = soup.find_all(name="strong")

# print(title_data)

title_list = []
for item in title_data:
    title = item.getText()
    title_list.append(title)

title_name = title_list[::-1]

for item in title_name:
    with open("movies.txt", "a", encoding='utf-8') as file:
        file.write(f"{item}\n")
