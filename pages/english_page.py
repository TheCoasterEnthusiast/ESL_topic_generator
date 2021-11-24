import random

from bs4 import BeautifulSoup
from typing import List

from locators.english_page_locators import EnglishPageLocators
from menu import Menus
from parsers.unit_parser import UnitParser


class EnglishPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def units(self) -> List[UnitParser]:
        unit_tags = self.soup.select(EnglishPageLocators.UNIT)
        return [UnitParser(e) for e in unit_tags]

    def print_random_topic(self):
        random_unit = self.get_random_unit()
        random_index = random.randrange(0, len(random_unit.topics))
        random_topic = random_unit.topics[random_index]
        random_link = random_unit.link[random_index]
        print(f"""Unit: {random_unit.unit_name}
Topic: {random_topic}
Link: http://curso-ingles.com{random_link}"""
              )

    def get_random_unit(self):
        units = self.units
        random_unit = units[random.randrange(0, len(units))]
        return random_unit

    def print_continue_menu(self):
        user_input = input(Menus.CONTINUE_MENU)
        while user_input != 'n':
            if user_input == 'y':
                self.print_random_topic()
            else:
                print("Invalid input, please try again.")
            user_input = input(Menus.CONTINUE_MENU)
