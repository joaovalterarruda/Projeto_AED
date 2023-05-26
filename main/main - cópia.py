
from projeto_aed.sistema.Sistema import ler_ficheiro, guardar_ficheiro, fazer_backup, adicionar_ponto_interesse, alterar_ponto_interesse, \
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
    print(" 2 - Ver pontos de interesse")
    print(" 3 - Adicionar ponto de interesse")
    print(" 4 - Alterar ponto de interesse")
    print(" 5 - Apagar ponto de interesse ")
    print(" 6 - Pesquisar pontos de interesse ")
    print(" 7 - Avaliar visita")
    print(" 8 - Consultar estatísticas de visitas")
    print(" 9 - Obter sugestões de visitas")
    print(" 0 - Sair ")


def menu():
    fim = False
    while not fim:
        opcoes_menu()
        print("-" * 72)
        try:
            op = int(input("Opção: "))
            if op == 1:
                print("\n""\033[4mPonta Delgada\033[0m"
                      "\nPonta Delgada é uma cidade portuguesa localizada na ilha de São Miguel\ne pertencente"
                      " à Região Autónoma dos Açores com uma população\nde 46 102 habitantes."
                      " Ponta Delgada é a capital económica da \nRegião Autónoma dos Açores "
                      "e a maior cidade desta região.")
                input("\nPrima Enter para voltar ao menu principal.")

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
