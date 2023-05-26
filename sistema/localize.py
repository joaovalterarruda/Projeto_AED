import geocoder


def obter_localizacao_atual():
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng
    else:
        return None


localizacao = obter_localizacao_atual()
if localizacao:
    latitude, longitude = localizacao
    print("A sua Latitude é:", latitude)
    print("A sua Longitude é:", longitude)
else:
    print("Não foi possível obter a localização atual.")
