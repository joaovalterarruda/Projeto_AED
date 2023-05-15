from Sistema import ler_ficheiro, guardar_ficheiro, adicionar_ponto_interesse, alterar_ponto_interesse, pesquisar_ponto_interesse, \
    mostrar_pontos_interesse, FICHEIRO, avaliar_visita, consultar_estatisticas, sugestao_pontos_interesse



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
        try:
            op = int(input("Opção: "))
            if op == 1:
                mostrar_pontos_interesse(linkedlist)
            elif op == 2:
                adicionar_ponto_interesse(linkedlist)
            elif op == 3:
                alterar_ponto_interesse(linkedlist)
            elif op == 4:
                pesquisar_ponto_interesse(linkedlist)
            elif op == 5:
                nome_ponto = str(input("Introduza o nome do ponto a avaliar: "))
                classificar = int(input("Introduza a classificação que pretende dar ao ponto:"
                                        "\n1- Nada satisfeito\n2- Pouco satisfeito\n3- Satisfeito\n4- Muito Satisfeito\n",))
                avaliar_visita(linkedlist, nome_ponto, classificar)
            elif op == 6:
                consultar_estatisticas(linkedlist)
            elif op == 7:
                latitude = float(input("Digite a latitude: "))
                longitude = float(input("Digite a longitude: "))
                distancia = float(input("Digite a distância máxima: "))

                pontos_sugeridos = sugestao_pontos_interesse(latitude, longitude, linkedlist, distancia)

                if len(pontos_sugeridos) == 0:
                    print("Não foram encontrados pontos de interesse dentro da distância máxima introduzida.")
                else:
                    print("----------------------------------------------------------------")
                    print("Pontos sugeridos:")
                    for ponto in pontos_sugeridos:
                        print("Designação:", ponto['designacao'])
                        print("Morada:", ponto['morada'])
                        print("Latitude:", ponto['latitude'])
                        print("Longitude:", ponto['longitude'])
                        print("Visitas:", ponto['visitas'])
                        opcao = input("Enter para continuar ou (C) para cancelar e voltar ao menu. ")
                        print("\n")
                        if opcao.lower() == 'c':
                            return
            elif op == 0:
                guardar_ficheiro(linkedlist, FICHEIRO)
                fim = True


        except ValueError:
            print("Opção inválida. Tente outra vez.")


linkedlist = ler_ficheiro("pontos_interesse.json")
menu()
