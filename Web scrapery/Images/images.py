#Basic image web scraper made with Python and BeautifulSoup library

from pip._vendor import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import json
import os

print("Whenever you want to stop, write 'nothing'.")


def start_search():

    print("\n")

    url = "https://www.bing.com/images/search"
    search = input("Search image of ")
    params = { "q": search }
    #Must have below line
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    
    #Naming directory with user's search topic
    directory_name = search.replace(" ", "_").lower()

    #If user writes 'nothing', code stops
    if(search == 'nothing'):
        print("Bye!")
        exit(0)
    
    #If there isn't a directory with user's search topic, create one
    if(not os.path.isdir(directory_name)):
        os.makedirs(directory_name)
    
    res = requests.get(url, params = params, headers = headers)

    soup = BeautifulSoup(res.text, "html.parser")
    # print(soup.prettify())

    links = soup.findAll("a", { "class": "iusc"} )
    print("Results:", len(links))

    user_choice = input("How many of them do you want? ")

    #If user writes a number equal or below '0', code starts again
    if(int(user_choice) <= 0):
        print("Ok, no images for you then...")
        start_search()

    print("Ok! Your images are going to be saved on the following folder: " + directory_name)

    #If user writes a number higher than the avaiable results, code starts again without saving anything
    if(int(user_choice) > len(links)):
        print("There aren't so many images avaiable. Please, try again.")
        start_search()
        # exit(0)

    #Removes the amount of images that the user doesn't want from the array 'links'
    for i in range(len(links) - int(user_choice)):
        links.pop()
    
    for link in links:

        image = json.loads(link.attrs['m'])
        image_url = image['murl']
        title = image_url.split('/')[-1]

        image_res = requests.get(url = image_url, headers = headers)

        image_object = Image.open(BytesIO(image_res.content))
        image_object.save("./" + directory_name + "/" + title, image_object.format.lower())
        
        print("Image:", image_url)

    #Main loop
    start_search()

#Start code
start_search()