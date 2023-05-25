from typing import List
from fila import Fila
from pilha import Pilha


class Grafo:
    def __init__(self, orientado: bool = False) -> None:
        """
        Cria um grafo vazio

        :param orientado: Define se o grafo é orientado ou não orientado através de um booleano
        """
        self._grafo: dict[str, dict[str, float]] = dict()
        self._orientado: bool = orientado

    def esta_vazio(self) -> bool:
        return self.numero_vertices() == 0

    # métodos relacionados com o tamanho do grafo
    def numero_vertices(self) -> int:
        """
        Retorna o número de vertices presentes no grafo

        :return: número inteiro de vertices no grafo
        """
        return len(self._grafo)

    def numero_arestas(self) -> int:
        """
        Retorna o número de arestas presentes no grafo

        :return: número inteiro de arestas no grafo
        """
        if not self._orientado:
            i = 0
            for v in list(self._grafo.values()):
                i += len(v)
            return int(i / 2)
        else:
            i = 0
            for v in list(self._grafo.values()):
                i += len(v)
            return i

    def __str__(self) -> str:
        texto = "{\n"
        keys = list(self._grafo.keys())
        for i in range(len(keys)):
            if i != len(keys)-1:
                texto += f'    "{keys[i]}": {self._grafo[keys[i]]},\n'
            else:
                texto += f'    "{keys[i]}": {self._grafo[keys[i]]}\n'
        texto = texto.replace("'", '"')
        texto += "}"
        return texto

    def __iter__(self):
        return iter(self._grafo)

    def limpar_grafo(self) -> None:
        """
        Limpa o grafo

        :return: None
        """
        self._grafo.clear()

    def obter_vertices(self) -> set[str]:
        return set(self._grafo.keys())

    def obter_grafo(self) -> dict:
        return self._grafo

    def adicionar_ponto(self, nome_ponto) -> None:
        """
        Adiciona um ponto ao grafo

        :param nome_ponto: nome do ponto
        :return: None
        """
        if nome_ponto not in self._grafo:
            self._grafo.__setitem__(nome_ponto, dict())

    def ligar_pontos(self, nome_ponto1: str, nome_ponto2: str, custo: float = 0) -> None:
        """
        Liga dois pontos que já existem no grafo

        :param nome_ponto1: nome do primeiro ponto
        :param nome_ponto2: nome do segundo ponto
        :param custo: custo de passar de um ponto para o outro
        :return: None
        """
        if self.verificar_ponto(nome_ponto1) and self.verificar_ponto(nome_ponto2):
            if nome_ponto2 not in self._grafo[nome_ponto1]:
                self._grafo[nome_ponto1].__setitem__(nome_ponto2, custo)
                if not self._orientado:
                    self._grafo[nome_ponto2].__setitem__(nome_ponto1, custo)

    def remover_ponto(self, nome_ponto: str) -> None:
        """
        Remove um ponto e todas as suas conexões

        :param nome_ponto: nome do ponto a remover
        :return: None
        """
        if self.verificar_ponto(nome_ponto):
            # self._grafo.pop(nome_ponto)
            del(self._grafo[nome_ponto])
            for k, v in self._grafo.items():
                if nome_ponto in v:
                    v.pop(nome_ponto)

    def desligar_pontos(self, nome_ponto1: str, nome_ponto2: str) -> None:
        """
        Retira a ligação entre dois pontos que já existem no grafo

        :param nome_ponto1: nome do primeiro ponto
        :param nome_ponto2: nome do segundo ponto
        :return: None
        """
        if self.verificar_ponto(nome_ponto1) and self.verificar_ponto(nome_ponto2):
            if nome_ponto2 in self._grafo[nome_ponto1]:
                self._grafo[nome_ponto1].pop(nome_ponto2)
                if not self._orientado:
                    self._grafo[nome_ponto2].pop(nome_ponto1)
            else:
                print("Os pontos não estão ligados")

    def get_ponto(self, nome_ponto: str) -> dict:
        """
        Retorna um dicionário com todos as conexões do ponto

        :param nome_ponto: nome do ponto
        :return: dicionário com todas as conexões e custos que o ponto possuí
        """
        return self._grafo[nome_ponto]

    def verificar_ponto(self, nome_ponto: str) -> bool:
        """
        Verifica se um ponto existe no grafo

        :param nome_ponto: nome do ponto a verificar
        :return: bool
        """
        return self._grafo.__contains__(nome_ponto)

    def vizinhos_do_ponto(self, nome_ponto: str) -> List:
        """
        Cria uma lista com os pontos onde o nome_ponto tenha conexão

        :param nome_ponto: ponto
        :return: lista com os vizinhos do ponto
        """
        return list(self._grafo[nome_ponto].keys())

    def travessia_largura_a_partir(self, nome_ponto_inicial: str):
        """
        Faz a travessia em largura a partir de um ponto

        :param nome_ponto_inicial: ponto onde a travessia começa
        :return: lista com a travessia em largura
        """
        if self.verificar_ponto(nome_ponto_inicial):
            pontos_a_passar: Fila = Fila()
            pontos_a_passar.add(nome_ponto_inicial)
            travessia = []
            while not pontos_a_passar.e_vazia():
                ponto: str = pontos_a_passar.remove()
                if not travessia.__contains__(ponto):
                    travessia.append(ponto)
                    pontos_a_passar.add(sorted(self.vizinhos_do_ponto(ponto)))
            return travessia
        else:
            print("O ponto não existe")

    def travessia_profundidade_a_partir(self, nome_ponto_inicial: str):
        """
        Faz a travessia em profundidade a partir de um ponto

        :param nome_ponto_inicial: ponto onde a travessia começa
        :return: lista com a travessia em profundidade
        """
        if self.verificar_ponto(nome_ponto_inicial):
            pontos_a_passar: Pilha = Pilha()
            pontos_a_passar.adicionar(nome_ponto_inicial)
            travessia = []
            while not pontos_a_passar.e_vazia():
                ponto: str = pontos_a_passar.retirar()
                if not travessia.__contains__(ponto):
                    travessia.append(ponto)
                    pontos_a_passar.adicionar(sorted(self.vizinhos_do_ponto(ponto), reverse=True))
            return travessia
        else:
            print("o ponto não existe")

    def caminho_mais_curto(self, from_label: str, to_label: str) -> list[str]:
        result = {}
        fila: Fila = Fila()
        if self.verificar_ponto(from_label) and self.verificar_ponto(to_label):
            result[from_label] = (0, None)
            fila.add((from_label, 0, None))
            while not fila.e_vazia():
                front = fila.remove()
                if front[0] not in result:
                    result[front[0]] = (front[1] + 1, front[2])
                for v in self._grafo[front[0]]:
                    if v not in result:
                        fila.add((v, front[1] + 1, front[0]))
            try:
                return self.de_resultado_ao_caminho_mais_curto(result, to_label)
            except KeyError:
                print("Os dois pontos não têm conexão")
        return []

    def de_resultado_ao_caminho_mais_curto(self, result: dict, to_label: str) -> list[str]:
        reversed_path: Pilha = Pilha()
        reversed_path.adicionar(to_label)
        vc = to_label
        while result[vc][1] is not None:
            vc = result[vc][1]
            reversed_path.adicionar(vc)
        path = []
        while not reversed_path.e_vazia():
            path.append(reversed_path.retirar())
        return path

    def calcular_custo_caminho(self, caminho: list[str]) -> int:
        result = 0
        if len(caminho) > 0:
            end = False
            i = 0
            while not end:
                if i+1 == len(caminho):
                    end = True
                else:
                    result += self._grafo[caminho[i]][caminho[i+1]]
                    i += 1

        return result
