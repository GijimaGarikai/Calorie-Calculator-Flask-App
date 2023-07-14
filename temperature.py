import requests
from selectorlib import Extractor


class Temperature:
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    """
    Represents a temperature extracted from
    the timeanddate.com/weather webpage
    """

    def __init__(self, country, city):
        self.country = country.replace(" ", "-").lower()
        self.city = city.replace(" ", "-").lower()

    def build_url(self):
        site = f"https://www.timeanddate.com/weather/{self.country}/{self.city}"
        return site

    def scrape(self):
        request = requests.get(self.build_url(), headers=self.headers)
        content = request.text
        return content

    def extract(self):
        extractor = Extractor.from_yaml_file('temperature.yaml')
        raw_result = extractor.extract(self.scrape())
        return raw_result

    def get(self):
        raw_result = self.extract()
        try:
            temp = float(raw_result['temp'].replace("\xa0°F", ""))
        except:
            print("City not found. Error in input")
            return 0
        return temp


test = Temperature('Zimbabwe', 'Harare')
test.get()


