from bs4 import BeautifulSoup

MAIN_URL = "https://www.zoll-auktion.de/"


class Product:
    def __init__(self, soup_tab):
        self.soup_tab = soup_tab

        # Get the secound a of the full tab
        a_tag = soup_tab.find_all("a")[1]
        self.name = a_tag.get("title")
        self.href = a_tag.get("href")

        self.pic_link = soup_tab.find("img")["src"]

        # Get all li tag of the full tab
        li_tags = soup_tab.find_all("li")
        self.shipping = "versand" in li_tags[0].text.lower()
        price_till = li_tags[1].text.index("\xa0")
        self.price = li_tags[1].text.lower()[:price_till]
        self.bids = li_tags[2].text
        self.time_till_end = li_tags[3].text
        self.end_date = li_tags[4].text

        location_list = soup_tab.find("td", class_="artikelstandort").find_all("div")
        self.location = " ".join([_.text for _ in location_list])

        self.icon = "❌"

        if self.shipping:
            self.icon = "✔"

        self.dict = {
            "$href": MAIN_URL + self.href,
            "$picture": MAIN_URL + "auktion/" + self.pic_link,
            "$name": self.name,
            "$plz": self.location.split(" ")[0],
            "$location": " ".join(self.location.split(" ")[1:]),
            "$price": self.price,
            "$bids": self.bids,
            "$end_time": self.end_date,
            "$icon": self.icon,
            "$link": "https://www.google.com/search?q=" + self.name.replace(" ", "+"),
        }

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Href: {self.href}")
        print(f"Pic link: {self.pic_link}")
        print(f"Shipping: {self.shipping}")
        print(f"Price: {self.price}")
        print(f"Bids: {self.bids}")
        print(f"Time till end: {self.time_till_end}")
        print(f"End date: {self.end_date}")
        print(f"Location: {self.location}")
