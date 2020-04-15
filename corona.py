from datetime import datetime
import requests
import sys
import re


# class Corona:
#     def __init__(self, country):
#         self.location = country
#         self.cases = ''
#         self.deaths = ''
#         self.recoveries = ''

def data_texto():
    date = datetime.now()
    date_end = date.strftime("%d/%m/%Y %H:%M:%S")

    return date_end


def request_site():
    location = sys.argv[1:]
    link = 'https://www.worldometers.info/coronavirus/'
    if location != 'world':
        return link + f'country/{location}'
    else:
        return link


def get_site():
    r = requests.get(request_site())
    source = r.text

    return source


def update():
    cases_regex = re.compile(r'<h1>Coronavirus[\S\s]+\">([\d, ]+)<\Wspan>\s<\Wdiv>')
    cases_search = cases_regex.search(data_texto())
    cases = cases_search.group(1)
    deaths_regex = re.compile(r'<h1>Deaths:<\Wh1>\s<[\s\S]+\Smaincounter-number\S>\s<span>([\d, ]+)<\Sspan>')
    deaths_search = deaths_regex.search(data_texto())
    deaths = deaths_search.group(1)
    recoveries_regex = re.compile(
        r'<h1>Recovered:<\Wh1>\s<[\s\S]+\W{2}maincounter-number\W\sstyle\W{2}color:\W8ACA2B\s\W>\s<span>([\d, ]+)<\Sspan>')
    recoveries_search = recoveries_regex.search(data_texto())
    recoveries = recoveries_search.group(1)
    cases = cases.replace(',', '')
    cases = cases.replace(' ', '')
    deaths = deaths.replace(',', '')
    recoveries = recoveries.replace(',', '')

    print(cases, deaths, recoveries)
    return {cases, deaths, recoveries}


if __name__ == 'main':
    data_texto()
    request_site()
    get_site()
    update()


