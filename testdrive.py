from Sistema import adicionar_ponto_interesse, alterar_ponto_interesse, pesquisar_ponto_interesse, \
    mostrar_pontos_interesse, FICHEIRO, avaliar_visita, consultar_estatisticas, sugestao_pontos_interesse
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
    print(" 0 - Sair ")


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
            nome_ponto = str(input("Introduza o nome do ponto a avaliar: "))
            classificar = int(input("Introduza a classificação que pretende dar ao ponto:"
                                    "\n1- Nada satisfeito\n2- Pouco satisfeito\n3- Satisfeito\n4- Muito Satisfeito\n",))
            avaliar_visita(FICHEIRO, nome_ponto, classificar)
        elif op == 6:
            consultar_estatisticas()
        elif op == 7:
            latitude = int(input("Introduza a latitude: "))
            longitude = int(input("Introduza a longitude: "))
            distancia = int(input("Introduza a distancia máxima: "))
            pontos_sugeridos = sugestao_pontos_interesse(latitude, longitude, FICHEIRO, distancia)
            print("Pontos sugeridos:")
            for ponto in pontos_sugeridos:
                print(ponto)
        elif op == 0:
            fim = True


menu()
