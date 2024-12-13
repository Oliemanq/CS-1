import requests
from bs4 import BeautifulSoup
import csv

# Define the URL
url = "https://www.learningames.net/gallery.htm"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Open a CSV file to save the data
    with open('learningames_titles.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Game Title"])

        # Locate all game entries in the gallery
        for game_table in soup.find_all('table', class_='gallery-table'):
            title_element = game_table.find('span', class_='colortitle')

            if title_element:
                title = title_element.get_text(strip=True)
                writer.writerow([title])

    print("Data successfully saved to learningames_titles.csv")
else:
    print("Failed to retrieve the webpage.")
