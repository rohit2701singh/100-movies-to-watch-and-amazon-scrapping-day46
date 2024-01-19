# use google colab to run this program ; https://colab.research.google.com/drive/1eZWFQV41Zfu2c8y2NOdorwxv6dTVfq6d#scrollTo=GBhmNEf_e_vi
# top movies with other details

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
web_data = response.text
# print(web_data)
soup = BeautifulSoup(web_data, "html.parser")

title_data = soup.find_all(name="h3", attrs={"class": "title"})

title_list = []
for item in title_data:
    title = item.getText()
    title_list.append(title)

title_name = title_list[::-1]

description_data = soup.find_all(name="div", class_="descriptionWrapper")
# print(description_data)

release_year_list = []
description_list = []
for item in description_data:
    para_tag = item.find_all(name="p")
    # print(para_tag)

    for tags in para_tag[1:2]:
        para_content = tags.getText()
        description = (para_content[3:]).strip("Read Empire's review of Stand By MeBuy the film now")
        description_list.append(description)
        # print(description)
        release_year_list.append(para_content[0:4])

# print(release_year_list)
# print(description_list)

release_year = release_year_list[::-1]
movie_brief = description_list[::-1]

print(release_year)
print(movie_brief)
print(title_name)