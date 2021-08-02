# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from weather import weather_func
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
         return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         day = tracker.current_state()['latest_message']['text']

         print(day)

         temp_value = weather_func(day)['temperature']

         print(temp_value)

         #dispatcher.utter_message("Temperature is {}".format(temp_value))

         dispatcher.utter_template("utter_weather",tracker,temp=temp_value)

         return []

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict",) -> List[Dict[Text, Any]]:
    
        SendEmail(
            tracker.get_slot("email"),
            tracker.get_slot("subject"),
            tracker.get_slot("message")
        )
        dispatcher.utter_message("Thanks for providing details. We have sent you a mail at {}".format(tracker.get_slot("email")))
        return []

def SendEmail(toaddr, subject, message):
    fromaddr = "ketan.mittal007@gmail.com"

    msg = EmailMessage()

    msg.set_content(message)

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = subject

    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()

    #Start tls for security
    s.starttls()

    #Authentication
    try:
        s.login(fromaddr,"ketmit25111999")

        #convert multipart message to string
        s.send_message(msg)

        print("Email sent")

    except:
        print("Error occured while sending email")

    finally:
        s.quit()
