import requests
from bs4 import BeautifulSoup
import pandas

url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

products = []
prices = []
ratings = []

# bhgxx2
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
	name=a.find('div', attrs={'class':'_3wU53n'})
	price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
	products.append(name.text)
	prices.append(price.text)

df = pandas.DataFrame({'Name': products, 'Price': prices})
df.to_csv("data.csv", index=False)
print("Done!")