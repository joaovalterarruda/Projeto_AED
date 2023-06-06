from projeto_aed.sistema.LinkedList import LinkedList
import json
import shutil
from projeto_aed.sistema.Grafo import Grafo


def ler_ficheiro(nome_ficheiro):
    """
    Lê o conteúdo de um ficheiro JSON e cria uma lista ligada com os dados lidos.

    Args: nome_ficheiro (str): O nome do ficheiro a ser lido.
    Returns:
    LinkedList: A lista ligada criada a partir dos dados do ficheiro.
    """

    linked_list = LinkedList()
    with open(nome_ficheiro, 'r', encoding="UTF-8") as file:
        conteudo = json.load(file)
        for item in conteudo:
            linked_list.add(item)
        print("Ficheiro " + nome_ficheiro + " carregado com sucesso.")
    return linked_list


def guardar_ficheiro(dados, nome_ficheiro):
    """
    Guardar os dados num ficheiro.json
    :param dados: Os dados a serem guardados no arquivo. Deve ser uma lista de itens.
    :param nome_ficheiro: O nome do arquivo de destino. Deve ter a extensão json.
    :return:
    """
    linked_list = LinkedList()
    for item in dados:
        linked_list.add(item)
    conteudo = linked_list.to_list()
    with open(nome_ficheiro, 'w', encoding="UTF-8") as file:
        json.dump(conteudo, file, indent=4)
    print("Ficheiro " + nome_ficheiro + " guardado com sucesso.")


def fazer_backup(nome_ficheiro):
    """
    Faz uma cópia de ‘backup’ do ficheiro JSON.
    :param nome_ficheiro: O nome do ficheiro a ser feito o ‘backup’.
    :return:
    """
    nome_backup = nome_ficheiro + ".backup"
    shutil.copy(nome_ficheiro, nome_backup)
    print("Backup do ficheiro " + nome_ficheiro + " criado com sucesso.")


def carregar_dados_grafo(file):
    """
    Carrega dos dados de um determinado ficheiro json
    :param file: Nome do ficheiro json
    :return:
    """
    grafo = Grafo()

    with open(file) as f:
        dados = json.load(f)

    for vertice in dados['vertices']:
        nome = vertice['nome']
        latitude = vertice['latitude']
        longitude = vertice['longitude']
        grafo.adicionar_vertice(nome, latitude, longitude)

    for aresta in dados['arestas']:
        origem = aresta['origem']
        destino = aresta['destino']
        peso = aresta['peso']
        grafo.adicionar_aresta(origem, destino, peso)

    return grafo
