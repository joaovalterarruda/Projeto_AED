

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
    print(" 1 - Ponta Delgada, História e Cultura")
    print(" 2 - Ver todos os pontos de interesse")
    print(" 3 - Adicionar um ponto de interesse")
    print(" 4 - Alterar um ponto de interesse")
    print(" 5 - Apagar ponto de interesse ")
    print(" 6 - Pesquisar pontos de interesse ")
    print(" 7 - Avaliar visita a ponto de interesse")
    print(" 8 - Consultar estatísticas de visitas aos pontos de interesse")
    print(" 9 - Obter sugestões de visitas a pontos de interesse ")
    print(" 0 - Sair ")


def menu():
    fim = False
    while not fim:
        opcoes_menu()
        print("-" * 72)
        try:
            op = int(input("Opção: "))
            if op == 1:
                print("Ponta Delgada é uma cidade portuguesa localizada na ilha de São Miguel\ne pertencente"
                      " à Região Autónoma dos Açores com uma população\nde 46 102 habitantes."
                      " Ponta Delgada é a capital económica da \nRegião Autónoma dos Açores "
                      "e a maior cidade desta região.")
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
                nome_ponto = str(input("Introduza o nome do ponto a avaliar: "))
                classificar = int(input("Introduza a classificação que pretende dar ao ponto:"
                                        "\n1- Nada satisfeito\n2- Pouco satisfeito\n3- Satisfeito\n4- Muito Satisfeito\n", ))
                avaliar_visita(linkedlist, nome_ponto, classificar)
            elif op == 8:
                consultar_estatisticas(linkedlist)
            elif op == 9:
                latitude = float(input("Digite a sua latitude: "))
                longitude = float(input("Digite a sua longitude: "))
                distancia = float(input("Digite a distância máxima de pesquisa: "))
                sugestao_pontos_interesse(latitude, longitude, linkedlist, distancia)
            elif op == 0:
                guardar_ficheiro(linkedlist, FICHEIRO)
                fazer_backup(FICHEIRO)
                fim = True
                print("Obrigado por utilizar o nosso programa. Até breve!")
        except ValueError:
            print("Opção inválida. Tente outra vez.")



if __name__ == '__main__':
    # Carrega o ficheiro JSON para a LinkedList no inicio do programa
    linkedlist = ler_ficheiro(FICHEIRO)
    fazer_backup(FICHEIRO)
    menu()
