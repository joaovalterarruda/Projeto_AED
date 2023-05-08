class Pilha:
    def __init__(self) -> None:
        self._pilha = []
        self._tamanho = 0

    def e_vazia(self) -> bool:
        """
        Verifica se a pilha está vazia

        :return: bool dizendo se a pilha está vazia
        """
        return self._pilha == []

    def __len__(self) -> int:
        """
        Retorna o tamanho da pilha

        :return: o comprimento da pilha
        """
        return self._tamanho

    def __contains__(self, item) -> bool:
        """
        Verifica se a pilha possui um item

        :param item: item a verificar
        :return: bool
        """
        return self._pilha.__contains__(item)

    def __str__(self) -> str:
        return str(self._pilha)

    def adicionar(self, elemento) -> None:
        """
        Permite adicionar um valor ou uma lista de valores

        :param elemento: elemento / lista de elementos
        :return: None
        """
        if type(elemento) == list:
            self._tamanho += len(elemento)
            for i in elemento:
                self._pilha.append(i)
        else:
            self._pilha.append(elemento)
            self._tamanho += 1

    def retirar(self):
        """
        Retira o último elemento da pilha

        :return: último elemento da pilha
        """
        if not self.e_vazia():
            self._tamanho -= 1
            return self._pilha.pop()
        else:
            print("Pilha vazia!")

    def visualizar(self) -> None:
        """ Imprime todos os elementos da pilha """
        for elemento in self._pilha:
            print(elemento)
