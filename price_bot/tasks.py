from .scraping import get_product
from celery import shared_task


@shared_task
def get_product_price():
    get_product()
    print('Hellow')
