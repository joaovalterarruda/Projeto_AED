class PontoInteresse:
    def __init__(self, designacao: str, morada: str, latitude: str, longitude: str, categoria_ponto: str,
                 acessibilidade: str, classificacao: 0, visitas=0) -> None:
        self._designacao: str = designacao
        self._morada: str = morada
        self._latitude: str = latitude
        self._longitude: str = longitude
        self._categoria_ponto: str = categoria_ponto
        self._acessibilidade: str = acessibilidade
        self._classificacao: int = classificacao
        self._visitas: int = visitas

    def __str__(self) -> str:
        return "Designacao: " + str(self._designacao) + "Morada:  " + str(self._morada) \
            + "Latitude:  " + str(self._latitude) + "Longitude: " + str(self._longitude) + "Categoria Turismo: " + \
            str(self._categoria_ponto) + "Acessiblidade" + str(self._acessibilidade) + "Classificacao" \
            + str(self._classificacao) + "Visitas" + str(self._visitas)

    def __dict__(self):
        return {
            "designacao": self._designacao,
            "morada": self._morada,
            "latitude": self._latitude,
            "longitude": self._longitude,
            "categoria_ponto": self._categoria_ponto,
            "acessibilidade": self._acessibilidade,
            "classificacao": self._classificacao,
            "visitas": self._visitas
        }

    def get_designacao(self) -> str:
        return self._designacao

    def get_morada(self) -> str:
        return self._morada

    def get_latitude(self) -> str:
        return self._latitude

    def get_longitude(self) -> str:
        return self._longitude

    def get_categoria_turismo(self) -> str:
        return self._categoria_ponto

    def get_acessibilidade(self) -> str:
        return self._acessibilidade

    def get_classificao(self) -> int:
        return self._classificacao

    def get_visitas(self) -> int:
        return self._visitas

    def set_categoria_turismo(self, categoria):
        self._categoria_ponto = categoria

    def set_acessibilidade(self, acessibilidade):
        self._acessibilidade = acessibilidade
