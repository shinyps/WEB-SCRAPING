#!/usr/bin/env python
# coding: utf-8

# # link - https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=71f33b8b-2d89-451d-9d5c-6cebf503fbee

# In[1]:


import bs4
from bs4 import BeautifulSoup as bs
import requests


# In[2]:


link='https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=71f33b8b-2d89-451d-9d5c-6cebf503fbee'


# In[3]:


page = requests.get(link)


# In[4]:


page.content


# In[5]:


soup = bs(page.content, 'html.parser')
#it gives us the visual representation of data
print(soup.prettify())


# In[6]:


name=soup.find('div',class_="_4rR01T")
print(name)


# In[7]:


# to get just the name we will use the below code
name.text


# In[24]:


#get rating of a product
rating=soup.find('div',class_="gUuXy-")
print(rating)
rating.text


# In[9]:


#get other details and specifications of the product
specification=soup.find('div',class_="fMghEO")
print(specification)
specification.text


# In[10]:


for each in specification:
    spec=each.find_all('li',class_='rgWa7D')
    print(spec[0].text)
    print(spec[1].text)
    print(spec[2].text)
    print(spec[3].text)
    print(spec[4].text)
    print(spec[5].text)
    


# In[11]:


#get price of the product
price=soup.find('div',class_="_3tbKJL")
print(price)
price.text


# In[30]:


type(rating)


# In[12]:


products=[]              #List to store the name of the product
prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product
apps = []                #List to store supported apps                
os = []                  #List to store operating system
hd = []                  #List to store resolution
sound = []               #List to store sound output


# In[17]:


for data in soup.findAll('div',class_='_3pLy-c row'):
        names=data.find('div', attrs={'class':'_4rR01T'})
        price=data.find('div', attrs={'class':'_25b18c'})
        rating=data.find('div', attrs={'class':'gUuXy-'})
        specification = data.find('div', attrs={'class':'fMghEO'})
        
        for each in specification:
            col=each.find_all('li', attrs={'class':'rgWa7D'})
            app =col[0].text
            os_ = col[1].text
            hd_ = col[2].text
            sound_ = col[3].text
            
            products.append(names.text) # Add product name to list
            prices.append(price.text) # Add price to list
            apps.append(app)# Add supported apps specifications to list
            os.append(os_) # Add operating system specifications to list
            hd.append(hd_) # Add resolution specifications to list
            sound.append(sound_) # Add sound specifications to list
            ratings.append(rating.text)   #Add rating specifications to list


# In[18]:


#printing the length of list
print(len(products))
print(len(ratings))
print(len(prices))
print(len(apps))
print(len(sound))
print(len(os))
print(len(hd))


# In[31]:


import numpy as np


# In[34]:


ratings.append(np.nan)


# In[35]:


print(len(ratings))


# In[36]:


import pandas as pd
df=pd.DataFrame({'Product Name':products,'Supported_apps':apps,'sound_system':sound,'OS':os,"Resolution":hd,'Price':prices,'Rating':ratings})
df.head(10)


# In[37]:


df.to_csv("Web Scrapping-shiny Flipkart Extraction.csv", index=True)


# In[ ]:




