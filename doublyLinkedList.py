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

    def popFirst(self):
        """(void) ExcluirPrim ()"""
        self.__cursor.goToFirst()
        self.popCurrent()

    def popLast(self):        
        """(void) ExcluirUlt ()"""
        self.__cursor.goToLast()
        self.popCurrent()

    def popElement(self, element):
        """(void) ExcluirElem ( chave )"""
        self.search(element)
        self.popCurrent()
        print(f"O elemento {element} foi excluído!")
    
    def excludeFromPos(self, k):
        """(void) ExcluirDaPos ( k )"""        
        if self.isEmpty():
            print("A lista está vazia!")
        elif k > self.__elements or k < 0:
            print("A posição não existe!")
        else:
            k-=1
            self.__cursor.goToFirst()
            self.__cursor.advanceKPos(k)
            self.popCurrent()
    
    

    def search(self, key):
        """(boolean) Buscar ( chave )"""
        self.__cursor.goToFirst()
        element = self.__cursor.current

        while element.data != key:
            if self.__cursor.current.next is None:
                print("Print: False, elemento inexistente!")
                return False
            else:
                self.__cursor.advanceKPos(1)
                element = self.__cursor.current
        print("Print: True, o elemento informado existe na lista!")
        return True

    # Outras (de apoio):

    def isEmpty(self):
        """(boolean) Vazia()"""
        return self.__elements == 0

    def isFull(self):
        """(boolean) Cheia()"""
        return self.__elements == self.__limit
        
    def positionOf(self, key):
        """(INT) posiçãoDe(chave)"""
        if self.isEmpty():
            print("A lista está vazia!")
        else:
            self.__cursor.goToFirst()
            current = self.__cursor.current
            position = 1

            while current.data != key:
                if self.__cursor.current.next is None:
                    print("Elemento inexistente!")
                    return None
                else:
                    self.__cursor.advanceKPos(1)
                    current = self.__cursor.current
                    position += 1
                print(f"A posição do elemento {key} é a de n. {position}!")
