import json

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    """
        Uma lista ligada simples.

        Attributes:
            head: O primeiro nó da lista.
            tail: O último nó da lista.
            length: O tamanho da lista.
        """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, data):
        """
        Adiciona um novo elemento no final da lista.

        Args:
            data: O dado a ser adicionado.

        Returns:
            None
        """

        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove(self, data):
        """
        Remove a primeira ocorrência do dado especificado da lista.

        Args:
            data: O dado a ser removido.

        Returns:
            None
        """
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            if self.head is None:
                self.tail = None
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self.length -= 1
                if current.next is None:
                    self.tail = current
                return
            current = current.next

    def find(self, data):
        """
        Procura a primeira ocorrência do dado especificado na lista.

        Args:
            data: O dado a ser procurado.

        Returns:
            Node: O nó contendo o dado, ou None se o dado não for encontrado.
        """
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def update(self, old_data, new_data):
        """
        Atualiza o valor de um dado na lista.

        Args:
            old_data: O dado a ser atualizado.
            new_data: O novo valor do dado.

        Returns:
            None
        """
        node = self.find(old_data)
        if node is not None:
            node.data = new_data

    def insertion_sort(self, key=lambda x: x):
        """
        Ordena a lista usando o algoritmo de ordenação por inserção.

        Args:
            key (function): A função de chave opcional para personalizar a ordenação.

        Returns:
            None
        """
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            sorted_head = self.insert_sorted(sorted_head, current, key)
            current = next_node

        self.head = sorted_head

    @staticmethod
    def insert_sorted(sorted_head, node, key):
        if sorted_head is None or key(node.data) <= key(sorted_head.data):
            node.next = sorted_head
            return node

        current = sorted_head
        while current.next and key(node.data) > key(current.next.data):
            current = current.next

        node.next = current.next
        current.next = node

        return sorted_head

    def to_list(self):
        """
        Converte a lista ligada em uma lista Python.

        Returns:
            list: A lista Python.
        """
        lst = []
        node = self.head
        while node is not None:
            lst.append(node.data)
            node = node.next
        return lst


    def load_from_json(self, nome_ficheiro):
        """
        Carrega os dados da lista a partir de um arquivo JSON.

        Args:
           nome_ficheiro (str): O nome do arquivo JSON.

        Returns:
           None
        """
        with open(nome_ficheiro, 'r', encoding="UTF-8") as f:
            conteudo = json.load(f)
        for item in conteudo:
            self.add(item)
        print("Ficheiro " + nome_ficheiro + " carregado com sucesso.")


    def save_to_json(self, nome_ficheiro):
        """
        Salva os dados da lista num arquivo JSON.

        Args:
            nome_ficheiro (str): O nome do arquivo JSON.

        Returns:
            None
        """
        with open(nome_ficheiro, 'w', encoding="UTF-8") as f:
            conteudo = []
            current = self.head
            while current is not None:
                conteudo.append(current.data)
                current = current.next
            json.dump(conteudo, f, indent=4)
        print("Ficheiro " + nome_ficheiro + " guardado com sucesso.")

    def __iter__(self):
        """
        Retorna um iterador para percorrer os elementos da lista.

        Returns:
            iterator: um iterador para percorrer os elementos da lista.
        """
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def __str__(self):
        """
        Retorna uma representação em string da lista.

        Returns:
            str: A representação em string da lista.
        """
        current = self.head
        items = []
        while current is not None:
            items.append(str(current.data))
            current = current.next
        return ' -> '.join(items)
