import smtplib
import ssl
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from user_info import get_users

PORT = 465
today = date.today()

with open("credentials.txt", "r") as credits_file:
    User = credits_file.readline()
    Pass = credits_file.readline()
    print(User)
    print(Pass)

class Email_util:
    def __init__(self):

        with open("html/html_top.html", "r") as reader:
            self.html_top = reader.read()

        with open("html/content.html", "r") as reader:
            self.html_content = reader.read()

        self.html_end = "</body></html>"
        self.context = ssl.create_default_context()

    def send_mail(self, receiver, product_list):
        msg = MIMEMultipart('alternative')
        msg["Subject"] = f"Zoll Scraper links - {today}"
        msg["From"] = "Zoll Scraper"
        msg["To"] = receiver.email

        text_msg = f"Hallo {receiver.name},"

        msg.attach(MIMEText(text_msg, "plain"))
        msg.attach(MIMEText(self.html_top, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=self.context) as server:
            server.login(User, Pass)
            server.sendmail(User, receiver, msg)

            print(f"Sent EMail to {receiver}")


a = Email_util()
print(a.html_content)
