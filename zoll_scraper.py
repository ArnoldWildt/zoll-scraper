from urllib import request
from bs4 import BeautifulSoup
from product import Product

MAIN_URL = "https://www.zoll-auktion.de"
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


print(len(product_list))
print(product_list[-1].print_info())
