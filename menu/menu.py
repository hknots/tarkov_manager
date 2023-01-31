import os


class Menu:
    def __init__(self, options: dict, previous_menu=None):
        self.options = options
        self.previous_menu: Menu = previous_menu

    @staticmethod
    def clear_menu():
        os.system('cls' if os.name == 'nt' else 'clear')

    def display(self):
        self.clear_menu()
        for key in self.options:
            print(f"{key}: {self.options[key]}")

    def choose(self):
        choice = None
        option_actions = self.get_option_actions()
        while choice not in option_actions.keys():
            self.display()
            choice = input("Choice: ")
            if choice in option_actions.keys():
                option_actions[choice]()

    def get_option_actions(self):
        return {}

    @staticmethod
    def exit():
        exit()
