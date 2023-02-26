import os
import keyboard
import time


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
        self.display()
        time.sleep(0.5)
        option_actions = self.get_option_actions()
        while True:
            choice = keyboard.read_key()
            if choice in self.options.keys():
                option_actions[choice]()
                break

    def get_option_actions(self):
        return {}
