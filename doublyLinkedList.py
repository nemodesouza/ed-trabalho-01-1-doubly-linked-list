from cursor import Cursor
from node import Node

class DoublyLinkedList:
    def __init__(self, limit=None):
        self.__cursor = Cursor()
        self.__limit = None
        self.__elements = 0

    @property
    def element(self):
        return self.__elements

    def accessCurrent(self):
        """(elemento) acessarAtual()"""
        return self.__cursor.current

    def insertBeforeCurrent(self, data):
        """(void) InserirAntesDoAtual ( novo )"""
        new_element = Node(data)

        if self.isFull():
            print("A lista está cheia!")
        elif self.isEmpty():
            self.__cursor.current = new_element
            self.__elements += 1
        elif self.__cursor.current.previous is None:
            self.__cursor.current.previous = new_element
            new_element.next = self.__cursor.current
            self.__elements += 1
        else:
            self.__cursor.current.previous.next = new_element
            new_element.previous = self.__cursor.current.previous
            self.__cursor.current.previous = new_element
            new_element.next = self.__cursor.current
            self.__elements += 1

    def insertAfterCurrent(self, data):
        """(void) InserirApósAtual ( novo )"""
        new_element = Node(data)

        if self.isFull():
            print("A lista está cheia!")
        elif self.isEmpty():
            self.__cursor.current = new_element
            self.__elements += 1
        elif self.__cursor.current.next is None:
            self.__cursor.current.next = new_element
            new_element.previous = self.__cursor.current
            self.__elements += 1
        
    def insertInTheEnd(self, data):
        """(void) inserirNoFim ( novo )"""
        if self.isEmpty():
            new_element = Node(data)
            self.__cursor.current = new_element
            self.__elements += 1
        else:
            self.__cursor.goToLast()
            self.insertAfterCurrent(data)

    def insertInFront(self, data):
        """(void) inserirNaFrente ( novo )"""
        if self.isEmpty():
            new_element = Node(data)
            self.__cursor.current = new_element
            self.__elements += 1
        
        else:
            self.__cursor.goToFirst()
            self.insertBeforeCurrent(data)

    
    def insertInPositionK(self, k, data):
        """(void) inserirNaPosicao ( k, novo )"""
        if self.isFull():
            print("A lista está cheia!")
        elif k < 0 or k > self.__elements:
            print("Essa posição não existe!")
        else:            
            self.__cursor.goToFirst()
            self.__cursor.advanceKPos(k-1)
            self.insertBeforeCurrent(data)


    def popCurrent(self):
        """(void) ExcluirAtual ()"""
        if self.isEmpty():
            print("A lista está vazia!")
        elif self.__cursor.current.previous is None and self.__cursor.current.next is None:
            self.__cursor.current.next = None    #verificar necessiade        
            self.__cursor.current.previous = None #verificar necessiade
            self.__cursor.current = None
            self.__elements -= 1
        elif self.__cursor.current.previous is None:
            self.__cursor.current.next.previous = None
            self.__cursor.current = self.__cursor.current.next
            self.__elements -= 1
        elif self.__cursor.current.next is None:
            self.__cursor.current.previous.next = None
            self.__cursor.current = self.__cursor.current.previous
            self.__elements -= 1
        else:
            self.__cursor.current.previous.next = self.__cursor.current.next
            self.__cursor.current.next.previous = self.__cursor.current.previous
            self.__cursor.current = self.__cursor.current.next
            self.__elements -= 1



# - [ ]  (void) ExcluirPrim ()
# - [ ]  (void) ExcluirUlt ()
# - [ ]  (void) ExcluirElem ( chave )
# - [ ]  (void) ExcluirDaPos ( k )
# - [ ]  (boolean) Buscar ( chave )



    
    
    def isEmpty(self):
        return self.__elements == 0

    def isFull(self):
        return self.__elements == self.__limit

    def positionOf(self, key): #verificar depois
        if self.isEmpty():
            print("Lista Vazia!")
        else:
            self.__cursor.goToFirst()
            element = self.__cursor.current
            position = 1
            
            while element.value != key:
                if self.__cursor.current.next is not None:
                    return None                
                else:
                    self.__cursor.advanceKPos(1)
                    element = self.__cursor.current
                    position += 1
                print(position)

                return position

    
        # Outras (de apoio):

        # - [ ]  (boolean) Vazia()
        # - [ ]  (boolean) Cheia()
        # - [ ]  (INT) posiçãoDe(chave)
