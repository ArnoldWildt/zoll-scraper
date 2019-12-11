from urllib import request
from bs4 import BeautifulSoup
from product import Product
from emails import Email_util
from user_info import get_users

MAIN_URL = "https://www.zoll-auktion.de/"
URL = "https://www.zoll-auktion.de/auktion/auktionsuebersicht.php?seite="

overtime = False
page_counter = 1
product_list = []

while not overtime:

    content = request.urlopen(URL + str(page_counter))

    soup = BeautifulSoup(content)

    bgw_tab = soup.find_all("tr", class_="bgw_tab")
    bgg_tab = soup.find_all("tr", class_="bgg_tab")

    for _ in [*bgw_tab, *bgg_tab]:
        product_obj = Product(_)
        product_list.append(product_obj)

        if "T." in product_obj.time_till_end:
            overtime = True

    page_counter += 1

print(f"Got {len(product_list)} products.")

email_service = Email_util()

users = get_users()

for user in users:
    email_content = email_service.get_email_content(user, product_list)
    email_service.send_mail(user, email_content)
