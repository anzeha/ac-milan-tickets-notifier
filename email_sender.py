import requests


import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()


def send_ticket_email(to, match, url):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxcd574be0daee4690a4f2e22c4f1fed8c.mailgun.org/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={
            "from": f"Ac Milan ticket bot <{os.getenv('MAILGUN_DOMAIN')}>",
            "to": [to],
            "subject": f"Tickets for {match}",
            "html": f"<html><body><p>Tickets for match {match} just became available! Click <a href='{url}'>here</a> to get them.</p></body></html>",
        },
    )
