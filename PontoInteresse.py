class PontoInteresse:
    """
    Representa um ponto de interesse turístico.

    Args:
        designacao (str): A designação do ponto de interesse.
        morada (str): O endereço do ponto de interesse.
        latitude (float): A latitude do ponto de interesse.
        longitude (float): A longitude do ponto de interesse.
        categoria_ponto (str): A categoria do ponto de interesse.
        acessibilidade_fis (str): A acessibilidade física do ponto de interesse.
        acessibilidade_geo (str): A acessibilidade geográfica do ponto de interesse.
        classificacao (int): A classificação do ponto de interesse.
        visitas (int): O número de visitas do ponto de interesse.

    Attributes:
        _designacao (str): A designação do ponto de interesse.
        _morada (str): O endereço do ponto de interesse.
        _latitude (float): A latitude do ponto de interesse.
        _longitude (float): A longitude do ponto de interesse.
        _categoria_ponto (str): A categoria do ponto de interesse.
        _acessibilidade_fis (str): A acessibilidade física do ponto de interesse.
        _acessibilidade_geo (str): A acessibilidade geográfica do ponto de interesse.
        _classificacao (int): A classificação do ponto de interesse.
        _visitas (int): O número de visitas do ponto de interesse.
    """

    def __init__(self, designacao: str, morada: str, latitude: float, longitude: float, categoria_ponto: str,
                 acessibilidade_fis: str, acessibilidade_geo: str, classificacao: 0, visitas=0) -> None:
        self._designacao: str = designacao
        self._morada: str = morada
        self._latitude: float = latitude
        self._longitude: float = longitude
        self._categoria_ponto: str = categoria_ponto
        self._acessibilidade_fis: str = acessibilidade_fis
        self._acessibilidade_geo: str = acessibilidade_geo
        self._classificacao: int = classificacao
        self._visitas: int = visitas

    def __str__(self) -> str:
        return "Designacao: " + str(self._designacao) + "Morada:  " + str(self._morada) \
            + "Latitude:  " + str(self._latitude) + "Longitude: " + str(self._longitude) + "Categoria Turismo: " + \
            str(self._categoria_ponto) + "Acessiblidade Física" + str(self._acessibilidade_fis) + \
            "Acessiblidade Geográfica" + str(self._acessibilidade_geo) + "Classificacao" \
            + str(self._classificacao) + "Visitas" + str(self._visitas)

    def __dict__(self):
        """
        Retorna um dicionário contendo os atributos do ponto de interesse.

        Returns:
            dict: Um dicionário contendo os atributos do ponto de interesse.
        """
        return {
            "designacao": self._designacao,
            "morada": self._morada,
            "latitude": self._latitude,
            "longitude": self._longitude,
            "categoria_ponto": self._categoria_ponto,
            "acessibilidade_fis": self._acessibilidade_fis,
            "acessibilidade_geo": self._acessibilidade_geo,
            "classificacao": self._classificacao,
            "visitas": self._visitas
        }

    def get_designacao(self) -> str:
        return self._designacao

    def get_morada(self) -> str:
        return self._morada

    def get_latitude(self) -> float:
        return self._latitude

    def get_longitude(self) -> float:
        return self._longitude

    def get_categoria_turismo(self) -> str:
        return self._categoria_ponto

    def get_acessibilidade_fis(self) -> str:
        return self._acessibilidade_fis

    def get_acessibilidade_geo(self) -> str:
        return self._acessibilidade_geo

    def get_classificacao(self) -> int:
        return self._classificacao

    def get_visitas(self) -> int:
        return self._visitas

    def set_categoria_turismo(self, categoria):
        self._categoria_ponto = categoria

    def set_acessibilidade_fis(self, acessibilidade_fis):
        self._acessibilidade_fis = acessibilidade_fis

    def set_acessibilidade_geo(self, acessibilidade_geo):
        self._acessibilidade_geo = acessibilidade_geo
