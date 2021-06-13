def format_html(html:str):
    return " ".join(html.split()).replace('> <', '><')
