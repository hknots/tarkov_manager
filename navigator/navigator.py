import pyautogui as pya
import os
import time


class Navigator:

    pya.PAUSE = 0.2

    def __init__(self):
        self.locations = self.__setup_locations()

    def go_to(self, location_name: str):
        location = pya.locateCenterOnScreen(self.locations[location_name], grayscale=True, confidence=0.95)
        if location:
            pya.click(location)

    def not_at(self, location_name: str) -> bool:
        location = pya.locateCenterOnScreen(self.locations[location_name])
        if location:
            return True

    def if_not_at_go_to(self, location: str):
        if self.not_at(location):
            self.go_to(location)
            time.sleep(0.5)

    def close_all_windows(self):
        exit_button = pya.locateCenterOnScreen(self.locations['exit'], confidence=0.95)
        if exit_button:
            pya.click(exit_button)
            return self.close_all_windows()

    @staticmethod
    def __setup_locations():
        prefix = "./navigator/location images/"
        res = {}
        for location_name in os.listdir(prefix):
            res[location_name[:-4]] = prefix + location_name
        return res
