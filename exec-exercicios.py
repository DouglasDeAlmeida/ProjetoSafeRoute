#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from agente import Agente
from labirinto import Labirinto
from turtle import *
from time import sleep

def main():
    tracer(False)
    bgcolor('black')

    dimensao_da_matriz = 20
    tam_celula = 20

    # Cria o labirinto
    lab = Labirinto(dimensao_da_matriz, tam_celula)
    lab.criar_labirinto()

    tam_agente = 20

    # 1o agente
    agente0 = Agente(0, tam_agente, "yellow")
    agente0.add_labirinto(lab)
    #pos_central = lab.criar_celula(coord_turt=(-20,20))
    #agente0._posicao = pos_central
    agente_percorreu_tudo = False
    while (not agente_percorreu_tudo):
        agente_percorreu_tudo = percorrer(agente0)
        update()
        sleep(0.4)

    #vizinhos = lab.obter_vizinhos(pos_central)
    #agente0._posicao = vizinhos[0]
    #percorrer(agente0)

    done()

def percorrer(agente):
    """ Percorrer significa passar por todas as coordenadas alcançáveis
        do labirinto
    """

    agente.add_percurso()
    waze = agente._waze
    if (waze.fim_percurso()):
        return True

    # Gera o percurso quando estiver sem coordenadas
    if (waze.esta_sem_coord()):
        waze.gerar_percurso( agente._posicao )

    # Atribui a próxima posição da lista ao agente quando há coordenadas
    if (not waze.esta_sem_coord()):
        agente._posicao = waze.obter_prox_coord()
        agente.desenhar_se()

    return False

main()
