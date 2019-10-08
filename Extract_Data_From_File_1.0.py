from bs4 import BeautifulSoup
import soupsieve as sv
import pandas as pd

target_files = ["Top 250 Movies IMDB 0 - 07-April-2019--13.11.html"]
column1 = []
column2 = []
column3 = []
column4 = []
column5 = []
column6 = []

# give soupsieve target, name of list to output to, and soup
def get_url(sv_target, targetlist, soup):
    key_tags1 = sv.select(sv_target, soup)
    outputlist = []
    for link in key_tags1:
        targetlist.append(link.get("href"))

def get_text(sv_target, targetlist, soup):
    key_tags2 = sv.select(sv_target, soup)
    for tag2 in key_tags2:
        targetlist.append(tag2.text)

def get_all_data():
    for thing in target_files:
        openedfile = open(thing)
        soup = BeautifulSoup(openedfile, "html.parser")
        get_text("td.titleColumn > a", column1, soup)
        get_text("td.ratingColumn > strong", column2, soup)
        #additional things you want in additional columns
        openedfile.close()
    write_to_excel("test.csv", "Titles", "Ratings")

def write_to_excel(filename, col1name, col2name=None, col3name=None, col4name=None, col5name=None, col6name=None):
    df1 = pd.DataFrame({col1name: column1, col2name: column2})
    df1.to_csv(filename, mode="a", index=False, encoding="utf-8-sig")

get_all_data()
