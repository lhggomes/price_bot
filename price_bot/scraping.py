from django.core.mail import send_mail
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from pages.models import Company, Product, WebSiteDivElement, ProductMinValue, ProductPriceHistory
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
    print(f'Inicio Processamento de Captura de ')
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
                            soup.findAll('div', {"class": str(company.price_div)}, limit=1)

                        elements = elements[0] if elements else None
                        if elements is None:
                            elements = \
                                soup.findAll('span', {"class": str(company.price_div)}, limit=1)
                            elements = elements[0] if elements else None

                        value = float(elements.text.split('R$ ')[-1].replace('.', "").replace(",", ".")) if elements is not None else float(9999999)
                        print(f'Teste Ok')
                        if value <= min_price.min_value:
                            try:

                                ProductPriceHistory.objects.create(
                                    product=product,
                                    company=company.company,
                                    price=float(value)
                                )
                                email_template = f"""
                                Olá, o seguinte produto foi encontrado com um preço menor do que o cadastrado! 
                                
                                Produto: {product.code}
                                Descrição: {product.description}
                                Valor Minimo Cadastrado: {min_price.min_value}
                                
                                VALOR SITE: {value}
                                REVENDEDORA: {web_site}
                                
                                """
                                send_mail(
                                    'ALERTA DE PREÇO: BOT',
                                    email_template,
                                    'price.bot.checker@gmail.com',
                                    ['lucas.henrique.s.go@gmail.com', 'cleidercsa@gmail.com',
                                     'lucas.henrique@a.unileste.edu.br'],
                                    fail_silently=False
                                )

                            except Exception as e:
                                send_mail(
                                    'ALERTA: EXCEPTIONS',
                                    e.__repr__(),
                                    'price.bot.checker@gmail.com',
                                    ['lucas.henrique.s.go@gmail.com'],
                                    fail_silently=False
                                )
                                print(f'Cannot perform update for this task: {e.__repr__()}')

                    except Exception as e:
                        send_mail(
                            'ALERTA: EXCEPTIONS',
                            e.__repr__(),
                            'price.bot.checker@gmail.com',
                            ['lucas.henrique.s.go@gmail.com', 'lucas.henrique@a.unileste.edu.br'],
                            fail_silently=False
                        )
                        print(e.__repr__())

                except HTTPError as e:
                    send_mail(
                        'ALERTA: EXCEPTIONS',
                        e.__repr__(),
                        'price.bot.checker@gmail.com',
                        ['lucas.henrique.s.go@gmail.com', 'lucas.henrique@a.unileste.edu.br'],
                        fail_silently=False
                    )
                    print(e.status, e.reason)
