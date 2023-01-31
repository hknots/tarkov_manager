from menu import Menu
from selling_menu import SellingMenu


class MainMenu(Menu):
    def __init__(self):
        options = {
            "1": "Sell",
            "2": "Exit"
        }
        super().__init__(options)
        self.selling_menu = SellingMenu(self)

    def get_option_actions(self):
        return {
            "1": self.selling_menu.choose,
            "2": self.exit
        }


menu = MainMenu()
menu.choose()