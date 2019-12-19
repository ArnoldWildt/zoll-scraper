from zoll_scraper import scrap_zoll
import schedule
import time
import sys


def execute_service():
    try:
        scrap_zoll()
    except:
        print("Unexpected error:", sys.exc_info()[0])


schedule.every().day.at("06:00").do(execute_service)
schedule.every().day.at("11:45").do(execute_service)
schedule.every().day.at("19:00").do(execute_service)


if __name__ == "__main__":
    while True:
        time.sleep(60)
        schedule.run_pending()
