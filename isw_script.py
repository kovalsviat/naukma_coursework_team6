import requests
import time
import datetime

OUTPUT_FOLDER = "/Users/bober/Desktop/study/naukma/hw2/isw"
BASA_URL = "https://understandingwar.org/backgrounder/russian-offensive-campaign-assessment"

def save_page(url, file_name):
    page = requests.get(url)
    
    url_name = url.split("/")[-1].replace("-","_")
    with open(f"{OUTPUT_FOLDER}/{file_name}__{url_name}.html",'wb+') as f:
        f.write(page.content)

def get_prev_date(what):
    mnths = ["january", "february", "march", "april", "may", "june", "july", "august","september", "october", "november", "december"]
    base = datetime.datetime.today() - datetime.timedelta(days=1)
    if what == "m":
        return mnths[int(base.strftime("%m"))-1]
    elif what == "d":
        return base.strftime("%d")
    elif what == "year":
        return base.strftime("%Y")

#month = "March"
#d = 13 
#year = 2023

month = get_prev_date("m")
d = get_prev_date("d")
year = get_prev_date("year")
url = f"{BASA_URL}-{month}-{d}-{year}"
file_name = f"{month}_{d}_{year}"

save_page(url,file_name)

