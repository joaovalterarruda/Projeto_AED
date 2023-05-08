from PontoInteresse import PontoInteresse
import os
import json

FICHEIRO = "pontos_interesse.json"
categorias_turismo = ("Praia", "Monumento", "Museu", "Parque", "Miradouro", "Outros")


def ler_ficheiro(nome_ficheiro):
    with open(nome_ficheiro, 'r') as file:
        conteudo = json.load(file)
    return conteudo


def guardar_ficheiro(dados, ficheiro):
    with open(ficheiro, 'w') as file:
        json.dump(dados, file, indent=4)


def mostrar_pontos_interesse():
    pontos_interesse = ler_ficheiro(FICHEIRO)
    for ponto in pontos_interesse:
        print("Designação:", ponto["designacao"])
        print("Morada:", ponto["morada"])
        print("Latitude:", ponto["latitude"])
        print("Longitude:", ponto["longitude"])
        print("Categoria:", ponto["categoria_ponto"])
        print("Acessibilidade:", ponto["acessibilidade"])
        print("Classificação:", ponto["classificacao"])
        print("\n")
        input("Prima qualquer tecla para continuar")


def adicionar_ponto_interesse():  # RF01
    pontos_interesse = ler_ficheiro(FICHEIRO)
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
    guardar_ficheiro(novo_ponto_interesse,FICHEIRO)
    print("\n")
    print("Ponto interesse criado com sucesso!!")
    print("\n")


def alterar_ponto_interesse():  # RF02
    nome_interesse = ler_ficheiro(FICHEIRO)
    designacao = input("Insira a designação do ponto de interesse que pretende alterar: ")
    for ponto in nome_interesse:
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
    guardar_ficheiro(nome_interesse, FICHEIRO)
    print("\n")
    print("Ponto de interesse alterado com sucesso!")
    print("\n")


def pesquisar_ponto_interesse():  # RF03
    nome_interesse = ler_ficheiro(FICHEIRO)
    categoria = str(input("Insira a categoria que pretende pesquisar: "))
    resultados = []
    for ponto in nome_interesse:
        if ponto["categoria_ponto"] == categoria:
            resultados.append(ponto)

    # Ordena os pontos de interesse por ordem alfabética da designação (utilizando Insertion Sort)
    for i in range(1, len(resultados)):
        j = i - 1
        while j >= 0 and resultados[j]["designacao"] > resultados[j + 1]["designacao"]:
            resultados[j], resultados[j + 1] = resultados[j + 1], resultados[j]
            j -= 1

    # Mostrar os resultados da pesquisa
    if len(resultados) > 0:
        print(f"Resultados para a categoria {categoria}:")
        for ponto in resultados:
            print("-----")
            print(f"Designação: {ponto['designacao']}")
            print(f"Morada: {ponto['morada']}")
            print(f"Latitude: {ponto['latitude']}")
            print(f"Longitude: {ponto['longitude']}")
            print(f"Categoria: {ponto['categoria_ponto']}")
            input("Prima qualquer tecla para continuar.")
    else:
        print(f"Não foram encontrados pontos de interesse para a categoria {categoria}!")


def avaliar_visita(nome_arquivo, nome_ponto_interesse, nova_classificacao):
    # Ler o conteúdo do ficheiro.json para uma variável
    dados = ler_ficheiro(nome_arquivo)

    # Percorrer a lista de pontos de interesse e atualizar o contador de visitas e a classificação
    encontrado = False
    for ponto in dados['pontos_interesse']:
        if ponto['nome'] == nome_ponto_interesse:
            ponto['visitas'] += 1
            ponto['classificacao'] = nova_classificacao
            encontrado = True
            break

    # Caso o ponto de interesse não seja encontrado, imprimir mensagem de erro
    if not encontrado:
        print("Ponto de interesse não encontrado!")
    else:
        # Guardar os dados atualizados no ficheiro.json
        guardar_ficheiro(dados, nome_arquivo)
