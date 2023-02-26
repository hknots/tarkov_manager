import pyautogui as pya
from scav_box import ScavBox
from selling.item import Item
from navigator import Navigator
import multiprocessing
import keyboard
import os
import time


class Selling(Navigator):

    pya.PAUSE = 0.2

    def __init__(self):
        super().__init__()
        self.scav_boxes = []

    def sell_all_items(self):
        self.if_not_at_go_to("character")
        self.locate_scav_boxes_in_inventory()
        self.scan_items_in_scavboxes()

        self.if_not_at_go_to("flea market")
        self.close_all_windows()
        self.__open_add_offer()
        self.__setup_add_offer_window()
        self.__update_scav_box_locations()
        self.close_all_windows()
        self.sell_items_in_scavbox()

    @staticmethod
    def scan_items_parallel(image_path: str):
        item = pya.locateCenterOnScreen(image_path, confidence=0.8, region=(0, 0, 893, 915))
        if item:
            item_name = image_path.replace("./selling/item images/", "")[:-4]
            return Item(item_name, item)

    def locate_scav_boxes_in_inventory(self):
        boxes = list(pya.locateAllOnScreen("./scav box.png", confidence=0.96))
        for box_location in boxes:
            scav_box = ScavBox(pya.center(box_location))
            self.scav_boxes.append(scav_box)

    def __update_scav_box_locations(self):
        boxes = list(pya.locateAllOnScreen("./scav box gray.png", confidence=0.98))
        for i in range(len(boxes)):
            print("GRAY BOX FOUND SIR")
            self.scav_boxes[i].location = pya.center(boxes[i])

    def scan_items_in_scavboxes(self):
        image_paths = [f"./selling/item images/{i}" for i in os.listdir("./selling/item images/") if "screenshot" not in i]
        for scavbox in self.scav_boxes:
            self.__open_and_move_scav_box(scavbox.location)
            with multiprocessing.Pool() as pool:
                item_list = pool.map(self.scan_items_parallel, image_paths)
                item_list = [i for i in item_list if i is not None]
            print(f"Amount of items found: {len(item_list)}")
            scavbox.items = item_list
            self.close_all_windows()

    def sell_items_in_scavbox(self):
        for scavbox in self.scav_boxes:
            for item in scavbox.items:
                if item.worth_selling and not item.bannedOnFlea:
                    print("Selling: ", item.name)
                    time.sleep(0.25)
                    self.__open_add_offer()
                    self.__open_and_move_scav_box(scavbox.location, flea_selling=True)
                    self.__sell_item(item)
                    print(f"Item sold! ")
                else:
                    print(f"Skipping {item.name} Worth selling: {item.worth_selling} Banned on flea: {item.bannedOnFlea}")

    @staticmethod
    def __open_add_offer():
        pya.FAILSAFE = False
        pya.moveTo(0, 0)
        while True:
            pya.moveTo(50, 50)
            pya.moveTo(1265, 78)
            if pya.pixel(1161, 73)[0] > 200:
                pya.click(1261, 78)
                break

    @staticmethod
    def __open_and_move_scav_box(location: tuple, flea_selling=False):
        if flea_selling:
            open_y_positon = 35
        else:
            open_y_positon = 55

        pya.rightClick(location)
        pya.moveRel(10, open_y_positon)
        pya.leftClick()
        pya.moveTo(949, 100)
        pya.dragTo(1, 1, 0.5)
        if keyboard.is_pressed("down"):
            exit()

    @staticmethod
    def __setup_add_offer_window():
        x, y = pya.locateCenterOnScreen("./autoselect similar.png", confidence=0.9)
        pya.click(x, y)
        pya.moveTo(x, y - 30)
        pya.dragTo(1, 1079, 0.4)

    @staticmethod
    def __sell_item(item: Item):
        pya.click(item.position)
        pya.click(1058, 661)
        pya.click(968, 195)
        pya.write(str(item.flea_selling_price), interval=0.1)
        pya.click(963, 904)
        pya.click(817, 1035)
