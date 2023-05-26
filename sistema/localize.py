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
    print("Latitude:", latitude)
    print("Longitude:", longitude)
else:
    print("Não foi possível obter a localização atual.")
