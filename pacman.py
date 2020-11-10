#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from agente import Agente
from labirinto import Labirinto
from turtle import *
from time import sleep

def main():
    # Simulação 1
    # um_agente_percorre_tudo()

    # Simulação 2
    #um_agente_vagueia()

    # Simulação 3
    #todos_vagueiam()

    # Simulação 4
    agente_com_um_destino()

    done()

""" Simulações """

def um_agente_percorre_tudo():
    """ Simulação 1:
        Agente percorre todo o labirinto
    """
    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    agente = lab.add_pacman(id)

    intervalo_entre_frames = 0.1

    chegou_ao_fim = False
    while (not chegou_ao_fim):
        chegou_ao_fim = agente.percorrer()
        # Atualiza "frame"
        update()
        sleep(intervalo_entre_frames)

def um_agente_vagueia():
    """ Simulação 2: Todos os agentes vagueiam """

    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    pacman = lab.add_pacman(id)

    n_frames = 500
    intervalo_entre_frames = 0.1
    for _ in range(n_frames):
        pacman.vaguear()
        update()
        sleep(intervalo_entre_frames)

def todos_vagueiam():
    """ Simulação 3: Todos os agentes vagueiam """

    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    pacman = lab.add_pacman(id)

    n_fantasmas = 10
    for id in range(1, n_fantasmas):
        f = lab.add_fantasma(id)

    n_frames = 500
    intervalo_entre_frames = 0.1

    agentes = lab.agentes
    for _ in range(n_frames):
        for id in agentes.keys():
            agentes[id].vaguear()
        # Atualiza "frame"
        update()
        sleep(intervalo_entre_frames)


def agente_com_um_destino():
    """ Agente caminha para um destino aleatoriamente sorteado """

    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    agente = lab.add_pacman(id)

    origem = agente._posicao
    destino = lab.fim_aleatorio()

    lab.desenhar_celula(origem, 'red')
    lab.desenhar_celula(destino, 'red')

    intervalo_entre_frames = 0.1

    chegou_ao_destino = False
    while (not chegou_ao_destino):
        chegou_ao_destino = agente.ir_a(destino)
        # Atualiza "frame"
        update()
        sleep(intervalo_entre_frames)

main()
