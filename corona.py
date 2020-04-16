from datetime import datetime
import requests
import sys
import re


def date_text():
    date = datetime.now()
    date_end = date.strftime("%d/%m/%Y %H:%M:%S")

    return date_end


def request_site():
    link = 'https://www.worldometers.info/coronavirus/'
    try:
        location = sys.argv[1]
        return link + f'country/{location}'
    except:
        return link


def get_site():
    r = requests.get(request_site())
    source = r.text

    return source


def update():
    match_cases = re.findall(r'\">(.*\d+,\d+)\s<', get_site())
    cases = match_cases[0]

    match_death_recoveries = re.findall(r'<span>(.*.*\d+)</span>', get_site())
    deaths = match_death_recoveries[0]
    recoveries = match_death_recoveries[1]

    return cases + " " + deaths + " " + recoveries + " " + date_text()


if __name__ == '__main__':
    date_text()
    request_site()
    get_site()
    try:
        print(update())
    except IndexError:
        print("Digite o Parâmetro-País em Inglês (Para EUA/USA, digite 'us')")
