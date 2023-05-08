class Fila:
    """docstring for Pilha"""

    def __init__(self):
        self._itens = []
        self._tamanho = 0

    def __len__(self) -> int:
        """
		Retorna o tamanho da fila
		:return: o comprimento da fila
		"""
        return self._tamanho

    def __contains__(self, item) -> bool:
        """
		Verifica se a fila possui um valor
		:param item: item a verificar
		:return: bool
		"""
        return self._itens.__contains__(item)

    def __str__(self) -> str:
        return str(self._itens)

    def e_vazia(self) -> bool:
        """
		Verifica se a fila está vazia
		:return: bool dizendo se a fila está vazia
		"""
        return len(self) == 0

    def add(self, value) -> None:
        """
		Permite adicionar um valor ou uma lista de valores
		:param value: elemento / lista de elementos
		:return: None
		"""
        if type(value) == list:
            self._tamanho += len(value)
            for i in value:
                self._itens.append(i)
        else:
            self._tamanho += 1
            self._itens.append(value)

    def remove(self):
        """
		Retira o primeiro elemento da fila
		:return: primeiro elemento da fila
		"""
        if len(self) > 0:
            self._tamanho -= 1
            item = self._itens[0]
            self._itens = self._itens[1:]
            return item

    def mostrar_fila(self) -> None:
        """
        Mostra os elementos da fila
        """
        print(self._itens)
