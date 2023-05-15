from PontoInteresse import PontoInteresse
import json
from math import radians, cos, sin, sqrt, atan2
from LinkedList import LinkedList

FICHEIRO = "pontos_interesse.json"
categorias_turismo = ("Praia", "Monumento", "Museu", "Parque", "Miradouro", "Outros")
classificacao = ("1", "2", "3", "4")


def ler_ficheiro(nome_ficheiro):
    linked_list = LinkedList()
    with open(nome_ficheiro, 'r') as file:
        conteudo = json.load(file)
        for item in conteudo:
            linked_list.add(item)
    return linked_list


def guardar_ficheiro(dados, ficheiro):
    linked_list = LinkedList()
    for item in dados:
        linked_list.add(item)
    conteudo = linked_list.to_list()
    with open(ficheiro, 'w') as file:
        json.dump(conteudo, file, indent=4)


def mostrar_pontos_interesse(linked_list):
    current = linked_list.head
    while current:
        ponto_interesse = PontoInteresse(**current.data)  ## Serve para não estar a passar os parâmetros todos um a um..
        print("Designação:", ponto_interesse.get_designacao())
        print("Morada:", ponto_interesse.get_morada())
        print("Latitude:", ponto_interesse.get_latitude())
        print("Longitude:", ponto_interesse.get_longitude())
        print("Categoria:", ponto_interesse.get_categoria_turismo())
        print("Acessibilidade:", ponto_interesse.get_acessibilidade())
        print("Classificação:", ponto_interesse.get_classificacao())
        print("\n")
        opcao = input("Enter para continuar ou 'c' para cancelar e voltar ao menu. ")
        if opcao.lower() == 'c':
            return  # retorna para o menu
        current = current.next



def adicionar_ponto_interesse(linked_list):  # RF01 OK
    designacao = str(input("Insira uma designação do ponto de interesse: "))

    # Verificar se a designação já existe na lista de pontos de interesse
    current = linked_list.head
    while current:
        ponto_interesse = PontoInteresse(**current.data)
        if ponto_interesse.get_designacao() == designacao:
            print("O ponto de interesse com esta designação já foi usado!")
            designacao = str(input("Insira uma designação do ponto de interesse: "))
            current = linked_list.head
        else:
            current = current.next

    morada = str(input("Insira a morada do ponto de interesse: "))
    latitude = int(input("Insira a latitude do ponto de interesse: "))
    longitude = int(input("Insira a longitude do ponto de interesse: "))
    while True:
        categoria_ponto = str(input("Insira a categoria do ponto de interesse: "))
        if categoria_ponto not in categorias_turismo:
            print("Categoria inválida! As que se encontram disponíveis são:", categorias_turismo)
        else:
            break
    acessibilidade = str(input("Insira a acessibilidade do ponto de interesse: "))
    novo_ponto_interesse = PontoInteresse(designacao, morada, latitude, longitude, categoria_ponto,
                                          acessibilidade, classificacao=0, visitas=0)

    linked_list.add(novo_ponto_interesse.__dict__())

    print("\n")
    print("Ponto interesse criado com sucesso!")
    print("\n")



def alterar_ponto_interesse(linked_list):  # RF02 ok
    designacao = input("Insira a designação do ponto de interesse que pretende alterar: ")
    current = linked_list.head
    while current:
        ponto_interesse = PontoInteresse(**current.data)
        if ponto_interesse.get_designacao() == designacao:
            print("O que pretende alterar?")
            print("1- Categoria")
            print("2- Acessibilidade")
            escolha = int(input("Insira a sua escolha (1) ou (2): "))
            if escolha == 1:
                nova_categoria = input(f"Insira a nova categoria ({', '.join(categorias_turismo)}): ")
                if nova_categoria in categorias_turismo:
                    ponto_interesse.set_categoria_turismo(nova_categoria)
                    linked_list.update(current.data, ponto_interesse.__dict__())
                    print("Categoria do ponto de interesse alterada com sucesso!")
                else:
                    print("Categoria inválida!")
                    return
            elif escolha == 2:
                nova_acessibilidade = input("Insira a nova acessibilidade: ")
                ponto_interesse.set_acessibilidade(nova_acessibilidade)
                linked_list.update(current.data, ponto_interesse.__dict__())
                print("Acessibilidade do ponto de interesse alterada com sucesso!")
            else:
                print("Escolha inválida!")
                return
            break
        current = current.next
    else:
        print("Não existe nenhum ponto de interesse com essa designação!")
        return

    print("\n")
    print("Ponto de interesse alterado com sucesso!")
    print("\n")



