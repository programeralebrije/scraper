from urllib import request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.underarmour.com/en-us/c/mens/shoes/"

Request_page = urlopen (url_to_scrape)
page_html = Request_page.read()
Request_page.close()

html_soup = BeautifulSoup(page_html, "html.parser")

shoes_list = html_soup.find_all ('div' , class_ = "l-plp-container men-footwear")

filename = "UnderArmour_Shoes.csv"
f = open(filename, "w")

headers = "title, Product_Name, Price\n"

f.write(headers)

for shoes in shoes_list:
    title = shoes.find("div", class_="product-listing-title").text
    price = shoes.find("div", class_="product-listing-price").text
    print (shoes.div.a["href"])

    f.write(title + "," + Product_Name + "," + Price + "\n")

    f.close