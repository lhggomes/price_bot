from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from pages.models import Company, Product, WebSiteDivElement, ProductMinValue
from price_bot.utils import format_html
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4503.5 Safari/537.36'

}


def create_company_and_product_list():
    companies = [WebSiteDivElement.objects.filter(company=company).first() for company in Company.objects.all()]
    products = [product for product in Product.objects.all()]

    return companies, products


def get_product():
    companies, products = create_company_and_product_list()
    for company in companies:
        for product in products:
            min_price = ProductMinValue.objects.filter(product=product).first()
            if min_price is not None:
                web_site = f"{company.company.web_site}/produto/{product.code}"
                try:
                    req = Request(web_site, headers=HEADERS)
                    response = urlopen(req)
                    html = response.read()
                    html = html.decode('utf-8')
                    html = format_html(html)

                    soup = BeautifulSoup(html, 'html.parser')

                    try:
                        elements = \
                            soup.findAll('div', {"class": str(company.price_div)}, limit=1)[0]

                        if elements is None:
                            elements = \
                                soup.findAll('span', {"class": str(company.price_div)}, limit=1)[0]
                        value = float(elements.text.split('R$ ')[-1].replace('.', "").replace(",", "."))
                        if value < min_price.min_value:
                            print('Thank you')

                    except Exception as e:
                        print(e.__repr__())

                except HTTPError as e:
                    print(e.status, e.reason)
