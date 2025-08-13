from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

all_teams = []

html = requests.get("https://www.baseball-reference.com/leagues/majors/2024.shtml").text
soup = BeautifulSoup(html, 'lxml')
table = soup.find_all('table', class_="stats_table")[0]

links = table.find_all("a") # finds all links in the table
links = [l.get("href") for l in links] # gets href value for each link
links = [l for l in links if "/teams/" in l] # makes sure that /teams/ is in the href so we only get teams

print("Filtered for /teams/:", links)
