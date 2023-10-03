# AC Milan Ticket Availability Checker 🔴⚫🎫

This Python script periodically checks for the availability of tickets for AC Milan football matches. When tickets become available, it sends a notification via email. This tool is designed to be run as a cron job, providing a convenient way to stay updated on ticket availability for your favorite team.

> **Note:** This script relies on parsing HTML of a website. If the AC Milan ticket website somehow changes, this script will not work anymore and will need modification.

## Key Features

-   **Automated Ticket Checks:** Regularly monitors ticket availability for AC Milan matches.
-   **Email Notifications:** Notifies you via email as soon as tickets are available.
-   **Customizable Scheduling:** Easily configure the frequency of ticket checks to suit your preferences.

## Usage Instructions

1. Clone the repository to your local machine.
2. Set up your Mailgun API credentials and configure the email sender and recipient details.
3. Schedule the script to run periodically using a cron job.
4. Receive timely notifications about AC Milan ticket availability.

Feel the excitement of securing your tickets and supporting AC Milan!

## Getting Started

### Prerequisites

-   Python 3.x
-   [Mailgun](https://www.mailgun.com/) API Key and Domain

### Setup

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/ac-milan-ticket-checker.git
```

2. Install requirments

```
pip install -r requirements.txt
```

3. Create a `.env` file in the root with the following two variables obtained from the Mailgun dashboard:

```
MAILGUN_API_KEY=...
MAILGUN_DOMAIN=...
```

4. Edit the `urls.txt` file to include urls of the match/matches you want to be notified about. Some example of urls are already listed in the provided `urls.txt`. List of matches and urls can be found [here](https://singletickets.acmilan.com/en/) (click `BUY NOW` for a selected match and copy url from the address bar into `urls.txt`).

5. Add email address/addresses for which the ticket notifications will be sent to in `emails.txt` file.

6. Run `init.py` file. This will create a `ticket_avaliable.json` file in your root directory that will include the initial ticket states of the selected matches.

7. Run `run.py`

### Scheduling with Cron

Ideally, the `run.py` script in step 7 should be run periodically using a scheduler like cron on a server or a remote VPS. This way, the script checks the availability of tickets periodically and sends a notification as soon as the change in ticket availability is detected.

Here is an example of a cron job that runs the script every 10 minutes and also outputs stdout and stderr to a log file called `ticket_log.txt`:

```bash
*/10 * * * * /usr/bin/python3 /path/to/ac-milan-ticket-checker/run.py >> /path/to/ac-milan-ticket-checker/ticket_log.txt 2>&1
```
