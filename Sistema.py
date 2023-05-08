from PontoInteresse import PontoInteresse
import os
import json

FICHEIRO = "pontos_interesse.json"


def mostrar_pontos_interesse():
    with open(FICHEIRO, "r") as f:
        pontos_interesse = json.load(f)
        for ponto in pontos_interesse:
            print("Designação:", ponto["designacao"])
            print("Morada:", ponto["morada"])
            print("Latitude:", ponto["latitude"])
            print("Longitude:", ponto["longitude"])
            print("Categoria:", ponto["categoria_ponto"])
            print("Acessibilidade:", ponto["acessibilidade"])
            print("Classificação:", ponto["classificacao"])
            print("\n")


def adicionar_ponto_interesse():
    # Verificar se o ficheiro existe e não está vazio
    if os.path.exists(FICHEIRO) and os.path.getsize(FICHEIRO) > 0:
        # Carregar os pontos de interesse existentes do ficheiro
        with open(FICHEIRO, "r") as f:
            pontos_interesse = json.load(f)
    else:
        pontos_interesse = []
    designacao = str(input("Insira uma designacao do ponto de interesse: "))
    morada = str(input("Insira a morada do ponto de interesse: "))
    latitude = int(input("Insira a latitude do ponto de interesse: "))
    longitude = int(input("Insira a longitude do ponto de interesse: "))
    categoria_ponto = str(input("Insira a categoria do ponto de interesse: "))
    acessibilidade = str(input("Insira a acessiblidade do ponto de interesse? "))

    novo_ponto_interesse = {
        "designacao": designacao,
        "morada": morada,
        "latitude": latitude,
        "longitude": longitude,
        "categoria_ponto": categoria_ponto,
        "acessibilidade": acessibilidade,
        "classificacao": 0
    }

    # Adicionar o novo ponto de interesse à lista
    pontos_interesse.append(novo_ponto_interesse)

    # Guardar todos os pontos de interesse no ficheiro
    with open(FICHEIRO, "w") as f:
        json.dump(pontos_interesse, f, indent=4)

    print("\n")
    print("Ponto interesse criado com sucesso!!")
    print("\n")


def alterar_ponto_interesse():
    nome_ficheiro = "pontos_interesse.json"
    # Verificar se o ficheiro existe e não está vazio
    if os.path.exists(nome_ficheiro) and os.path.getsize(nome_ficheiro) > 0:
        # Carregar os pontos de interesse existentes do ficheiro
        with open(nome_ficheiro, "r") as f:
            pontos_interesse = json.load(f)
    else:
        print("Não há pontos de interesse registados!")
        return

    designacao = input("Insira a designação do ponto de interesse que pretende alterar: ")

    for ponto in pontos_interesse:
        if ponto["designacao"] == designacao:
            print("O que pretende alterar?")
            print("1- Categoria")
            print("2- Acessibilidade")
            escolha = int(input("Insira a sua escolha (1) ou (2): "))

            if escolha == 1:
                nova_categoria = str(input("Insira a nova categoria: "))
                ponto["categoria_ponto"] = nova_categoria
                print("Categoria do ponto de interesse alterada com sucesso!")
            elif escolha == 2:
                nova_acessibilidade = input("Insira a nova acessibilidade: ")
                ponto["acessibilidade"] = nova_acessibilidade
                print("Acessibilidade do ponto de interesse alterada com sucesso!")
            else:
                print("Escolha inválida!")
            break
    else:
        print("Não existe nenhum ponto de interesse com essa designação!")
        return

    # Guardar todos os pontos de interesse no ficheiro
    with open(nome_ficheiro, "w") as f:
        json.dump(pontos_interesse, f, indent=4)

    print("\n")
    print("Ponto de interesse alterado com sucesso!")
    print("\n")


def pesquisar_ponto_interesse():
    if os.path.exists(FICHEIRO) and os.path.getsize(FICHEIRO) > 0:
        with open(FICHEIRO, "r") as f:
            pontos_interesse = json.load(f)
    else:
        print("Não existem pontos de interesse registados!")
        return

    categoria = str(input("Insira a categoria que pretende pesquisar: "))
    resultados = []

    for ponto in pontos_interesse:
        if ponto["categoria_ponto"] == categoria:
            resultados.append(ponto)

    # Ordenar os pontos de interesse por ordem alfabética da designação (utilizando Insertion Sort)
    for i in range(1, len(resultados)):
        j = i - 1
        while j >= 0 and resultados[j]["designacao"] > resultados[j+1]["designacao"]:
            resultados[j], resultados[j+1] = resultados[j+1], resultados[j]
            j -= 1

    # Exibir os resultados
    if len(resultados) > 0:
        print(f"Resultados para a categoria {categoria}:")
        for ponto in resultados:
            print("-----")
            print(f"Designação: {ponto['designacao']}")
            print(f"Morada: {ponto['morada']}")
            print(f"Latitude: {ponto['latitude']}")
            print(f"Longitude: {ponto['longitude']}")
            print(f"Categoria: {ponto['categoria_ponto']}")
            print("-----")
    else:
        print(f"Não foram encontrados pontos de interesse para a categoria {categoria}!")


def avaliar_ponto_interesse(pontos_interesse):
    # Mostrar a lista de pontos de interesse disponíveis
    print("Pontos de interesse disponíveis:")
    for i, ponto in enumerate(pontos_interesse):
        print(f"{i}: {ponto['designacao']}")

    # Pedir ao utilizador que selecione o ponto de interesse a avaliar
    ponto_index = int(input("Selecione o ponto de interesse a avaliar: "))

    # Incrementar o contador de visitas
    pontos_interesse[ponto_index]['visitas'] += 1

    # Pedir ao utilizador que insira a sua classificação da experiência
    classificacao = int(input("Insira a sua classificação da experiência (1-4): "))

    # Verificar se a classificação é válida
    while classificacao < 1 or classificacao > 4:
        classificacao = int(input("Insira uma classificação válida (1-4): "))

    # Atualizar a classificação do ponto de interesse
    pontos_interesse[ponto_index]['classificacoes'].append(classificacao)

    # Mostrar a mensagem de sucesso
    print("Avaliação registada com sucesso!")

