from bs4 import BeautifulSoup
import requests
#Install and import BeautifulSoup from the bs4 module.
#Write a simple program to parse a small HTML string.
html_doc = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <a href="https://example.com">Click Here</a>
  </body>
</html>
"""

#parse the html
soup = BeautifulSoup(html_doc,features="html.parser")
print(soup) #html gets printed
#Given this HTML:
#Extract the title text.
title = soup.title.text
print("Title:",title)
#Extract the <h1> text.
print(soup.find("h1"))
#Extract the paragraph text.
print(soup.find("p"))
#Write a program to:
#Find the first <a> tag.
links = soup.find("a")
print(links)
#Print its href attribute.
print(links.get("href"))
#Use .prettify() to format parsed HTML.
print(soup.prettify())

#Scrape product details from an e-commerce sample page:
url = "http://books.toscrape.com/"
headers = {
    #user agent is making the request and from where
    "User-Agent" : "Chrome/120.0.0.0"
}
response = requests.get(url,headers = headers)
print(response.status_code)
#parse the html
soup = BeautifulSoup(response.text,features="html.parser")
print(soup) #html gets printed
#Product name
books = soup.find_all("article",class_="product_pod")

#extract all the titles and prices of books
for book in books:
    title = book.find("h3").find("a")["title"]
    print("Title:",title)
#Price
for book in books:
    price = book.find("p", class_="price_color").text
    print("Price:", price)
#Rating
for book in books:
    rating = book.find("p",class_="star-rating")
    print("Rating:",rating)
#Availability
#Extract all image URLs from a webpage.
for book in books:
    image = book.find("img",class_="thumbnail")
    print("image src:",image)



