def obter_ponto_interesse(linked_list, acao):
    """
    Busca um ponto de interesse na lista ligada.
    :param linked_list: A lista ligada contendo os pontos de interesse.
    :param acao: Ação a ser realizada (por exemplo, "alterar" ou "apagar").
    :return: O ponto de interesse encontrado ou None se não for encontrado.
    """
    if acao == "alterar":
        mensagem = "Insira a designação do ponto de interesse que pretende alterar: "
    elif acao == "apagar":
        mensagem = "Insira a designação do ponto de interesse que pretende apagar: "
    else:
        mensagem = "Insira a designação do ponto de interesse: "

    designacao = input(mensagem).capitalize()
    current = linked_list.head
    while current:
        ponto_interesse = PontoInteresse(**current.data)
        if ponto_interesse.get_designacao().lower() == designacao.lower():
            return ponto_interesse
        current = current.next
    return None


ponto_interesse = obter_ponto_interesse(linked_list, "alterar")


ponto_interesse = obter_ponto_interesse(linked_list, "apagar")
