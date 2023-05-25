from PontoInteresse import PontoInteresse
from grafo import Grafo
import networkx as nx
import matplotlib.pyplot as plt
from inputs import ler_grafo


class System():
    def __init__(self, ficheiro_grafo):
        self._ponto_interesse = PontoInteresse
        self._rede: Grafo = Grafo(orientado=True)
        self._rede._grafo = ler_grafo(ficheiro_grafo)

    def obter_grafo(self) -> dict:
        return self._rede.obter_grafo()

    def obter_grafo_str(self) -> str:
        return str(self._rede)

    def mostrar_grafo(self) -> None:
        g = nx.DiGraph(self._rede.obter_grafo())
        pos = nx.spring_layout(g)  # Utiliza o algoritmo de posicionamento spring layout
        nx.draw(g, pos, with_labels=True)
        plt.show()

    def adicionar_ponto_grafo(self) -> None:
        nome_ponto: str = input("Introduza o nome do novo ponto do grafo: ").upper()
        self._rede.adicionar_ponto(nome_ponto)

    def remover_ponto_grafo(self) -> None:
        nome_ponto: str = input("Introduza o nome do ponto a remover do grafo: ").upper()
        self._rede.remover_ponto(nome_ponto)

    def adicionar_caminho_grafo(self) -> None:
        ponto1: str = input("Introduza o nome do ponto de origem: ").upper()
        ponto2: str = input("Introduza o nome do ponto de chegada: ").upper()
        custo: str = input("Introduza o custo de viagem: ")
        if custo.isdigit():
            self._rede.ligar_pontos(ponto1, ponto2, int(custo))
        else:
            print("Custo inválido. O custo deve ser um valor numérico.")

    def remover_caminho_grafo(self) -> None:
        ponto1: str = input("Introduza o nome do ponto de origem: ").upper()
        ponto2: str = input("Introduza o nome do ponto de chegada: ").upper()
        self._rede.desligar_pontos(ponto1, ponto2)

    def calcular_caminho(self, from_label, to_label):
        if self._rede.verificar_ponto(from_label) and self._rede.verificar_ponto(to_label):
            caminho_curto = self._rede.caminho_mais_curto(from_label, to_label)
            custo = self._rede.calcular_custo_caminho(caminho_curto)
            print(caminho_curto, custo)
            return custo

    def __str__(self) -> str:
        # completar
        pass

