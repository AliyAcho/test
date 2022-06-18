import requests
import xml.etree.ElementTree as ET

def get_dollar():
    url = "https://www.cbr.ru/scripts/XML_daily.asp?date_req="
    res = requests.get(url)
    xml = ET.fromstring(res.content)
    dollar = xml.find("./*[@ID='R01235']/Value")
    return float(dollar.text.replace(',', '.')) 