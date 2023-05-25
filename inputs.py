import json


def ler_grafo(filename: str):
    dic = {}
    with open(filename, "r") as file:
        data = json.load(file)
        for item in data:
            designacao = item.get("designacao")
            dic[designacao] = {}
    return dic
