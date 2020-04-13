from datetime import datetime
import requests
import sys
# import re

date = datetime.now()
date_end = date.strftime("%d/%m/%Y %H:%M:%S")

if sys.argv[1:] == []:

    r = requests.get('https://www.worldometers.info/coronavirus/')
    text = str(r.content)

    # pad = re.compile(r"\d\d\d,\d\d\d")
    # found = pad.finditer(text)
    # for i in found:
    #     print(i)

    print(text[384:393] + " ; " + text[404:410] + " ; " + text[9788:9795] + " ; " + date_end)

elif sys.argv[1] == "brazil":

    r1 = requests.get('https://www.worldometers.info/coronavirus/country/brazil/')
    text_br = str(r1.content)
    print(text_br[375:381] + " ; " + text_br[391:395] + " ; " + text_br[8930:8933] + " ; " + date_end)

elif sys.argv[1] == "italy":

    r2 = requests.get('https://www.worldometers.info/coronavirus/country/italy/')
    text_it = str(r2.content)
    if text_it[8934] == ">":
        print(text_it[374:381] + " ; " + text_it[392:398] + " ; " + text_it[8935:8941] + " ; " + date_end)
    else:
        print(text_it[374:381] + " ; " + text_it[392:398] + " ; " + text_it[8934:8940] + " ; " + date_end)

elif sys.argv[1] == "us":

    r3 = requests.get('https://www.worldometers.info/coronavirus/country/us/')
    text_us = str(r3.content)
    if text_us[8964] == ">":
        print(text_us[382:389] + " ; " + text_us[400:405] + " ; " + text_us[8965:8971] + " ; " + date_end)
    else:
        print(text_us[382:389] + " ; " + text_us[400:405] + " ; " + text_us[8964:8970] + " ; " + date_end)

elif sys.argv[1] == "spain":

    r4 = requests.get('https://www.worldometers.info/coronavirus/country/spain/')
    text_sp = str(r4.content)
    if text_sp[8934] == ">":
        print(text_sp[374:381] + " ; " + text_sp[392:398] + " ; " + text_sp[8935:8941] + " ; " + date_end)
    else:
        print(text_sp[374:381] + " ; " + text_sp[392:398] + " ; " + text_sp[8934:8940] + " ; " + date_end)
