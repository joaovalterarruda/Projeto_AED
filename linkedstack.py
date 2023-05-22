from node import Node


class LinkedStack:
    """Implementação do TDA Stack baseada em estrutura ligada"""

    def __init__(self, sourceCollection = None):
        """Define o estado inicial de self com sourceCollection"""
        self._items = None  # referencia para o primeiro nó - topo da pilha
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.push(item)

    # métodos gerais de coleção

    def is_empty(self):
        """Retorna True se len(self) é 0, senão False"""
        return self._size == 0

    def __len__(self):
        """Retorna o numero de elementos do stack"""
        return self._size

    def __str__(self):
        """Retorna a representação em string de self"""
        lista = []
        for item in self:
            lista.append(item)
        return str(lista) + " :  " + str(self._size) + " elementos"

    def clear(self):
        """Torna self vazio"""
        self._items = None
        self._size = 0

    def __iter__(self):
        """Suporta a iteração sobre self"""
        cursor = self._items
        while not cursor is None:
            yield cursor.get_data()
            cursor = cursor.get_next()

    def peek(self):
        """Retorna o ‘item’ que está no topo de self.
        Precondição: self não é vazio."""
        if not self.is_empty():
            return self._items.get_data()
        else:
            raise KeyError(" pilha vazia!")

    def push(self, item):
        """ Sobrepoe ‘item’ a self
            Poscondição: ‘item’ foi sobreposto a self"""
        self._items = Node(item, self._items)
        self._size += 1

    def pop(self):
        """Remove elemento do topo de self e retorna esse elemento.
             Precondição: self não é vazio.
             Poscondição: topo foi removido de self"""
        if len(self) > 0:
            self._size -= 1
            top = self._items.get_data()
            self._items = self._items.get_next()
            return top
        else:
            raise KeyError(" pilha vazia!")
