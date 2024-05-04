from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import concurrent.futures
import random
import json



# Start a Chrome WebDriver session
driver = webdriver.Chrome()

"""
P.S:- Please provide Assembly Constituency's url from this site
url = 'https://www.ceodelhi.gov.in/AcListEng.aspx'
"""

#Function to get the all location name of a Assembly Constituency.
#Give a Assembly Constituency's url and we can get the all location name
def get_vill(url):
    
    driver.get(url)
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    village_dict = {}
    
    table = soup.find_all('div', class_='col-md-12')
    current_key = None  # Variable to track the current last element text
    
    for item in table:
        ac_vil = item.find_all('div', style='border:solid 2px #e9e9e9;')
        
        for name in ac_vil:
            sana = name.find_all('div', class_="col-md-2 box_style")[2]
            loc = name.find_all('div', class_="col-md-4 box_style")
            
            for me, location in zip(sana, loc):
                last_element_text = me.text.strip()  # Store the text of each element
                ac_loc = location.text.strip()  # Store the text of corresponding location
                
                if last_element_text != current_key:
                    if last_element_text not in village_dict:
                        village_dict[last_element_text] = []
                    current_key = last_element_text
                
                village_dict[last_element_text].append(ac_loc)  # Append location to the list under last element text key

    
    return village_dict




#Function to get the name of all location of all Assembly Constituency of delhi.
def get_ac(url):
  
    try:
        driver.get(url)
        ac_name = {}
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find_all('div',class_='col-md-4 box_style')
        if table:
            for new in table:
                ac = new.find_all('a')
                for name in ac:
                    dis_name = name.text
                    ac_name[dis_name] ={}
                    url = 'https://www.ceodelhi.gov.in/'+ name['href']
                    delay = random.uniform(1,2)
                    time.sleep(delay)
                    data = get_vill(url)
                    
                    ac_name[dis_name] = data

            with open('ac_data4.json', 'w') as json_file:
                json.dump(ac_name, json_file, indent=4)

        return ac_name
    except Exception as e:
        print(f"An error occurred: {str(e)}")




#Getting the json file of all location name in delhi
url = 'https://www.ceodelhi.gov.in/AcListEng.aspx'
print(get_ac(url))
