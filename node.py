class Node:
    def __init__(self, data):
        self.__data = data
        self.__previous = None
        self.__next = None

@property
def data(self):
    return self.__data

@data.setter
def data(self, data):
    self.__data = data


@property
def previous(self):
    return self.__previous

@previous.setter
def previous(self, previous):
    self.__previous = previous

@property
def next(self):
    return self.__next

@next.setter
def next(self, next):
    self.__next = next

