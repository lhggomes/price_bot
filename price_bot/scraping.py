from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from pages.models import Company, Product, WebSiteDivElement, ProductMinValue
from price_bot.utils import format_html
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4503.5 Safari/537.36'

}


def create_company_and_product_dict():
    companies = {}
    company_product = {}
    all_companies = Company.objects.all()
    for company in all_companies:
        companies[company.description.lower()] = {
            f"{company.description.lower()}": company,
            f"{company.description.lower()}_div": WebSiteDivElement.objects.filter(company=company).first(),
            f"{company.description.lower()}_site": str(company.web_site),

        }
        all_products = Product.objects.all()
        for product in all_products:
            price = ProductMinValue.objects.filter(product=product,
                                                   company=company).first()
            price = price.min_value if price else ""
            company_product[company.description.lower()] = {
                f"{product.code}": product,
                f"{product.code}_price": price
            }

    return companies, company_product


def get_product():
    companies = create_company_and_product_dict()

    product = Product.objects.filter(code='1611318018').first()
    min_price = ProductMinValue.objects.filter(product=product, company=companies[0]['americanas']['americanas']).first()

    americanas_site = f"{str(companies[0]['americanas']['americanas_site'])}/produto/1611318018"

    try:
        req = Request(americanas_site, headers=HEADERS)
        response = urlopen(req)
        html = response.read()
        html = html.decode('utf-8')
        html = format_html(html)

        soup = BeautifulSoup(html, 'html.parser')

        try:
            elements = \
                soup.findAll('div', {"class": str(companies[0]['americanas']['americanas_div'].price_div)}, limit=1)[0]
            value = float(elements.text.split('R$ ')[-1].replace('.', "").replace(",", "."))
            if value < min_price.min_value:
                print('Thank you')

        except Exception as e:
            print(e.__repr__())

    except HTTPError as e:
        print(e.status, e.reason)
