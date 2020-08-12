import smtplib
import ssl
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from user_info import get_users
import re

PORT = 465

with open("credentials.txt", "r") as credits_file:
    User = credits_file.readline()
    Pass = credits_file.readline()
    print(User[:-1])
    print(Pass)


def find_replace_multi(string, dictionary):
    for key, val in dictionary.items():
        string = string.replace(key, val)
    return string


class Email_util:
    def __init__(self):
        with open("html/html_top.html", "r") as reader:
            self.html_top = reader.read()

        with open("html/content.html", "r") as reader:
            self.html_content = reader.read()

        self.html_end = "</table></body></html>"
        self.context = ssl.create_default_context()

    def get_email_content(self, receiver, product_list):
        today = date.today()
        msg = MIMEMultipart('alternative')
        msg["Subject"] = f"Zoll Scraper links {today}"
        msg["From"] = "Zoll Scraper"
        msg["To"] = receiver.email

        text_msg = f"Hallo {receiver.name},"
        msg.attach(MIMEText(text_msg, "plain"))

        html_email_content = self.html_top

        for product in product_list:
            product_cont = find_replace_multi(self.html_content, product.dict)
            html_email_content += product_cont

        html_email_content += self.html_end
        msg.attach(MIMEText(html_email_content, "html"))

        return msg

    def send_mail(self, receiver, msg):
        with smtplib.SMTP_SSL("smtp.gmail.com", PORT,
                              context=self.context) as server:
            server.login(User, Pass)
            server.sendmail(User, receiver.email, msg.as_string())

            print(f"Sent EMail to {receiver.email}")
