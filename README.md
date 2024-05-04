# Data Collection Project

States project involves scraping data from 'https://vlist.in/' to gather information about villages, tehsils, districts, and states in India.

## Requirements

- Python (version 3.x)
- Selenium WebDriver
- BeautifulSoup
- Chrome WebDriver (or WebDriver compatible with your browser)

Install the required libraries using pip:

```bash
pip install selenium beautifulsoup4
```

Make sure you have Chrome WebDriver installed and added to your system PATH.

## Usage

1. Clone this repository:

```bash
git clone <repository_url>
```

2. Navigate to the project directory:

```bash
cd <project_directory>
```

3. Update the `url` variable in the script with the desired URL:

```python
url = 'https://vlist.in/'
```

4. Run the script to scrape the data:

```bash
python all_states.py
```

The script will extract information about states, districts, tehsils, and villages from the provided URL and store the data in JSON format.

## Project Structure

- `all_states.py`: Contains the main scraping functions (`get_state`, `get_one_state`, `get_district`, `get_tehsil`, `get_village`).
- `states_data.json`: Output JSON file containing data for some states only. You can run the code and can get all states data.
- `delhi.json`: Output JSON file containing data for a specific state.

## Note

- The scraping process may take some time due to delays introduced between requests (`time.sleep(delay)`).
- Ensure you comply with the website's terms of service and use responsible scraping practices.

---


# Delhi Assembly Constituency Location Data Scraper

This project involves scraping data from the Delhi Election Commision website to gather information about the locations within each Assembly Constituency (AC).

## Requirements

- Python (version 3.x)
- Selenium WebDriver
- BeautifulSoup
- Chrome WebDriver (or WebDriver compatible with your browser)

Install the required libraries using pip:

```bash
pip install selenium beautifulsoup4
```

Make sure you have Chrome WebDriver installed and added to your system PATH.

## Usage

1. Clone this repository:

```bash
git clone <repository_url>
```

2. Navigate to the project directory:

```bash
cd <project_directory>
```

3. Update the `url` variable in the script (`scraper.py`) with the desired URL:

```python
url_ac = 'https://www.ceodelhi.gov.in/AcListEng.aspx'
```

4. Run the script to scrape the data:

```bash
python delhi_name.py
```

The script will extract information about locations within each Assembly Constituency (AC) in Delhi from the provided URL and store the data in a JSON file (`ac_data4.json`).

## Project Structure

- `delhi_name.py`: Contains the main scraping functions (`get_vill`, `get_ac`) for extracting AC location data.
- `ac_data4.json`: Output JSON file containing Assembly Constituency location data.

## Note

- The scraping process may take some time due to delays introduced between requests (`time.sleep(delay)`).
- Ensure you comply with the website's terms of service and use responsible scraping practices.
