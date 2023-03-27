import random


def jugador_aleatorio(jugador_1, jugador_2):
    jugadors_inicial = ""
    lista = [jugador_1, jugador_2]
    jugadors_inicial = random.choice(lista)
    return jugadors_inicial
