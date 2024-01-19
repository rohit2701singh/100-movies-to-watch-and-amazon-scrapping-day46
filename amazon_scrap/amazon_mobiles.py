import requests
from bs4 import BeautifulSoup
import pandas


name_list = []
rating_list = []
reviews_list = []
discounted_price_list = []
old_price_list = []
link_list = []

for i in range(5):
    URL = f"https://www.amazon.in/s?k=mobile&i=electronics&rh=n%3A1389401031&page={i}&qid=1698089015&ref=sr_pg_{i}"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    response = requests.get(url=URL, headers=header)
    web_data = response.text
    soup = BeautifulSoup(web_data, "html.parser")

    all_div_tag = (soup.find_all(name="div", class_="a-section a-spacing-small a-spacing-top-small"))[1:]
    # print(all_headphone_div_tag)

    for single_div_tag in all_div_tag:
        try:
            name_tag_text = (single_div_tag.find(name="span", class_="a-size-medium a-color-base a-text-normal")).getText()
            name_list.append(name_tag_text)
            # print(name_tag_text)
        except:
            name_list.append("unknown")

        try:
            rating = (((single_div_tag.find(name="span", class_="a-icon-alt")).getText()).replace("out of", "/")).strip(
                "star")
            rating_list.append(rating)
            # print(rating)
        except:
            rating_list.append("unknown")

        try:
            total_reviews = (single_div_tag.find(name="span", class_="a-size-base s-underline-text")).getText()
            reviews_list.append(total_reviews)
            # print(total_reviews)
        except:
            reviews_list.append("unknown")

        try:
            discounted_price = single_div_tag.find(name="span", class_="a-offscreen").getText()
            discounted_price_list.append(discounted_price)
            # print(discounted_price)
        except:
            discounted_price_list.append("unknown")

        try:
            old_price= (single_div_tag.find_all(name="span", class_="a-offscreen"))[-1].getText()
            old_price_list.append(old_price)
        except:
            old_price_list.append("unknown")

        try:
            item_link = (single_div_tag.find(name="a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")).get("href")
            link_list.append("https://www.amazon.in/" + item_link)
        except:
            link_list.append("link not found")

print(name_list)
print(rating_list)
print(reviews_list)
print(discounted_price_list)
print(old_price_list)
print(link_list)

dataframe = {
    "name": name_list,
    "rating_star": rating_list,
    "total_reviews": reviews_list,
    "old_price": old_price_list,
    "new_price": discounted_price_list,
    "website_link": link_list,
}

data = pandas.DataFrame(dataframe)
print(data)
try:
    with open("amazon_mobile.csv", "r") as file:
        file.read()
        data.to_csv("amazon_mobile.csv", mode="a", encoding="utf-8", header=False)
except FileNotFoundError:
    data.to_csv("amazon_mobile.csv", mode="a", encoding="utf-8",)
