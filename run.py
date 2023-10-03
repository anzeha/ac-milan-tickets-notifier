from bs4 import BeautifulSoup
import json
import requests
import time
import random
from email_sender import send_ticket_email
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format it as a string
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Print the timestamp
print(timestamp)


with open("ticket_avaliable.json", "r") as file:
    ticket_avaliable = json.load(file)
    new_ticket_avaliable = ticket_avaliable.copy()

game_urls = []
with open("urls.txt", "r") as file:
    for line in file:
        game_urls.append(line.strip())

emails = []
with open("emails.txt", "r") as file:
    for line in file:
        emails.append(line.strip())


for game_url in game_urls:
    response = requests.get(game_url, timeout=random.randint(1, 4))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        html_content = response.content  # This contains the HTML content
        # Now you can save this content to a file or process it further
    else:
        print(f"fail for {game_url}")
        continue

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the div with the attribute 'seo-type' equal to 'matches_cta_singletickets'
    el_with_attribute = soup.find_all(attrs={"seo-label": "Buy ticket"})

    if len(el_with_attribute) > 0:
        el_with_attribute = el_with_attribute[0]
        el_text = el_with_attribute.text

        # Get the value of the 'seo-match' attribute
        seo_match_value = el_with_attribute.get("seo-match")
        # print(seo_match_value)

        # print(el_text)

        if "buy" in str(el_text).lower():
            print(f"{seo_match_value} Can be bought")
            new_ticket_avaliable[seo_match_value] = True
        else:
            print(f"{seo_match_value} Cant be bought")
            new_ticket_avaliable[seo_match_value] = False

        # Change in sales detected:
        if (
            new_ticket_avaliable[seo_match_value] == True
            and ticket_avaliable[seo_match_value] == False
        ):
            print(f"Ticket for {seo_match_value} can now be bought")
            for email in emails:
                send_ticket_email(email, seo_match_value, game_url)

    time.sleep(3)


# Write the dictionary to a JSON file
with open("ticket_avaliable.json", "w") as file:
    json.dump(new_ticket_avaliable, file)
