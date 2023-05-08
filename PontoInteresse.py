class PontoInteresse:
    def __init__(self, designacao: str, morada: str, latitude: int, longitude: int, _categoria_ponto: str, acessibilidade: str) -> None:
        self._designacao: str = designacao
        self._morada: str = morada
        self._latitude: int = latitude
        self._longitude: int = longitude
        self._categoria_ponto: str = _categoria_ponto
        self._acessibilidade: str = acessibilidade

    def __str__(self) -> str:
        return "Designacao: " + str(self._designacao) + "Morada:  " + str(self._morada) \
            + "Latitude:  " + str(self._latitude) + "Longitude: " + str(self._longitude) + "Categoria Turismo: " + \
            str(self._categoria_ponto) + "Acessiblidade" + str(self._acessibilidade)

    def get_designacao(self) -> str:
        return self._designacao

    def get_morada(self) -> str:
        return self._morada

    def get_latitude(self) -> int:
        return self._latitude

    def get_longitude(self) -> int:
        return self._longitude

    def get_categoria_turismo(self) -> str:
        return self._categoria_ponto

    def get_acessibilidade(self) -> str:
        return self._acessibilidade