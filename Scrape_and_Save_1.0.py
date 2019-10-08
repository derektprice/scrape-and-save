import requests
from bs4 import BeautifulSoup
from time import sleep
import datetime


html_list = ["https://store.steampowered.com/wishlist/profiles/76561198054858793/#sort=order"]
html_list_length = len(html_list)
num_of_files = list(range(html_list_length))
num_of_files.reverse()
html_source_filename_list = []

hdr = {"User-Agent": "Derek Price",
           "From": "derek.t.price@vanderbilt.edu"}

def make_filename(website):
    d = datetime.datetime.now()
    file_name = f"{website} {num_of_files.pop()} - {d:%d-%B-%Y--%H.%M}.html"
    html_source_filename_list.append(file_name)
    return file_name

def save_html_source(websites, website_name):
    for thing in websites:
        page = requests.get(thing, headers=hdr)
        soup = BeautifulSoup(page.content, "html.parser")
        sleep(1.0)
        with open(make_filename(website_name), "wb") as file:
            file.write(soup.encode('utf-8-sig'))
            file.close()

save_html_source(html_list, "Dereks wishlist")
