from apscheduler.schedulers.background import BackgroundScheduler
from .scraping import get_product


# 3 hours to check
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_product, 'interval', seconds=10800)
    scheduler.start()
