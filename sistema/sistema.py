import json
import math
import time
import webbrowser

import networkx as nx
from matplotlib import pyplot as plt

from sistema.PontoInteresse import PontoInteresse
from sistema.localize import obter_localizacao_atual
from sistema.constantes import categorias_turismo, LAT, LONG, FRASE_INPUT, GRAFO, FREGUESIAS, FICHEIRO
from sistema.algortimos import merge_sort
from sistema.json import carregar_dados_grafo, ler_ficheiro, guardar_ficheiro, fazer_backup


def mostrar_info_conselho():
    print("\n", "\033[4mPonta Delgada\033[0m"
                "\nPonta Delgada é uma cidade portuguesa localizada na ilha de São Miguel\ne pertencente"
                " à Região Autónoma dos Açores com uma população\nde 46 102 habitantes."
                " Ponta Delgada é a capital económica da \nRegião Autónoma dos Açores "
                "e a maior cidade desta região.")
    print("\nLinks úteis:")
    print("1. Website Visit Azores: https://www.visitazores.com")
    print("2. Câmara de Ponta Delgada: https://www.cm-pontadelgada.pt/")
    print("3. Mais informação: https://pt.wikipedia.org/wiki/Ponta_Delgada")
    while True:
        link_op = input(
            "Selecione uma das opções para abrir no navegador ou pressione (ENTER) para sair: ")
        if link_op.isdigit():
            link_op = int(link_op)
            if link_op == 1:
                webbrowser.open("https://www.visitazores.com")
                break
            elif link_op == 2:
                webbrowser.open("https://www.cm-pontadelgada.pt/")
                break
            elif link_op == 3:
                webbrowser.open("https://pt.wikipedia.org/wiki/Ponta_Delgada")
                break
            else:
                print("Opção inválida. Por favor, selecione um número válido.")
        else:
            break


