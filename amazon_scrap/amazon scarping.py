import requests
from bs4 import BeautifulSoup
import pandas

name_list = []
rating_list = []
reviews_list = []
discounted_price_list = []
old_price_list = []
link_list = []

for i in range(1):
    URL = f"https://www.amazon.in/s?k=earphones+wired&i=electronics&rh=n%3A976419031%2Cp_36%3A1318503031&page=3&crid=2KR2PU76C0SVW&nav_sdd=aps&qid=1698052037&rnid=1318502031&sprefix=earphones+wired&ref=sr_pg_{i}"

    header = {
        "Accept - Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }

    response = requests.get(url=URL, headers=header)
    web_data = response.text
    soup = BeautifulSoup(web_data, "html.parser")
    # print(soup)
    all_headphone_div_tag = soup.find_all(name="div", class_="a-section a-spacing-small puis-padding-left-small puis-padding-right-small")
    # print(all_headphone_div_tag)

    for headphone_div_tag in all_headphone_div_tag:
        try:
            name_tag_text = (headphone_div_tag.find(name="span", class_="a-size-base-plus a-color-base a-text-normal")).getText()
            name_list.append(name_tag_text)
        except:
            name_list.append("NaN")

        try:
            rating = (((headphone_div_tag.find(name="span", class_="a-icon-alt")).getText()).replace("out of", "/")).strip(
                "star")
            rating_list.append(rating)
        except:
            rating_list.append("NaN")

        try:
            total_reviews = (headphone_div_tag.find(name="span", class_="a-size-base s-underline-text")).getText()
            reviews_list.append(total_reviews)
        except:
            reviews_list.append("NaN")

        try:
            discounted_price = (headphone_div_tag.find(name="span", class_="a-offscreen")).getText()
            discounted_price_list.append(discounted_price)
        except:
            discounted_price_list.append("NaN")

        try:
            old_price_tag = headphone_div_tag.find(name="span", class_="a-price a-text-price")
            old_price = (old_price_tag.find(name="span", class_="a-offscreen")).getText()
            old_price_list.append(old_price)
        except:
            old_price_list.append("NaN")

        try:
            item_link = (headphone_div_tag.find(name="a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")).get("href")
            link_list.append("https://www.amazon.in/" + item_link)
        except:
            link_list.append("NaN")

# print(name_list)
# print(rating_list)
# print(reviews_list)
# print(discounted_price_list)
# print(old_price_list)
# print(link_list)

dataframe = {
    "earphone": name_list,
    "rating_star": rating_list,
    "total_reviews": reviews_list,
    "old_price": old_price_list,
    "new_price": discounted_price_list,
    "website_link": link_list,
}

data = pandas.DataFrame(dataframe)
try:
    with open("amazon_headphone.csv", "r") as file:
        file.read()
        data.to_csv("amazon_headphone.csv", mode="a", encoding="utf-8", header=False)
except FileNotFoundError:
    data.to_csv("amazon_headphone.csv", encoding="utf-8",)
