import smtplib
import ssl
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

PORT = 465
today = date.today

msg = MIMEMultipart('alternative')
msg["Subject"] = f"HTML Link {today}"
msg["From"] = "Zoll Scraper"
msg["To"] = "##################"

text = "Python Test Email"
html_text = """\
<!DOCTYPE html>
<html>
<head>
<style>
.button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>
</head>
<body>

<h2>CSS Buttons</h2>

<button>Default Button</button>
<a href="#" class="button">Link Button</a>
<button class="button">Button</button>
<input type="button" class="button" value="Input Button">

</body>
</html>
"""

with open("credentials.txt", "r") as credits_file:
    User = credits_file.readline()
    Pass = credits_file.readline()
    print(User)
    print(Pass)

print("Test")

part1 = MIMEText(text, "plain")
part2 = MIMEText(html_text, "html")


msg.attach(part1)
msg.attach(part2)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
    server.login(User, Pass)
    server.sendmail(User, "################", msg.as_string())

    print(f"Sent EMail to ##################")


class Email_util:
    def __init__(self):

        with open("html_top.html", "r") as reader:
            self.html_top = reader.read()

        self.html_end = "</body></html>"
        self.context = ssl.create_default_context()

    def send_mail(self, receiver, product_list):
        with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=self.context) as server:
            server.login(User, Pass)
            server.sendmail(User, receiver, message)

            print(f"Sent EMail to {receiver}")


# a = Email_util()
# a.send_mail(REC, 1)