class Sistema:
    def __init__(self):
        self.linked_list = ler_ficheiro(FICHEIRO)
        self.grafo = carregar_dados_grafo(GRAFO)

    def guardar_ficheiro(self):
        guardar_ficheiro(self.linked_list, FICHEIRO)

    def backup_dados(self):
        fazer_backup(FICHEIRO)

    def mostrar_pontos_interesse(self):
        """
        Mostra os pontos de interesse de uma lista ligada, ordenados por critério definido pelo utilizador.
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
            time.sleep(2)
            return

        print("\n\033[4mLISTA DE PONTOS DE INTERESSE\033[0m:")
        pontos_interesse = []
        current = self.linked_list.head

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
            print("------------")
            print("Designação:", ponto_interesse.get_designacao())
            print("Morada:", ponto_interesse.get_morada())
            print(LAT, ponto_interesse.get_latitude())
            print(LONG, ponto_interesse.get_longitude())
            print("Categoria:", ponto_interesse.get_categoria_turismo())
            print("Acessibilidade física:", ponto_interesse.get_acessibilidade_fis())
            print("Acessibilidade geográfica:", ponto_interesse.get_acessibilidade_geo())
            print("Classificação:", ponto_interesse.get_classificacao())
            opcao = input(FRASE_INPUT)
            if opcao.lower() == 'c':
                return  # retorna para o menu

    def adicionar_ponto_interesse(self):
        """
        Adiciona um novo ponto de interesse à LinkedList.
        """
        designacao = str(input("Insira uma designação do ponto de interesse: "))

        # Verificar se a designação já existe na lista de pontos de interesse
        current = self.linked_list.head
        while current:
            ponto_interesse = PontoInteresse(**current.data)
            if ponto_interesse.get_designacao() == designacao:
                print("O ponto de interesse com esta designação já foi usado!")
                designacao = str(input("Insira uma designação do ponto de interesse: "))
                current = self.linked_list.head
            else:
                current = current.next

        morada = str(input("Insira a morada do ponto de interesse: "))

        latitude = input("Insira a latitude do ponto de interesse: ")
        latitude = float(latitude.replace(",", "."))

        longitude = input("Insira a longitude do ponto de interesse: ")
        longitude = float(longitude.replace(",", "."))

        while True:
            categoria_ponto = input(f"Insira a categoria do ponto de interesse ({', '.join(categorias_turismo)}): ")
            categoria_ponto = categoria_ponto.lower()
            if categoria_ponto not in categorias_turismo:
                print("Categoria inválida! As que se encontram disponíveis são:", categorias_turismo)
            else:
                break

        acessibilidade_fis = str(
            input("Insira a acessibilidade física do ponto de interesse (rampa, elevador, etc.): "))
        acessibilidade_geo = str(input(
            "Insira a acessibilidade geográfica do ponto de interesse (parque de estacionamento, transp. públicos, "
            "ciclovia, etc.): "))

        novo_ponto_interesse = PontoInteresse(designacao, morada, latitude, longitude, categoria_ponto,
                                              acessibilidade_fis, acessibilidade_geo, classificacao=0, visitas=0)

        self.linked_list.add(novo_ponto_interesse.__dict__())

        print("\n")
        print("Ponto de interesse criado com sucesso!")
        print("\n")

    def obter_ponto_interesse(self):
        """
        Obtém um ponto de interesse na lista ligada.
        """
        designacao = input("Insira a designação do ponto de interesse que pretende alterar: ").capitalize()
        current = self.linked_list.head
        while current:
            ponto_interesse = PontoInteresse(**current.data)
            if ponto_interesse.get_designacao().lower() == designacao.lower():
                return ponto_interesse, current.data
            current = current.next
        return None, None

    def alterar_ponto_interesse(self):
        """
        Altera as informações de um ponto de interesse existente na lista ligada.
        """
        ponto_interesse, data = self.obter_ponto_interesse()

        if ponto_interesse is None:
            print("Não existe nenhum ponto de interesse com essa designação!")
            time.sleep(2)
            return

        while True:
            print(f"O que pretende alterar no ponto de interesse '{ponto_interesse.get_designacao()}'?")
            print("--------")
            print("1 - Categoria")
            print("2 - Acessibilidade física")
            print("3 - Acessibilidade geográfica")
            print("4 - Morada")
            print("5 - Latitude")
            print("6 - Longitude")
            print("0 - Voltar ao menu principal")
            escolha = int(input("Insira a sua escolha (0 a 6): "))

            if escolha == 0:
                break

            elif escolha == 1:
                nova_categoria = input(f"Insira a nova categoria ({', '.join(categorias_turismo)}): ").lower()
                if nova_categoria in categorias_turismo:
                    ponto_interesse.set_categoria_turismo(nova_categoria)
                    self.linked_list.update(data, ponto_interesse.__dict__())
                    print("Categoria do ponto de interesse alterada com sucesso!\n")
                else:
                    print("Categoria inválida!")
                    return
            elif escolha == 2:
                nova_acessibilidade_fis = input("Insira a nova acessibilidade física: ").capitalize()
                ponto_interesse.set_acessibilidade_fis(nova_acessibilidade_fis)
                self.linked_list.update(data, ponto_interesse.__dict__())
                print("Acessibilidade física do ponto de interesse alterada com sucesso!\n")
            elif escolha == 3:
                nova_acessibilidade_geo = input("Insira a nova acessibilidade geográfica: ").capitalize()
                ponto_interesse.set_acessibilidade_geo(nova_acessibilidade_geo)
                self.linked_list.update(data, ponto_interesse.__dict__())
                print("Acessibilidade geográfica do ponto de interesse alterada com sucesso!\n")
            elif escolha == 4:
                nova_morada = input("Insira a nova morada do ponto de interesse: ")
                ponto_interesse.set_morada(nova_morada)
                self.linked_list.update(data, ponto_interesse.__dict__())
                print("Morada do ponto de interesse alterada com sucesso!\n")
            elif escolha == 5:
                nova_latitude = input("Insira a nova latitude do ponto de interesse: ")
                nova_latitude = float(nova_latitude.replace(",", "."))
                ponto_interesse.set_latitude(nova_latitude)
                self.linked_list.update(data, ponto_interesse.__dict__())
                print("Latitude do ponto de interesse alterada com sucesso!\n")
            elif escolha == 6:
                nova_longitude = input("Insira a nova longitude do ponto de interesse: ")
                nova_longitude = float(nova_longitude.replace(",", "."))
                ponto_interesse.set_longitude(nova_longitude)
                self.linked_list.update(data, ponto_interesse.__dict__())
                print("Longitude do ponto de interesse alterada com sucesso!\n")
            else:
                print("Escolha inválida!")
                return

        print("Ponto de interesse alterado com sucesso!")
        print("\n")
        time.sleep(2)

    def apagar_ponto_interesse(self):
        """
        Remove um ponto de interesse da lista ligada.
        """
        designacao = input("Insira a designação do ponto de interesse que pretende apagar: ").capitalize()
        current = self.linked_list.head
        previous = None
        while current:
            ponto_interesse = PontoInteresse(**current.data)
            if ponto_interesse.get_designacao().lower() == designacao.lower():
                if previous is None:
                    self.linked_list.head = current.next
                else:
                    previous.next = current.next
                print("Ponto de interesse apagado com sucesso!")
                time.sleep(2)
                return
            previous = current
            current = current.next

        print("Não existe nenhum ponto de interesse com essa designação!")
        time.sleep(2)

    def pesquisar_ponto_interesse(self):
        """
        Pesquisa pontos de interesse com base numa palavra-chave e/ou categoria.
        """
        palavra_chave = input("Insira a palavra-chave para a pesquisa (ou deixe em branco para ignorar): ")
        categoria = input(
            f"Insira a categoria para a pesquisa ({', '.join(categorias_turismo)}) (ou deixe em branco para ignorar): ")

        resultados = []
        current = self.linked_list.head
        while current:
            ponto_interesse = PontoInteresse(**current.data)

            if palavra_chave.lower() in ponto_interesse.get_designacao().lower():
                if categoria.lower() == ponto_interesse.get_categoria_turismo().lower() or not categoria:
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
            print(f"Resultados para a palavra-chave '{palavra_chave}' e categoria '{categoria}':")
            for ponto in resultados:
                print("------------")
                print(f"Designação: {ponto.get_designacao()}")
                print(f"Morada: {ponto.get_morada()}")
                print(f"Latitude: {ponto.get_latitude()}")
                print(f"Longitude: {ponto.get_longitude()}")
                print(f"Categoria: {ponto.get_categoria_turismo()}")
                print("------------")
                input("Prima Enter para continuar.")
                print("\n")
        else:
            print(
                f"Não foram encontrados pontos de interesse para a palavra-chave '{palavra_chave}' e categoria '{categoria}"
                f"'!")
            time.sleep(2)

    def avaliar_visita(self):
        """
        Avalia uma visita a um ponto de interesse, atualizando o número de visitas e a classificação média.
        """
        nome_ponto = str(input("Introduza o nome do ponto a avaliar: ")).capitalize()
        classificar = int(input("Introduza a classificação que pretende dar ao ponto:"
                                "\n1- Nada satisfeito\n2- Pouco satisfeito\n3- Satisfeito\n4- Muito "
                                "Satisfeito\n", ))

        current = self.linked_list.head

        # Verificar se o ponto de interesse existe
        ponto = None
        while current:
            if current.data.get('designacao').lower() == nome_ponto.lower():
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

    def consultar_estatisticas(self):
        """
        Consulta estatísticas sobre os pontos turísticos, exibindo as informações de cada ponto de interesse
        e um gráfico com a distribuição das classificações para cada ponto turístico.
        """
        pontos_turisticos = self.linked_list.to_list()

        print("Estatísticas das Visitas nos Pontos Turísticos: ")

        classificacoes = []  # Lista para armazenar todas as classificações

        for ponto in pontos_turisticos:
            num_visitas = ponto.get('visitas')
            classificacao = ponto.get('classificacao')
            print(f"Designação: {ponto.get('designacao')}")
            print(f"Número de Visitantes: {num_visitas}")
            print(f"Classificação: {classificacao}\n")

            classificacoes.append(classificacao)  # Adiciona a classificação à lista

        if classificacoes:
            # Gera o gráfico de distribuição das classificações
            labels = ['Nada Satisfeito', 'Pouco Satisfeito', 'Satisfeito', 'Muito Satisfeito']
            count = [classificacoes.count(i) for i in
                     range(1, 5)]  # Conta as ocorrências para cada classificação de 1 a 4

            plt.pie(count, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')  # Assegura que o gráfico é desenhado como um círculo.
            plt.title('Classificações Pontos de Interesse')
            plt.show()
        else:
            print("Não há dados suficientes para gerar o gráfico.")

        opcao = input(FRASE_INPUT)
        if opcao.lower() == 'c':
            return  # retorna para o menu

    def haversine(self, lat1, lon1, lat2, lon2) -> float:
        """
        Calcula a distância em km entre dois pontos na Terra utilizando a fórmula de Haversine.
        Os pontos são especificados em latitude e longitude.
        :param lat1: Latitude do primeiro ponto.
        :param lon1: Longitude do primeiro ponto.
        :param lat2: Latitude do segundo ponto.
        :param lon2: Longitude do segundo ponto.
        :return:
        """
        # Raio médio da Terra em km
        radius = 6371
        # Converter graus para radianos
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        # Diferença das latitudes e longitudes
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        # Fórmula de Haversine
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = radius * c

        return distance

    def obter_localizacao(self):
        localizacao = obter_localizacao_atual()
        if localizacao:
            latitude, longitude = localizacao
            print("Sua localização atual:")
            print(LAT, latitude)
            print(LONG, longitude)
            return latitude, longitude
        else:
            latitude = float(input("Digite a sua latitude: "))
            longitude = float(input("Digite a sua longitude: "))
            return latitude, longitude

    def sugestao_pontos_interesse(self):
        """
        Retorna uma lista de pontos de interesse próximos a uma localização específica, numa distância máxima.
        """
        latitude, longitude = self.obter_localizacao()

        distancia_maxima = float(input("Digite a distância máxima de pesquisa: "))

        pontos_perto = []
        current = self.linked_list.head
        while current:
            ponto = current.data
            if isinstance(ponto, dict) and 'latitude' in ponto and 'longitude' in ponto:
                coord_ponto = (float(ponto['latitude']), float(ponto['longitude']))
                coord_localizacao = (latitude, longitude)
                dist = self.haversine(coord_ponto[0], coord_ponto[1], coord_localizacao[0], coord_localizacao[1])
                if dist < distancia_maxima:
                    pontos_perto.append(ponto)
            current = current.next
        if len(pontos_perto) == 0:
            print("\n")
            print("Não foram encontrados pontos de interesse dentro da distância máxima introduzida.")
            time.sleep(2)
        else:
            # Ordenar pontos_perto em ordem decrescente do número de visitas usando Merge Sort
            merge_sort(pontos_perto, 'visitas', reverse=True)

            print("----------------------------------------------------------------")
            print("\033[4mPontos sugeridos\033[0m:")
            for ponto in pontos_perto:
                print("Designação:", ponto['designacao'])
                print("Morada:", ponto['morada'])
                print("Acessibilidade física: ", ponto['acessibilidade_fis'])
                print("Acessibilidade geográfica: ", ponto['acessibilidade_geo'])
                print(LAT, ponto['latitude'])
                print(LONG, ponto['longitude'])
                print("Visitas:", ponto['visitas'])
                print("------------")
                opcao = input("Enter para continuar ou (C) para cancelar e voltar ao menu. ")
                print("\n")
                if opcao.lower() == 'c':
                    return
        return pontos_perto

    def inserir_pontos_interesse_json(self):
        """
        Insere dados dos pontos de interesse como vértices num arquivo JSON.
        """
        current = self.linked_list.head
        vertices = []

        while current:
            ponto = current.data
            ponto = {
                "nome": ponto['designacao'],  # Acesso aos valores do dicionário usando chaves
                "latitude": ponto['latitude'],
                "longitude": ponto['longitude']
            }
            vertices.append(ponto)
            current = current.next

        pontos_int = {"vertices": vertices}
        # Salvar os pontos de interesse num arquivo JSON
        with open("grafo_teste.json", "w") as file:
            json.dump(pontos_int, file, indent=4)

        print("Dados dos pontos de interesse foram salvos em pontos_interesse.json.")

    # Segunda Entrega

    def pontos_criticos(self):
        # Identificar pontos críticos
        pontos_criticos = self.grafo.identificar_pontos_criticos()

        # Calcular centralidade de proximidade (closeness) para cada vértice
        centralidade_closeness = self.grafo.calcular_proximidade_closeness()

        # Exibir descrições dos pontos críticos, valores de closeness e graus
        for vertice, valor_closeness in centralidade_closeness.items():
            descricao = "Ponto crítico" if vertice in pontos_criticos else "Não crítico"
            grau_interno = self.grafo.calcular_centralidade_grau_interno(vertice)
            grau_externo = self.grafo.calcular_centralidade_grau_externo(vertice)

            print(f"Vértice: {vertice}")
            print(f"Descrição: {descricao}")
            print(f"Centralidade de Closeness: {valor_closeness}")
            print(f"Grau Interno: {grau_interno}")
            print(f"Grau Externo: {grau_externo}")
            print()
