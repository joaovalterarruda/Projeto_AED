import math
import shutil
from PontoInteresse import PontoInteresse
import json
from LinkedList import LinkedList

FICHEIRO = "pontos_interesse.json"
categorias_turismo = ("natureza", "cultural", "aventura", "gastronomia", "praia", "outros")
classificacao = ("1", "2", "3", "4")

FRASE_INPUT = "Enter para continuar ou (C) para cancelar e voltar ao menu. "

def ler_ficheiro(nome_ficheiro):
    """
        Lê o conteúdo de um ficheiro JSON e cria uma lista ligada com os dados lidos.

        Args:
            nome_ficheiro (str): O nome do ficheiro a ser lido.

        Returns:
            LinkedList: A lista ligada criada a partir dos dados do ficheiro.
        """

    linked_list = LinkedList()
    with open(nome_ficheiro, 'r') as file:
        conteudo = json.load(file)
        for item in conteudo:
            linked_list.add(item)
        print("Ficheiro " + nome_ficheiro + " carregado com sucesso.")
    return linked_list



def guardar_ficheiro(dados, nome_ficheiro):
    linked_list = LinkedList()
    for item in dados:
        linked_list.add(item)
    conteudo = linked_list.to_list()
    with open(nome_ficheiro, 'w') as file:
        json.dump(conteudo, file, indent=4)
    print("Ficheiro " + nome_ficheiro + " guardado com sucesso.")


def fazer_backup(nome_ficheiro):
    """
        Faz uma cópia de backup do ficheiro JSON.

        Args:
            nome_ficheiro (str): O nome do ficheiro a ser feito o backup.

        Returns:
            None
    """
    nome_backup = nome_ficheiro + ".backup"
    shutil.copy(nome_ficheiro, nome_backup)
    print("Backup do ficheiro " + nome_ficheiro + " criado com sucesso.")


def mostrar_pontos_interesse(linked_list):
    """
        Mostra os pontos de interesse de uma lista ligada, ordenados por critério definido pelo utilizador.

        Args:
            linked_list (LinkedList): A lista ligada contendo os pontos de interesse.

        Returns:
            None
        """
    opcao_ordem = input("Ordenar por: (D)esignação, (C)ategoria ou (A)cessibilidade: ")

    if opcao_ordem.lower() == 'd':
        atributo_ordenacao = 'get_designacao'
    elif opcao_ordem.lower() == 'c':
        atributo_ordenacao = 'get_categoria_turismo'
    elif opcao_ordem.lower() == 'a':
        atributo_ordenacao = 'get_acessibilidade_fis'
    else:
        print("Opção inválida.")
        return

    pontos_interesse = []
    current = linked_list.head

    while current:
        ponto_interesse = PontoInteresse(**current.data)
        pontos_interesse.append(ponto_interesse)
        current = current.next

    # Algoritmo Insertion Sort para ordenar os pontos de interesse
    for i in range(1, len(pontos_interesse)):
        key = pontos_interesse[i]
        j = i - 1
        while j >= 0 and getattr(pontos_interesse[j], atributo_ordenacao)() > getattr(key, atributo_ordenacao)():
            pontos_interesse[j + 1] = pontos_interesse[j]
            j -= 1
        pontos_interesse[j + 1] = key

    for ponto_interesse in pontos_interesse:
        print("\n")
        print("Designação:", ponto_interesse.get_designacao())
        print("Morada:", ponto_interesse.get_morada())
        print("Latitude:", ponto_interesse.get_latitude())
        print("Longitude:", ponto_interesse.get_longitude())
        print("Categoria:", ponto_interesse.get_categoria_turismo())
        print("Acessibilidade física:", ponto_interesse.get_acessibilidade_fis())
        print("Acessibilidade geográfica:", ponto_interesse.get_acessibilidade_geo())
        print("Classificação:", ponto_interesse.get_classificacao())
        print("\n")
        opcao = input(FRASE_INPUT)
        if opcao.lower() == 'c':
            return  # retorna para o menu


