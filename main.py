import multiprocessing

from selling import Selling
import time


def main():
    test = Selling()
    test.sell_all_items()


if __name__ == "__main__":
    main()
