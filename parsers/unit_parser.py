from typing import List

from locators.unit_parser_locators import UnitParserLocators


class UnitParser:
    def __init__(self, parent):
        self.parent = parent

    @property
    def unit_name(self) -> str:
        return self.parent.select_one(UnitParserLocators.UNIT_NAME).string

    @property
    def topics(self) -> List[str]:
        return [e.string for e in self.parent.select(UnitParserLocators.TOPIC)]

    @property
    def link(self) -> List[str]:
        return [e.attrs['href'] for e in self.parent.select(UnitParserLocators.LINK)]
