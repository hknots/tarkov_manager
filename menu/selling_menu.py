from menu import Menu


class SellingMenu(Menu):
    def __init__(self, previous_menu: Menu):
        options = {
            "1": "Sell trash to traders",
            "2": "Display best flea sales",
            "3": "Sell to flea with low pricing",
            "4": "Sell to flea with avg pricing",
            "5": "Go back"
        }
        super().__init__(options, previous_menu)

    def get_option_actions(self):
        return {
            "1": self.go_back,
            "2": self.go_back,
            "3": self.go_back,
            "4": self.go_back,
            "5": self.go_back
        }

    def go_back(self):
        self.previous_menu.choose()
