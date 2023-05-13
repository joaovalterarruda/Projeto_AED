from PontoInteresse import PontoInteresse
import json
from math import radians, cos, sin, sqrt, atan2

FICHEIRO = "pontos_interesse.json"
categorias_turismo = ("Praia", "Monumento", "Museu", "Parque", "Miradouro", "Outros")
classificacao = ("1", "2", "3", "4")


def ler_ficheiro(nome_ficheiro):
    with open(nome_ficheiro, 'r') as file:
        conteudo = json.load(file)
    return conteudo


def guardar_ficheiro(dados, ficheiro):
    with open(ficheiro, 'w') as file:
        json.dump(dados, file, indent=4)


def mostrar_pontos_interesse():
    for ponto in ler_ficheiro(FICHEIRO):
        ponto_interesse = PontoInteresse(**ponto)  ## Serve para não estar a passar os parâmetros todos um a um..
        print("Designação:", ponto_interesse.get_designacao())
        print("Morada:", ponto_interesse.get_morada())
        print("Latitude:", ponto_interesse.get_latitude())
        print("Longitude:", ponto_interesse.get_longitude())
        print("Categoria:", ponto_interesse.get_categoria_turismo())
        print("Acessibilidade:", ponto_interesse.get_acessibilidade())
        print("Classificação:", ponto_interesse.get_classificacao())
        print("\n")
        input("Prima Enter para continuar")


def adicionar_ponto_interesse():  # RF01 OK
    pontos_interesse = ler_ficheiro(FICHEIRO)
    designacao = str(input("Insira uma designacao do ponto de interesse: "))

    # Verificar se a designação já existe na lista de pontos de interesse
    existe_designacao = [ponto["designacao"] for ponto in pontos_interesse]
    while designacao in existe_designacao:
        print("O ponto de interesse com esta designacao já foi usado!")
        designacao = str(input("Insira uma designacao do ponto de interesse: "))

    morada = str(input("Insira a morada do ponto de interesse: "))
    latitude = int(input("Insira a latitude do ponto de interesse: "))
    longitude = int(input("Insira a longitude do ponto de interesse: "))
    while True:
        categoria_ponto = str(input("Insira a categoria do ponto de interesse: "))
        if categoria_ponto not in categorias_turismo:
            print("Categoria inválida! As que se encontram disponíveis são:", categorias_turismo)
        else:
            break
    acessibilidade = str(input("Insira a acessiblidade do ponto de interesse? "))
    novo_ponto_interesse = PontoInteresse(designacao, morada, latitude, longitude, categoria_ponto,
                                          acessibilidade, classificacao=0, visitas=0)

    # Adicionar o novo ponto de interesse à lista
    pontos_interesse.append(novo_ponto_interesse.__dict__())
    # Guardar todos os pontos de interesse no ficheiros
    with open(FICHEIRO, "w") as f:
        json.dump(pontos_interesse, f, indent=4)
    print("\n")
    print("Ponto interesse criado com sucesso!!")
    print("\n")


def alterar_ponto_interesse():  # RF02 ok
    pontos_interesse = ler_ficheiro(FICHEIRO)
    designacao = input("Insira a designação do ponto de interesse que pretende alterar: ")
    for ponto in pontos_interesse:
        if ponto["designacao"] == designacao:
            print("O que pretende alterar?")
            print("1- Categoria")
            print("2- Acessibilidade")
            escolha = int(input("Insira a sua escolha (1) ou (2): "))
            if escolha == 1:
                nova_categoria = input(f"Insira a nova categoria ({', '.join(categorias_turismo)}): ")
                # join para juntar os elementos da lista categorias_turismo
                if nova_categoria in categorias_turismo:
                    ponto["categoria_turismo"] = nova_categoria
                    print("Categoria do ponto de interesse alterada com sucesso!")
                else:
                    print("Categoria inválida!")
                    return
            elif escolha == 2:
                nova_acessibilidade = input("Insira a nova acessibilidade: ")
                ponto["acessibilidade"] = nova_acessibilidade
                print("Acessibilidade do ponto de interesse alterada com sucesso!")
            else:
                print("Escolha inválida!")
                return
            break
    else:
        print("Não existe nenhum ponto de interesse com essa designação!")
        return

    # Guardar todos os pontos de interesse no ficheiro
    guardar_ficheiro(pontos_interesse, FICHEIRO)
    print("\n")
    print("Ponto de interesse alterado com sucesso!")
    print("\n")


def pesquisar_ponto_interesse():  # RF03 ok
    pontos_interesse = ler_ficheiro(FICHEIRO)
    categoria = input("Insira a categoria que pretende pesquisar: ")
    resultados = [PontoInteresse(**p) for p in pontos_interesse if p.get('categoria_ponto') == categoria]

    # Ordena os pontos de interesse por ordem alfabética da designação (utilizando Insertion Sort)
    for i in range(1, len(resultados)):
        j = i - 1
        while j >= 0 and resultados[j]._designacao > resultados[j + 1]._designacao:
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


def avaliar_visita(ficheiro, nome_ponto, classificar):  ############# falta completar RF04
    pontos_interesse = ler_ficheiro(ficheiro)

    # É feita a procura pela designação
    ponto = None
    for i in pontos_interesse:
        if i.get('designacao') == nome_ponto:
            ponto = i
            break

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

    # Atualizar o arquivo com os dados
    with open(ficheiro, "w") as f:
        json.dump(pontos_interesse, f, indent=4)

    print("A classificação a {} foi avaliada com sucesso!".format(nome_ponto))


def consultar_estatisticas():  # RF05 ok
    pontos_interesse = ler_ficheiro(FICHEIRO)
    pontos_turisticos = []
    for ponto_dict in pontos_interesse:
        ponto = PontoInteresse(
            designacao=ponto_dict.get("designacao"),
            morada=ponto_dict.get("morada"),
            latitude=ponto_dict.get("latitude"),
            longitude=ponto_dict.get("longitude"),
            categoria_ponto=ponto_dict.get("categoria_ponto"),
            acessibilidade=ponto_dict.get("acessibilidade"),
            classificacao=ponto_dict.get("classificacao"),
            visitas=ponto_dict.get("visitas")
        )
        pontos_turisticos.append(ponto)

    print("Estatísticas das Visitas nos Pontos Turísticos: ")
    for ponto in pontos_turisticos:
        num_visitas = ponto.get_visitas()
        classificacao_media = ponto.get_classificacao()
        print(f"Designação: {ponto.get_designacao()}")
        print(f"Número de Visitantes: {num_visitas}")
        print(f"Classificação Média: {classificacao_media}\n")


def formula_de_haversine(coord1, coord2):
    R = 6371  # raio da Terra em km
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) * sin(dlat / 2) + cos(radians(lat1)) \
        * cos(radians(lat2)) * sin(dlon / 2) * sin(dlon / 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = R * c
    return d


def sugestao_pontos_interesse(latitude, longitude, ficheiro, distancia_maxima):
    pontos = ler_ficheiro(ficheiro)
    pontos_perto = []
    for ponto in pontos:
        if isinstance(ponto, PontoInteresse):
            coord_ponto = (ponto.get_latitude(), ponto.get_longitude())
            coord_localizacao = (latitude, longitude)
            dist = formula_de_haversine(coord_ponto, coord_localizacao)
            if dist <= distancia_maxima:
                pontos_perto.append(ponto)
    pontos_perto = sorted(pontos_perto, key=lambda x: x.get_visitas(), reverse=True)
    return pontos_perto

