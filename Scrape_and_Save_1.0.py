import requests
from bs4 import BeautifulSoup
from time import sleep
import datetime

#this block creates a list of the urls you want to scrape, and counts how long that list is
html_list = ["INSERT_URLS_HERE"]
html_list_length = len(html_list)
num_of_files = list(range(html_list_length))
num_of_files.reverse()
html_source_filename_list = []

#defining headers for polite scraping
hdr = {"User-Agent": "NAME",
           "From": "EMAIL_ADDRESS"}

#creates a file name for each element in your url list
def make_filename(website):
    d = datetime.datetime.now()
    file_name = f"{website} {num_of_files.pop()} - {d:%d-%B-%Y--%H.%M}.html"
    html_source_filename_list.append(file_name)
    return file_name

#this actually requests the pages and runs the make_filename function
def save_html_source(websites, website_name):
    for thing in websites:
        page = requests.get(thing, headers=hdr)
        soup = BeautifulSoup(page.content, "html.parser")
        sleep(1.0)
        with open(make_filename(website_name), "wb") as file:
            file.write(soup.encode('utf-8-sig'))
            file.close()
                      
#this is where the program actually runs, all from just one function. You must add a "stem" to save_html_source - all locally saved html files will start with this "stem," so you can keep your scrapes organized
save_html_source(html_list, "HTML_FILENAME_STEM")
