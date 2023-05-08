from Sistema import adicionar_ponto_interesse, alterar_ponto_interesse, pesquisar_ponto_interesse, \
    mostrar_pontos_interesse, FICHEIRO
from PontoInteresse import PontoInteresse


def opcoes_menu():
    print("----------------------------------------------------------------")
    print(" 1 - Ver todos os pontos de interesse")
    print(" 2 - Adicionar um ponto de interesse")
    print(" 3 - Alterar um ponto de interesse")
    print(" 4 - Pesquisar pontos de interesse ")
    print(" 5 - Avaliar visita a ponto de interesse")
    print(" 6 - Consultar estátisticas de visitas aos pontos de interesse")
    print(" 7 - Obter sugestões de visitas a pontos de interesse ")
    print(" 9 - Sair ")


def menu():
    fim = False
    while not fim:
        opcoes_menu()
        print("----------------------------------------------------------------")
        op = int(input("Opção: "))
        if op == 1:
            mostrar_pontos_interesse()
        elif op == 2:
            adicionar_ponto_interesse()
        elif op == 3:
            alterar_ponto_interesse()
        elif op == 4:
            pesquisar_ponto_interesse()
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 0:
            fim = True


menu()
