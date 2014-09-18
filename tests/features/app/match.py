# -*- coding: utf-8 -*-
class Match:
    score = []
    opcionset = {"1st": 0, "2nd": 1, "3rd": 2, "4th": 3, "5th": 4}

    def __init__(self, player1, player2, pacted_sets):
        self.p1 = player1
        self.p2 = player2
        self.pacted_sets = pacted_sets
        self.texto = ""
        self.juegosP1 = 0
        self.juegosP2 = 0
        del self.score[:]
        self.score.append("0-0")
        self.ganador = "none"

    def score_set(self):
        numeroaum = 1
        if int(self.pacted_sets) == 5:
            numeroaum = 2

        if((self.juegosP1 + numeroaum) == int(self.pacted_sets)):
            self.text = self.p1 + " defeated " + self.p2
        elif ((self.juegosP2 + numeroaum) == int(self.pacted_sets)):
            self.text = self.p2 + " defeated " + self.p1
        else:
            self.text = self.p1 + " plays with " + self.p2

        return "{0} | {1}".format(self.text, self.listapuntuacion())

    def listapuntuacion(self):
        listapuntos = ""
        inicio = 0
        for i in self.score:
            if inicio == 0:
                listapuntos = i
                inicio += 1
            else:
                listapuntos = listapuntos + ", " + i
        return listapuntos

    def ordenarPuntuacion(self, jugadorGanador, puntos1, puntos2):
        if self.ganador == "none":
            self.ganador = jugadorGanador
        if self.ganador == jugadorGanador:
            return puntos1 + "-" + puntos2
        else:
            return puntos2 + "-" + puntos1

    def ganoSet(self, player):
        if(player == self.p1):
            self.juegosP1 += 1
        else:
            self.juegosP2 += 1

    def guardarPuntuacion(self, puntos1, puntos2, nSets, jugadorGanador):
        if(nSets == "1st"):
            self.score[0] = self.ordenarPuntuacion(
                jugadorGanador, puntos1, puntos2)
        else:
            self.score.insert(
                self.opcionset.get(nSets),
                self.ordenarPuntuacion(
                    jugadorGanador,
                    puntos1,
                    puntos2))
