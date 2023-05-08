from Sistema import adicionar_ponto_interesse, alterar_ponto_interesse, pesquisar_ponto_interesse
from projeto_aed.PontoInteresse import PontoInteresse


def opcoes_menu():
    print("----------------------------------------------------------------")
    print(" 1 - Adicionar um ponto de interesse")
    print(" 2 - Alterar um ponto de interesse")
    print(" 3 - Pesquisar pontos de interesse ")
    print(" 4 - Assinalar e avaliar visita a ponto de interesse")
    print(" 5 - Consultar estátisticas de visitas aos pontos de interesse")
    print(" 6 - Obter sugestões de visitas a pontos de interesse ")
    print(" 0 - Sair ")


def menu():
    fim = False
    while not fim:
        opcoes_menu()
        print("----------------------------------------------------------------")
        op = int(input("Opção: "))
        if op == 1:
            adicionar_ponto_interesse()
        elif op == 2:
            alterar_ponto_interesse()
        elif op == 3:
            pesquisar_ponto_interesse()
        elif op == 4:
            pass  # COMPLETAR
        elif op == 5:
            pass  # COMPLETAR
        elif op == 6:
            pass  # COMPLETAR
        elif op == 0:
            fim = True


menu()