def pesquisar_ponto_interesse(linked_list):  # RF03 ok
    categoria = input("Insira a categoria que pretende pesquisar: ")
    resultados = []
    current = linked_list.head
    while current:
        ponto_interesse = PontoInteresse(**current.data)
        if ponto_interesse.get_categoria_turismo() == categoria:
            resultados.append(ponto_interesse)
        current = current.next

    # Ordena os pontos de interesse por ordem alfabética da designação (utilizando Insertion Sort)
    for i in range(1, len(resultados)):
        j = i - 1
        while j >= 0 and resultados[j].get_designacao() > resultados[j + 1].get_designacao():
            resultados[j], resultados[j + 1] = resultados[j + 1], resultados[j]
            j -= 1

    # Mostrar os resultados da pesquisa
    if len(resultados) > 0:
        print(f"Resultados para a categoria {categoria}:")
        for ponto in resultados:
            print("-----")
            print(f"Designação: {ponto.get_designacao()}")
            print(f"Morada: {ponto.get_morada()}")
            print(f"Latitude: {ponto.get_latitude()}")
            print(f"Longitude: {ponto.get_longitude()}")
            print(f"Categoria: {ponto.get_categoria_turismo()}")
            input("Prima Enter para continuar.")
    else:
        print(f"Não foram encontrados pontos de interesse para a categoria {categoria}!")


def avaliar_visita(linked_list, nome_ponto, classificar):  ############# falta completar RF04
    current = linked_list.head

    # É feita a procura pela designação
    ponto = None
    while current:
        if current.data.get('designacao') == nome_ponto:
            ponto = current.data
            break
        current = current.next

    # Caso não encontre o ponto de interesse
    if ponto is None:
        print("Ponto de interesse não encontrado!")
        return

    # Incrementa o número de visitas
    ponto['visitas'] += 1

    # Atualizar a classificação
    if classificar in range(1, 5):
        ponto['classificacao'] = (ponto.get('classificacao', 0) + classificar) / ponto['visitas']
    else:
        print("Classificação inválida! Insira um número de 1 a 4")
        return

    print("A classificação de {} foi avaliada com sucesso!".format(nome_ponto))



def consultar_estatisticas(linked_list):  # RF05 ok
    opcao = input("Escolha a ordenação (1 - Nome, 2 - Número de Visitas, 3 - Classificação Média): ")

    if opcao == "1":
        ordenar_por = "designacao"
    elif opcao == "2":
        ordenar_por = "visitas"
    elif opcao == "3":
        ordenar_por = "classificacao"
    else:
        print("Opção inválida!")
        return

    pontos_turisticos = linked_list.to_list()

    # Ordenar os pontos de interesse com base na opção selecionada
    pontos_turisticos.sort(key=lambda ponto: ponto.get(ordenar_por), reverse = (ordenar_por in ["visitas", "classificacao"]))

    print("Estatísticas das Visitas nos Pontos Turísticos: ")
    for ponto in pontos_turisticos:
        num_visitas = ponto.get('visitas')
        classificacao_media = ponto.get('classificacao')
        print(f"Designação: {ponto.get('designacao')}")
        print(f"Número de Visitantes: {num_visitas}")
        print(f"Classificação Média: {classificacao_media}\n")

        opcao = input("Enter para continuar ou 'c' para cancelar e voltar ao menu. ")
        if opcao.lower() == 'c':
            return  # retorna para o menu




def formula_de_haversine(coord1, coord2):
    r = 6371  # raio da Terra em km
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) * sin(dlat / 2) + cos(radians(lat1)) \
        * cos(radians(lat2)) * sin(dlon / 2) * sin(dlon / 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = r * c
    return d


# coord1 = (37.4359, -25)
# coord2 = (37.752745973611226, -25)
# distancia = formula_de_haversine(coord1, coord2)
# print(distancia)


def sugestao_pontos_interesse(latitude, longitude, ficheiro, distancia_maxima):
    pontos = ler_ficheiro(ficheiro)
    pontos_perto = []
    for ponto in pontos:
        if isinstance(ponto, dict) and 'latitude' in ponto and 'longitude' in ponto and 'visitas' in ponto:
            coord_ponto = (ponto['latitude'], ponto['longitude'])
            coord_localizacao = (latitude, longitude)
            dist = formula_de_haversine(coord_ponto, coord_localizacao)
            if dist < distancia_maxima:
                pontos_perto.append(ponto)
    pontos_perto = sorted(pontos_perto, key=lambda x: x['visitas'], reverse=True)
    return pontos_perto

# pontos_sugeridos = sugestao_pontos_interesse(38.7072, -9.1362, FICHEIRO, 5)
# print("Pontos sugeridos:")
# for ponto in pontos_sugeridos:
#     print(ponto)
