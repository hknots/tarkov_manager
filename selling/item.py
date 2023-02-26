import requests
import pyautogui as a


class Item:

    AVG_PRICE_MINUS = 2000

    def __init__(self, item_name: str, position: tuple):
        data = requests.get(f"https://tarkov-market.com/api/v1/item?q={item_name}&x-api-key=").json()[0]
        self.position = position
        self.name = data["name"]
        self.bannedOnFlea = data["bannedOnFlea"]
        self.base_price = data["basePrice"]
        self.trader_price = data["traderPrice"]
        self.trader = data["traderName"]
        self.avg24hPrice = data["avg24hPrice"]
        self.flea_selling_price = self.avg24hPrice - self.AVG_PRICE_MINUS
        self.worth_selling = self.flea_selling_price > self.trader_price
