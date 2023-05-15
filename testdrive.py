import webbrowser

from Sistema import ler_ficheiro, guardar_ficheiro, fazer_backup, adicionar_ponto_interesse, alterar_ponto_interesse, \
    apagar_ponto_interesse, pesquisar_ponto_interesse, \
    mostrar_pontos_interesse, FICHEIRO, avaliar_visita, consultar_estatisticas, sugestao_pontos_interesse


def opcoes_menu():
    print("\u250C" + "\u2500" * 70 + "\u2510")
    print(
        "\u2502" + "\033[1;36m" + "\t \t \t \t \t \tConcelho de Ponta Delgada\t \t \t \t \t   " + "\033[0m" + "\u2502")
    print(
        "\u2502" + "\033[1;36m" + "\t \t \t \t \t \t   Pontos de Interesse\t \t \t \t \t \t   " + "\033[0m" + "\u2502")
    print("\u2514" + "\u2500" * 70 + "\u2518")
    print("-" * 72)
    print(" 0 - Ponta Delgada, Historia e Cultura")
    print(" 1 - Ver todos os pontos de interesse")
    print(" 2 - Adicionar um ponto de interesse")
    print(" 3 - Alterar um ponto de interesse")
    print(" 4 - Apagar ponto de interesse ")
    print(" 5 - Pesquisar pontos de interesse ")
    print(" 6 - Avaliar visita a ponto de interesse")
    print(" 7 - Consultar estátisticas de visitas aos pontos de interesse")
    print(" 8 - Obter sugestões de visitas a pontos de interesse ")
    print(" 9 - Sair ")


def menu():
    fim = False
    while not fim:
        opcoes_menu()
        print("-" * 72)
        try:
            op = int(input("Opção: "))
            if op == 0:
                webbrowser.open("http://www.visitpontadelgada.pt/ponta-delgada/informacoes-sobre-ponta-delgada")
            elif op == 1:
                mostrar_pontos_interesse(linkedlist)
            elif op == 2:
                adicionar_ponto_interesse(linkedlist)
            elif op == 3:
                alterar_ponto_interesse(linkedlist)
            elif op == 4:
                apagar_ponto_interesse(linkedlist)
            elif op == 5:
                pesquisar_ponto_interesse(linkedlist)
            elif op == 6:
                nome_ponto = str(input("Introduza o nome do ponto a avaliar: "))
                classificar = int(input("Introduza a classificação que pretende dar ao ponto:"
                                        "\n1- Nada satisfeito\n2- Pouco satisfeito\n3- Satisfeito\n4- Muito Satisfeito\n", ))
                avaliar_visita(linkedlist, nome_ponto, classificar)
            elif op == 7:
                consultar_estatisticas(linkedlist)
            elif op == 8:
                latitude = float(input("Digite a sua latitude: "))
                longitude = float(input("Digite a sua longitude: "))
                distancia = float(input("Digite a distância máxima de pesquisa: "))
                sugestao_pontos_interesse(latitude, longitude, linkedlist, distancia)
            elif op == 9:
                guardar_ficheiro(linkedlist, FICHEIRO)
                fazer_backup(FICHEIRO)
                fim = True
        except ValueError:
            print("Opção inválida. Tente outra vez.")

if __name__ == '__main__':
    #Carrega o ficheiro JSON para a LinkedList no inicio do programa
    linkedlist = ler_ficheiro("pontos_interesse.json")
    fazer_backup(FICHEIRO)
    menu()
