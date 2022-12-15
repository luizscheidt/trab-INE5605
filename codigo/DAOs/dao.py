import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource,'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()


    def update(self, key, obj):
        if self.__cache.get(key):
            self.__cache[key] = obj
            self.__dump()

    def get(self, key):
        return self.__cache.get(key)


    def remove(self, key):
        self.__cache.pop(key, None)
        self.__dump()

    def get_all(self):
        return self.__cache.values()
