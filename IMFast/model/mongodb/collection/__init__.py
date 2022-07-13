from abc import ABCMeta
from datetime import datetime
from model.mongodb import db

# TODO how to schema?

class Model(metaclass=ABCMeta):

    VERSION = 1

    def __init__(self):
        self.col = db[self.__class__.__name__]

    def index(self) -> list:
        """Collection index"""
        return []

    def create_index(self):
        """Create index"""
        index = self.index()
        if index:
            self.col.create_indexes(index)

    def p(self, *args) -> dict:
        """projection shortcut method"""
        return {field: 1 for field in args}
