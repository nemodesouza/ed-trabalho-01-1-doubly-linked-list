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
        return self__cursor.current

# - [ ]  
# - [ ]  (void) InserirAntesDoAtual ( novo )
# - [ ]  (void) InserirApósAtual ( novo )
# - [ ]  (void) inserirNoFim ( novo )
# - [ ]  (void) inserirNaFrente ( novo )
# - [ ]  (void) inserirNaPosicao ( k, novo )
# - [ ]  (void) ExcluirAtual ()
# - [ ]  (void) ExcluirPrim ()
# - [ ]  (void) ExcluirUlt ()
# - [ ]  (void) ExcluirElem ( chave )
# - [ ]  (void) ExcluirDaPos ( k )
# - [ ]  (boolean) Buscar ( chave )