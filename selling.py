import pyautogui as pya
from scav_box import ScavBox
from item import Item
import multiprocessing
import os


class Selling:

    pya.PAUSE = 0.25

    def __init__(self):
        self.scav_boxes = []

    def locate_scav_boxes(self):
        boxes = list(pya.locateAllOnScreen("./Scav box.png", confidence=0.99))
        for box_location in boxes:
            scav_box = ScavBox(pya.center(box_location))
            self.scav_boxes.append(scav_box)

    @staticmethod
    def scan_items_parallel(image_path: str):
        item = pya.locateCenterOnScreen(image_path, confidence=0.95)
        if item:
            item_name = image_path.replace("./item images/", "")[:-4]
            return Item(item_name)

    @staticmethod
    def __open_and_move_scav_box(location: tuple):
        pya.rightClick(location)
        pya.moveRel(10, 35)
        pya.leftClick()
        pya.moveTo(949, 93)
        pya.dragTo(200, 200, 1)

    def scan_items(self):
        image_paths = [f"./item images/{i}" for i in os.listdir("./item images/") if "screenshot" not in i]
        for ScavBox in self.scav_boxes:
            self.__open_and_move_scav_box(ScavBox.location)
            with multiprocessing.Pool() as pool:
                item_list = pool.map(self.scan_items_parallel, image_paths)
            ScavBox.items = item_list
            print(ScavBox.items)


        # Scan items of n scanbox

        # Run query against tarkov api and generate Item objects and save them if its worth selling

        # Store the Item object inside-of an object called scav box
        pass

    def sell_items(self):
        ## Setup
        # Open add over and move to bottom right

        # Check Autoselect similar

        # Close

        ## Loop while items to sell
        # Click on Add offer when available

        # Open scav box and move it bottom left

        # Click on position of item thats worth selling

        # Click on plus

        # Click on ruble area and input amount

        # Click add

        # Click Place offer
        pass

    def check_flea_selling_status(self):
        if pya.locateOnScreen("./Flea Market.png", confidence=0.9):
            print("yes")