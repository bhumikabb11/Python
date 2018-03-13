from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://www.alzerina.com/collections/petite-necklace'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


#html parsing- python calling

page_soup = soup(page_html,"html.parser")
page_soup.h1 #it will show you the header of the page source


page_soup.body.span

container = page_soup.findAll("div",{"class":"product span3 adaptive-grid"}) #after inspecting and taking only 1 div of the item
print(len(container)) # out-put :16 because the above page contains 16 items
contain = container[0] #will show you the 1st item's html code

scrapped = "alzi_product.csv"
f = open(scrapped,"w")
header = "name,price\n"

f.write(header)

for contain in container:
	name = contain.h4.text
	price = contain.span.text
	price = price.strip()
	f.write(name + "," + price + "\n")

f.close()