def adicionar_ponto_interesse(linked_list):  # RF01 OK
    """
       Adiciona um novo ponto de interesse à LinkedList.

       Args:
           linked_list (LinkedList): A lista ligada onde o ponto de interesse será adicionado.

       Returns:
           None
       """
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
    latitude = float(input("Insira a latitude do ponto de interesse: "))
    longitude = float(input("Insira a longitude do ponto de interesse: "))
    while True:
        categoria_ponto = input(f"Insira a categoria do ponto de interesse ({', '.join(categorias_turismo)}): ")
        if categoria_ponto not in categorias_turismo:
            print("Categoria inválida! As que se encontram disponíveis são:", categorias_turismo)
        else:
            break
    acessibilidade_fis = str(input("Insira a acessibilidade fisica do ponto de interesse (rampa, elevador, etc.): "))
    acessibilidade_geo = str(input("Insira a acessibilidade geográfica do ponto de interesse (parque de estacionamento, transp. públicos, ciclovia, etc.): "))
    novo_ponto_interesse = PontoInteresse(designacao, morada, latitude, longitude, categoria_ponto,
                                          acessibilidade_fis, acessibilidade_geo, classificacao=0, visitas=0)

    linked_list.add(novo_ponto_interesse.__dict__())

    print("\n")
    print("Ponto interesse criado com sucesso!")
    print("\n")



def alterar_ponto_interesse(linked_list): # RF02 ok
    """
        Altera as informações de um ponto de interesse existente na lista ligada.

        Args:
            linked_list (LinkedList): A lista ligada contendo os pontos de interesse.

        Returns:
            None
        """
    designacao = input("Insira a designação do ponto de interesse que pretende alterar: ")
    current = linked_list.head
    while current:
        ponto_interesse = PontoInteresse(**current.data)
        if ponto_interesse.get_designacao() == designacao:
            print("O que pretende alterar?")
            print("1- Categoria")
            print("2- Acessibilidade física")
            print("3- Acessibilidade geográfica")
            escolha = int(input("Insira a sua escolha (1), (2) ou (3): "))
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
                nova_acessibilidade_fis = input("Insira a nova acessibilidade fisica: ")
                ponto_interesse.set_acessibilidade_fis(nova_acessibilidade_fis)
                linked_list.update(current.data, ponto_interesse.__dict__())
                print("Acessibilidade fisica do ponto de interesse alterada com sucesso!")
            elif escolha == 3:
                nova_acessibilidade_geo = input("Insira a nova acessibilidade geográfica: ")
                ponto_interesse.set_acessibilidade_geo(nova_acessibilidade_geo)
                linked_list.update(current.data, ponto_interesse.__dict__())
                print("Acessibilidade geográfica do ponto de interesse alterada com sucesso!")
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


def apagar_ponto_interesse(linked_list):
    """
        Remove um ponto de interesse da lista ligada.

        Args:
            linked_list (LinkedList): A lista ligada contendo os pontos de interesse.

        Returns:
            None
        """
    designacao = input("Insira a designação do ponto de interesse que pretende apagar: ")
    current = linked_list.head
    previous = None
    while current:
        ponto_interesse = PontoInteresse(**current.data)
        if ponto_interesse.get_designacao() == designacao:
            if previous is None:
                linked_list.head = current.next
            else:
                previous.next = current.next
            print("Ponto de interesse apagado com sucesso!")
            return
        previous = current
        current = current.next

    print("Não existe nenhum ponto de interesse com essa designação!")


def pesquisar_ponto_interesse(linked_list):  # RF03 ok
    """
        Pesquisa pontos de interesse com base na categoria especificada.

        Args:
            linked_list (LinkedList): A lista ligada contendo os pontos de interesse.

        Returns:
            None
        """

    categoria = input(f"Insira a categoria que pretende pesquisar: ({', '.join(categorias_turismo)}): ")
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
        print("\n")
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


def avaliar_visita(linked_list, nome_ponto, classificar):
    """
       Avalia uma visita a um ponto de interesse, atualizando o número de visitas e a classificação média.

       Args:
           linked_list (LinkedList): A lista ligada contendo os pontos de interesse.
           nome_ponto (str): O nome do ponto de interesse a ser avaliado.
           classificar (int): A classificação atribuída à visita (1 a 4).

       Returns:
           None
       """
    current = linked_list.head

    # Verificar se o ponto de interesse existe
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
    """
       Consulta estatísticas sobre os pontos turísticos, como ordenar por nome, número de visitas ou classificação média.

       Args:
           linked_list (LinkedList): A lista ligada contendo os pontos de interesse.

       Returns:
           None
       """

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

        opcao = input(FRASE_INPUT)
        if opcao.lower() == 'c':
            return  # retorna para o menu




