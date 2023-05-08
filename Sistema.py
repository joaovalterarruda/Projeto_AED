from PontoInteresse import PontoInteresse
import os
import json


def adicionar_ponto_interesse():
    nome_ficheiro = "pontos_interesse.json"
    # Verificar se o ficheiro existe e não está vazio
    if os.path.exists(nome_ficheiro) and os.path.getsize(nome_ficheiro) > 0:
        # Carregar os pontos de interesse existentes do ficheiro
        with open(nome_ficheiro, "r") as f:
            pontos_interesse = json.load(f)
    else:
        pontos_interesse = []

    designacao = str(input("Insira uma designacao do ponto de interesse: "))
    morada = str(input("Insira a morada do ponto de interesse: "))
    latitude = int(input("Insira a latitude do ponto de interesse: "))
    longitude = int(input("Insira a longitude do ponto de interesse: "))
    categoria_ponto = int(input("Insira a categoria do ponto de interesse: (0) a (10) "))
    acessibilidade = str(input("Insira a acessiblidade do ponto de interesse? "))

    novo_ponto_interesse = {
        "designacao": designacao,
        "morada": morada,
        "latitude": latitude,
        "longitude": longitude,
        "categoria_ponto": categoria_ponto,
        "acessibilidade": acessibilidade
    }

    # Adicionar o novo ponto de interesse à lista
    pontos_interesse.append(novo_ponto_interesse)

    # Guardar todos os pontos de interesse no ficheiro
    with open(nome_ficheiro, "w") as f:
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
                nova_categoria = int(input("Insira a nova categoria (0 a 10): "))
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



