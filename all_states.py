from bs4 import BeautifulSoup
import requests
import time
import concurrent.futures
import random
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json



# Start a Chrome WebDriver session
driver = webdriver.Chrome()

"""
P.S:- This is maine url of website. provide all url from this website
url = 'https://vlist.in/'
"""



#Function to get the Name of all villages from tehsil url
def get_village(url):
    village_list = {}
    driver.get(url)
    delay = random.uniform(2, 3)
    time.sleep(delay)
    
    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('tbody')
    
    if table:
        rows = table.find_all('tr')
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:
                village_name = cols[1].text.strip()
                village_code = cols[2].text.strip()
                village_list[village_name] = village_code
    
    return village_list



#Function to get the name of all tehsil from district url;
def get_tehsil(url):
  tehsil_list = {}
  driver.get(url)
  # Get the page source after it's loaded
  page_source = driver.page_source

  # Parse the page source with BeautifulSoup
  soup = BeautifulSoup(page_source, 'html.parser')
  table = soup.find_all('tbody')
  for tehsils in table:
    tehsil = tehsils.find_all('a')
    # delay = random.uniform(2, 5)
    # time.sleep(delay)
    for all_tehsil in tehsil:
      tehsil_name = all_tehsil.text
      tehsil_list[tehsil_name] = {}
      villages_url = 'https://vlist.in' + all_tehsil['href']
      delay = random.uniform(2, 4)
      time.sleep(delay)
      villages = get_village(villages_url)
      tehsil_list[tehsil_name] = villages
  return tehsil_list


#Function to get the name of all district of a state
def get_district(url):
  distict_list = {}
  driver.get(url)
  delay = random.uniform(2,4)
  time.sleep(delay)

  page_source = driver.page_source
  soup = BeautifulSoup(page_source, 'html.parser')
  table = soup.find_all('tbody')
  for disticts in table:
    state = disticts.find_all('a')
    for all_distict in state:
    #   delay = random.uniform(4, 8)
    #   time.sleep(delay)
      distict_name = all_distict.text
      distict_list[distict_name] = {}
      tehsil_url = 'https://vlist.in' + all_distict['href']
      delay = random.uniform(3, 6)
      time.sleep(delay)
      distict = get_tehsil(tehsil_url)
      distict_list[distict_name] = distict

  
  return distict_list


#function to get the all district, tehsil, and village name from state;
# By the help of this function we can get the data of all states and their district, tehsil, villages respectively in one go.

def get_state(url):
    states_list = {}
    
    driver = webdriver.Chrome()
    try:
        # Load the URL
        driver.get(url)
        
        # Delay to ensure the page is fully loaded
        delay = random.uniform(8, 10)
        time.sleep(delay)

        # Get the page source after it's loaded
        page_source = driver.page_source
        
        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # Find all 'tbody' elements (assuming states are in a table)
        table = soup.find_all('tbody')
        
        # Iterate over each 'tbody' element to extract state information
        for states in table:
            state_links = states.find_all('a')
            for state_link in state_links:
                state_name = state_link.text.strip()
                states_list[state_name] = {}
                
                # Construct the URL for the district data
                district_url = 'https://vlist.in' + state_link['href']
                
                # Get district data (assuming get_district function is defined)
                district_data = get_district(district_url)
                
                # Add district data to states_list for the current state
                states_list[state_name] = district_data
                
                # Delay before processing the next state (to be polite)
                delay = random.uniform(5, 10)
                time.sleep(delay)
        
        # Save the states_list dictionary to a JSON file
        with open('all_states_data.json', 'w') as json_file:
            json.dump(states_list, json_file, indent=4)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Always quit the driver to clean up resources
        driver.quit()

    return states_list



#Function to get the name of all district, tehsil and village name of a one specific state.
def get_one_state(url):
    try:
        with open('states_data.json', 'r') as json_file:
            states_list = json.load(json_file)
    except FileNotFoundError:
        states_list = {}

    driver = webdriver.Chrome()
    try:
        driver.get(url)
        delay = random.uniform(2, 4)
        time.sleep(delay)

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find_all('tbody')

        # Check if table is found and extract the first state URL
        if table:
            for new in table:
                state = new.find_all('tr')
                for i in range(5, min(8, len(state))):
                    state_row = state[i]

                # if len(state) > 1:  # Ensure there's enough data to extract
                    first_state = state_row.find('a')  # Get the first state link
                    if first_state:
                        state_name = first_state.text
                        states_list[state_name] = {}
                        district_url = 'https://vlist.in' + first_state['href']
                        district_data = get_district(district_url)
                        delay = random.uniform(3,5)
                        time.sleep(delay)
                        states_list[state_name] = district_data

            # Save the states_list dictionary to a JSON file
            with open('states_data.json', 'w') as json_file:
                json.dump(states_list, json_file, indent=4)

    finally:
        driver.quit()  # Make sure to quit the driver after use

    return states_list


url = 'https://vlist.in/'
print(get_one_state(url))