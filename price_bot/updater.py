from apscheduler.schedulers.background import BackgroundScheduler
from .scraping import get_product


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_product, 'interval', seconds=180)
    scheduler.start()