def haversine(lat1, lon1, lat2, lon2) -> float:
    """
        Calcula a distância em km entre dois pontos na Terra utilizando a fórmula de Haversine.
        Os pontos são especificados em latitude e longitude.

        Args:
            lat1 (float): Latitude do primeiro ponto.
            lon1 (float): Longitude do primeiro ponto.
            lat2 (float): Latitude do segundo ponto.
            lon2 (float): Longitude do segundo ponto.

        Returns:
            float: A distância entre os dois pontos em km.
        """


    # Raio médio da Terra em km
    radius = 6371
    # Converter graus para radianos
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    # Diferença das latitudes e longitudes
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    # Fórmula de Haversine
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c

    return distance





def sugestao_pontos_interesse(latitude: float, longitude: float, linked_list, distancia_maxima: float):
    """
        Retorna uma lista de pontos de interesse próximos a uma localização específica, dentro de uma distância máxima.

        Args:
            latitude (float): Latitude da localização de referência.
            longitude (float): Longitude da localização de referência.
            linked_list (LinkedList): A lista ligada contendo os pontos de interesse.
            distancia_maxima (float): A distância máxima em km.

        Returns:
            List[Dict]: Uma lista de dicionários representando os pontos de interesse próximos.
        """

    pontos_perto = []
    current = linked_list.head
    while current:
        ponto = current.data
        if isinstance(ponto, dict) and 'latitude' in ponto and 'longitude' in ponto:
            coord_ponto = (float(ponto['latitude']), float(ponto['longitude']))
            coord_localizacao = (latitude, longitude)
            dist = haversine(coord_ponto[0], coord_ponto[1], coord_localizacao[0], coord_localizacao[1])
            if dist < distancia_maxima:
                pontos_perto.append(ponto)
        current = current.next
    if len(pontos_perto) == 0:
        print("\n")
        print("Não foram encontrados pontos de interesse dentro da distância máxima introduzida.")
    else:
        # Ordenar pontos_perto em ordem decrescente do número de visitas usando Merge Sort
        merge_sort(pontos_perto, 'visitas', reverse=True)

        print("----------------------------------------------------------------")
        print("Pontos sugeridos:")
        for ponto in pontos_perto:
            print("Designação:", ponto['designacao'])
            print("Morada:", ponto['morada'])
            print("Latitude:", ponto['latitude'])
            print("Longitude:", ponto['longitude'])
            print("Visitas:", ponto['visitas'])
            opcao = input("Enter para continuar ou (C) para cancelar e voltar ao menu. ")
            print("\n")
            if opcao.lower() == 'c':
                return
    return pontos_perto


def merge_sort(arr, key, reverse=False):
    """
        Ordena uma lista usando o algoritmo de ordenação merge sort.

        Args:
            arr (List[Dict]): A lista a ser ordenada.
            key (str): A chave do dicionário a ser usada como critério de ordenação.
            reverse (bool): Indica se a ordenação deve ser em ordem decrescente. O padrão é False (ordem crescente).

        Returns:
            List[Dict]: A lista ordenada.
        """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left, key, reverse)
    right = merge_sort(right, key, reverse)

    return merge(left, right, key, reverse)


def merge(left, right, key, reverse=False):
    """
        Combina duas listas ordenadas em uma única lista ordenada.

        Args:
            left (List[Dict]): A primeira lista ordenada.
            right (List[Dict]): A segunda lista ordenada.
            key (str): A chave do dicionário a ser usada como critério de ordenação.
            reverse (bool): Indica se a ordenação deve ser em ordem decrescente. O padrão é False (ordem crescente).

        Returns:
            List[Dict]: A lista combinada e ordenada.
        """

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if reverse:
            if left[i][key] >= right[j][key]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if left[i][key] <= right[j][key]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result






