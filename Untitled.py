#!/usr/bin/env python
# coding: utf-8

# In[12]:


import requests
import time
from calendar import monthrange


# In[13]:


OUTPUT_FOLDER = "/Users/bober/Desktop/study/naukma/prog_new/hw2/isw"
BASE_URL = "https://www.understandingwar.org/backgrounder/russian-offensive-campaign-assessment-"


# In[14]:


def save_page(url, file_name):
    page = requests.get(url)
    
    url_name = url.split("/")[-1].replace("-","_")
    with open(f"{OUTPUT_FOLDER}/{file_name}__{url_name}.html",'wb+') as f:
        f.write(page.content)


# In[15]:


mnths = ["Feb", "Mar", "Apr", "May", "June", "July", "August", "Sept", "Oct"]


# ### 2022 FEB-OCT
# ## not working

# In[16]:


YEAR = 2022
mon_ind = 2
for m in mnths:
    fisrt_day = 1
    day_count = monthrange(YEAR, mon_ind)

    if m == "Feb":
        fisrt_day=25
        
    for d in range(fisrt_day, day_count [1]+1):
        if m == "Oct" and d>19:
            continue
        date = f"{m}{d}"
        file_name = f"{d}_{mon_ind}_{YEAR}"
        url = f"{BASE_URL}{date}"
        print(date)
        print(url)
        save_page(url, file_name) 
        time.sleep(1)
        


# ### 2022 October-December
# ## not working

# In[ ]:


#YEAR = 2022
#mon_ind = 10
#mnths = ["Oct", "Now", "Dec"]
for n in mnths:
    fisrt_day = 1
    day_count = monthrange(YEAR, mon_ind)


    if m == "Oct":
        fisrt_day=21
    for d in range(fisrt_day, day_count[1]+1):
        if d<=9:
            sd = "0"+str(d)
        else:
            sd = str(d)
        date = f"{mon_ind}{sd}22"
        
        file_name = f"{d}_{mon_ind}_{YEAR}"
        url = f"{BASE_URL}{date}"
        
        print(date)
        print(url)
        save_page(url, file_name) 
        time.sleep(1)
        
    mon_ind += 1


# ## All 2022 working

# In[30]:


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
        time.sleep(0.00001)
    
    mon_ind += 1
    


# ### 2023

# In[25]:


YEAR = 2023
mon_ind = 1
mnths = ["january"]
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
        url = f"{BASE_URL}-{m}-{d}-{YEAR}"
        
        print(url)
        save_page(url, file_name) 
        time.sleep(1)
    
    mon_ind += 1
    


# In[ ]:




