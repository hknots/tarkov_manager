import requests
import os


class Item:
    def __init__(self, item_name: str):
        data = requests.get(f"https://tarkov-market.com/api/v1/item?q={item_name}&x-api-key={os.environ['API_KEY']}").json()[0]
        self.name = data["name"]
        self.bannedOnFlea = data["bannedOnFlea"]
        self.base_price = data["basePrice"]
        self.trader_price = data["traderPrice"]
        self.trader = data["traderName"]


f = Item("Pliers Elite")
print(f.name, f.bannedOnFlea)