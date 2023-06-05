import json
import time

from projeto_aed.sistema.Sistema import adicionar_ponto_interesse, alterar_ponto_interesse, apagar_ponto_interesse, \
    pesquisar_ponto_interesse, mostrar_pontos_interesse, avaliar_visita, consultar_estatisticas, \
    sugestao_pontos_interesse
from projeto_aed.sistema.json import ler_ficheiro, guardar_ficheiro, fazer_backup
from projeto_aed.interface.input import opcoes_menu, sub_menu  # , interromper_via_circulacao
from projeto_aed.sistema.constantes import FICHEIRO, GRAFO
from projeto_aed.rascunhos.graph import Graph
from projeto_aed.rascunhos.Grafo_teste import Grafo, desenhar_grafo, testar_caminho,obter_itinerario,\
    obter_arvore_rotas_carro


def menu():
    fim = False
    while not fim:
        opcoes_menu()
        print("-" * 72)
        try:
            op = int(input("Opção: "))
            if op == 1:
                print("\n", "\033[4mPonta Delgada\033[0m"
                            "\nPonta Delgada é uma cidade portuguesa localizada na ilha de São Miguel\ne pertencente"
                            " à Região Autónoma dos Açores com uma população\nde 46 102 habitantes."
                            " Ponta Delgada é a capital económica da \nRegião Autónoma dos Açores "
                            "e a maior cidade desta região.")
                print("\n------------")
                input("Prima Enter para voltar ao menu principal.")

            elif op == 2:
                mostrar_pontos_interesse(linkedlist)
            elif op == 3:
                adicionar_ponto_interesse(linkedlist)
            elif op == 4:
                alterar_ponto_interesse(linkedlist)
            elif op == 5:
                apagar_ponto_interesse(linkedlist)
            elif op == 6:
                pesquisar_ponto_interesse(linkedlist)
            elif op == 7:
                avaliar_visita(linkedlist)
            elif op == 8:
                consultar_estatisticas(linkedlist)
            elif op == 9:
                sugestao_pontos_interesse(linkedlist)
            elif op == 10:
                menu_sec()
            elif op == 0:
                guardar_ficheiro(linkedlist, FICHEIRO)
                fazer_backup(FICHEIRO)
                fim = True
                print("Obrigado por utilizar o nosso programa. Até breve!")
        except ValueError:
            print("Opção inválida. Tente outra vez.")
            time.sleep(2)


def menu_sec():
    voltar_menu_principal = False
    while not voltar_menu_principal:
        sub_menu()
        print("-" * 72)
        try:
            op = int(input("Opção: "))
            if op == 1:
                desenhar_grafo(GRAFO)
            elif op == 2:
                print("consultar os pontos criticos ")
            elif op == 3:
                testar_caminho()
            elif op == 4:
                obter_itinerario()
            elif op == 5:
                ponto_interesse = input("Digite o ponto de interesse: ")
                obter_arvore_rotas_carro(ponto_interesse)
            elif op == 0:
                voltar_menu_principal = True
        except ValueError:
            print("Opção inválida. Tente outra vez.")


linkedlist = ler_ficheiro(FICHEIRO)
