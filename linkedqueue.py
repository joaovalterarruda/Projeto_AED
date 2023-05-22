from node import Node


class LinkedQueue:
    """Implementação do TDA Queue baseada em estrutura ligada"""

    def __init__(self, sourceCollection = None):
        """Define o estado inicial de self com sourceCollection"""
        self._front = None  # referencia nó da frente da fila
        self._rear = None  # referencia ultimo nó da fila
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # métodos gerais de coleção
    def is_empty(self):
        """Retorna True se len(self) é 0, senão False"""
        return self._size == 0

    def __len__(self):
        """Retorna o número de elementos da queue"""
        return self._size

    def __str__(self):
        """Retorna a representação em ‘string’ de self"""
        return ""

    def clear(self):
        """Torna o self vazio"""
        self._front = None  # referencia nó da frente da fila
        self._rear = None  # referencia ultimo nó da fila
        self._size = 0

    def __iter__(self):
        """Suporta a iteração sobre self"""
        cursor = self._front
        while not cursor is None:
            yield cursor.get_data()
            cursor = cursor.get_next()

    # métodos específicos da fila

    def peek(self):
        """Retorna o ‘item’ que está na frente de self.
             Precondição: self não é vazio."""
        return self._front.get_data()

    def add(self, item):
        """Acrescenta ‘item’ a self no fim
            Poscondição: ‘item’ foi acrescentado a self"""
        novo = Node(item)
        if self.is_empty():
            self._front = novo
            self._rear = self._front
        else:
            self._rear.set_next(novo)
            self._rear = novo

        self._size += 1

    def pop(self):
        """Remove elemento do topo de self e retorna esse elemento.
             Precondição: self não é vazio.
             Poscondição: ‘item’ foi removido de self """
        front = self._front.get_data()
        self._front = self._front.get_next()
        if self._front is None:
            self._rear = None
        self._size -= 1
        return front
