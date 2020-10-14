#Basic web scrap that will return the title, link and summary of your search!

from bs4 import BeautifulSoup
from pip._vendor import requests

search = input("What would you like to search? ")
params = { "q": search }
#Must have below line
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

res = requests.get("http://www.bing.com/search", params = params, headers = headers )

print("\n")

soup = BeautifulSoup(res.text, "html.parser")
# print(soup.prettify())

#Finds all 'ol' HTML elements with id equal to 'b_results'
results = soup.find("ol", { "id": "b_results" })

#Finds all 'li' HTML elements with class equal to 'b_algo' inside the ones found above
links = results.findAll("li", { "class": "b_algo" })

# print(results)
# print(links)

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"] # <--- attrs is short for attributes

    #The line below is commented because some searchs don't have summary
    # item_sum = item.find("a").parent.parent.find("p").text

    if(item_text and item_href):
        print("Title: " + item_text)
        print("Link: " + item_href)
        # print("Summary: " + item_sum)
        print("\n===================================================================\n")