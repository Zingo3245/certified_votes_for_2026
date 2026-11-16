import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time

def main():

    # Read in counties
    geo_counties = pd.read_excel('certified_vote.xlsx', header=1)

    # initialize whatever driver you are using
    driver = webdriver.Chrome()

    for county in geo_counties.Counties:
        # Goes through each county for county-level results
        print(county)
        excel_link = f'https://results.sos.ga.gov/results/public/{county}-county-ga/elections/11032026GeneralAndSpecialElection/reports'
        # get the link
        driver.get(excel_link)
        time.sleep(2)
        #download the link
        # Find all <a> elements on the page
        link_elements = driver.find_elements(By.TAG_NAME, "a")
        urls = [
            link.get_attribute("href")
            for link in link_elements
            if link.get_attribute("href")
        ]
        for url in urls:
            if url.endswith('.xlsx'):
                driver.get(url)
                time.sleep(5)


if __name__ == "__main__":
    main()