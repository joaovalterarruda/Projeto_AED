
def merge_sort(arr, key, reverse=False):
    """
    Ordena uma lista usando o algoritmo de ordenação merge sort.
    :param arr: A lista a ser ordenada.
    :param key: A chave do dicionário a ser usada como critério de ordenação.
    :param reverse: Indica se a ordenação deve ser em ordem decrescente. O padrão é False (ordem crescente).
    :return:
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
    Combina duas listas ordenadas numa única lista ordenada.
    :param left: Primeira lista ordenada.
    :param right: Segunda lista ordenada.
    :param key: Chave do dicionário a ser usada como critério de ordenação.
    :param reverse: Indica se a ordenação deve ser em ordem decrescente. O padrão é False (ordem crescente).
    :return:
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
