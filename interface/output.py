
import time


from sistema.json import carregar_dados_grafo
from interface.input import opcoes_menu, sub_menu  # , interromper_via_circulacao
from sistema.constantes import GRAFO, FREGUESIAS
from sistema.sistema import Sistema, mostrar_info_conselho
grafo = carregar_dados_grafo(GRAFO)
sist = Sistema()
def menu():
    fim = False
    while not fim:
        opcoes_menu()
        print("-" * 72)
        try:
            op = int(input("Opção: "))
            if op == 1:
                mostrar_info_conselho()
            elif op == 2:
                sist.mostrar_pontos_interesse()
            elif op == 3:
                sist.adicionar_ponto_interesse()
            elif op == 4:
                sist.alterar_ponto_interesse()
            elif op == 5:
                sist.apagar_ponto_interesse()
            elif op == 6:
                sist.pesquisar_ponto_interesse()
            elif op == 7:
                sist.avaliar_visita()
            elif op == 8:
                sist.consultar_estatisticas()
            elif op == 9:
                sist.sugestao_pontos_interesse()
            elif op == 10:
                menu_sec()
            elif op == 11:
                sist.inserir_pontos_interesse_json()
            elif op == 0:
                sist.guardar_ficheiro()
                sist.backup_dados()
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
                grafo.desenhar_grafo(GRAFO, FREGUESIAS)

            elif op == 2:
                grafo.mostrar_pontos_criticos()
                print(len(grafo.vertices))
            elif op == 3:
                grafo.testar_caminho()
            elif op == 4:
                grafo.obter_itinerario()
            elif op == 5:
                ponto_interesse = input("Digite o ponto de interesse: ")
                grafo.obter_arvore_rotas_carro(ponto_interesse, GRAFO, ponto_interesse)
            elif op == 6:
                ponto_interesse = input("Introduza um ponto para fazer a travessia em largura: ")
                grafo.bfs(ponto_interesse)
            elif op == 7:
                ponto_interesse = input("Introduza um ponto para fazer a travessia em profundidade: ")
                grafo.dfs(ponto_interesse)
            elif op == 8:

                grafo.interromper_via()
            elif op == 9:
                origem = input("origem: ")
                destino = input("destino: ")
                grafo.shortest_path(origem, destino)
                print(grafo.shortest_path(origem,destino))
            elif op == 0:
                voltar_menu_principal = True
        except ValueError:
            print("Opção inválida. Tente outra vez.")


