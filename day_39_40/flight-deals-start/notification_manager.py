from twilio.rest import Client
from dotenv import load_dotenv
import os 
import smtplib

class NotificationManager:
    def __init__(self, emails):
        load_dotenv()
        self.password = os.getenv("EMAIL_PASSWORD")
        self.emails = emails
        self.my_email = "exaltmokonogho@gmail.com"
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as self.connection:
            self.connection.login("exaltmokonogho@gmail.com", self.password)

        self.client = Client(os.getenv("ACC_SID"), os.getenv("AUTH_TOKEN"))
    def send_emails(self, messages):
        for mail in self.emails:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as self.connection:
                self.connection.login("exaltmokonogho@gmail.com", self.password)
                self.connection.sendmail(from_addr= "exaltmokonogho@gmail.com", 
                            to_addrs= mail, 
                            msg= f" Subject: Cheap Flight Today\n\n{messages}")
    

    #This class is responsible for sending notifications with the deal flight details.
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:+2348136552264'
        )
        print(message.sid)