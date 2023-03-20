##ADDITIONAL METHOD TO DOWNLOAD THE DATA(FEBRUARY 2022 NOT WORKS)

import requests
import time
from calendar import monthrange

OUTPUT_FOLDER = "/Users/bober/Desktop/study/naukma/prog_new/hw2/isw"
BASE_URL = "https://www.understandingwar.org/backgrounder/russian-offensive-campaign-assessment-"

def save_page(url, file_name):
    page = requests.get(url)
    
    url_name = url.split("/")[-1].replace("-","_")
    with open(f"{OUTPUT_FOLDER}/{file_name}__{url_name}.html",'wb+') as f:
        f.write(page.content)

mnths = ["Feb", "Mar", "Apr", "May", "June", "July", "August", "Sept", "Oct"]

# ## All 2022 working

YEAR = 2022
mon_ind = 1
mnths = ["march","april","may","june","july","august","september","october","november","december"]
BASE_URL = "https://www.understandingwar.org/backgrounder/russian-offensive-campaign-assessment"
for m in mnths:
    fisrt_day = 1
    day_count = monthrange(YEAR, mon_ind)


    for d in range(fisrt_day, day_count[1]+1):
        if d<=9:
            sd = "0"+str(d)
        else:
            sd = str(d)

        
        file_name = f"{d}_{mon_ind}_{YEAR}"
        url = f"{BASE_URL}-{m}-{d}"
        
        print(url)
        #save_page(url, file_name) 
        time.sleep(0.1)
    
    mon_ind += 1
    


# ### 2023


YEAR = 2023
mon_ind = 1
mnths = ["january"]
BASE_URL = "https://www.understandingwar.org/backgrounder/russian-offensive-campaign-assessment"
for m in mnths:
    fisrt_day = 1
    day_count = monthrange(YEAR, mon_ind)


    for d in range(fisrt_day, day_count[1]+1):
        
        sd = str(d)

        
        file_name = f"{d}_{mon_ind}_{YEAR}"
        url = f"{BASE_URL}-{m}-{d}-{YEAR}"
        
        print(url)
        #save_page(url, file_name) 
        time.sleep(1)
    
    mon_ind += 1
    





