import requests 
import json 
import smtplib 
import logging 

URL = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit" 

with open('creds.json', 'r') as f: 
    creds = json.load(f) 
    f.close() 

LOGFILE = 'email_send.log' 
EMAIL = creds['email'] 
PASSWORD = creds['password'] 
RECIPIENT = EMAIL 

logging.basicConfig(filemode='a', filename=LOGFILE, level=logging.INFO, format='%(levelname)s - %(asctime)s - %(message)s') 

def send_email(joke): 

    try: 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
    except smtplib.SMTPConnectError: 
        logging.error("Could not connect to the mail server.") 
        exit() 

    try: 
        s.login(EMAIL, PASSWORD) 
    except smtplib.SMTPAuthenticationError: 
        logging.error("Auth failure") 
        exit() 

    try:    
        s.sendmail(EMAIL, RECIPIENT, f'\n{joke}') 
    except smtplib.SMTPException: 
        logging.error("Unable to send email due to error.") 
        exit() 

    s.quit() 


def get_joke_content(): 
    response = requests.get(URL) 

    result = response.json() 

    if result['error']: 
        logging.error("Something went wrong with the API request.") 
        return None 

    if result['type'] == 'twopart': 
        setup = result['setup'] 
        delivery = result['delivery'] 
        return f"Setup: {setup}\nDelivery: {delivery}" 
    else: 
        joke = result['joke'] 
        return f"Joke: {joke}" 


joke = get_joke_content() 

logging.info("Joke retrieved successfully.") 

if joke is not None: 
    send_email(joke) 
    logging.info('Email successfully sent.')