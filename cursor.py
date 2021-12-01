class Cursor:
    self.__current = None

@property
def current(self):
    """Retorna o elemento atlatl"""
    return self.__current

@current.setter
def current(self, Element):
    """Define o elemento atual"""
    self.__current = Element

def advanceKPos(self, k):
    """Avança k posições na lista"""
    for i in range(k):
        self.__current = self.__current.next

def goBackwardKPos(self, k):
    """Retrocede k posições na lista"""
    for i in range(k):
        self.__current = self.__current.previous

def goToFirst(self):
    """Vai para o primeiro elemento"""
    while self.__current is not None:
        self.__current = self.__current.previous

def goToLast(self):
    """Vai para o último elemento"""
    while self.__current is not None:
        self.__current = self.__current.next


