from zoll_scraper import scrap_zoll
from timeloop import Timeloop
from datetime import timedelta
import sys

tl = Timeloop()


@tl.job(interval=timedelta(hours=12))
def execute_service():
    try:
        scrap_zoll()
    except:
        print("Unexpected error:", sys.exc_info()[0])


if __name__ == "__main__":
    tl.start(block=True)
