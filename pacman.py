#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from labirinto import Labirinto
from turtle import *
from time import sleep

import myInput
def main():
    '''IMPORTANTE: BAIXAR O ARQUIVO "legend.gif" e colocar o caminho dele no método criar_tela (labirinto)'''
    #esse é o método principal
    projeto_SaferRoute()

    #REQ-02
    #um_agente_vagueia()

    #REQ-03
    #todos_vagueiam()

    #REQ-04
    #um_agente_percorre_tudo()

    #REQ-05
    #varios_agentes_percorrem_tudo()#OBS: precisa definir no input a quantidade agentes

    #REQ-07
    #agente_com_um_destino()

    #REQ-08
    #agente_com_n_destinos()#OBS: precisa definir no input a quantidade agentes

    #REQ-09 NESSE METODO ABAIXO NÃO HÁ COLISÃO DE AGENTES
    #todos_vagueiam()

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
    lab.add_pacman(id)

    n_fantasmas = myInput.qtd_fantasmas() #define a quantidade de fantasmas de acordo com a aglomeração
    for kid in range(1, n_fantasmas):
        lab.add_fantasma(kid)

    n_frames = 500
    intervalo_entre_frames = 0.1

    agentes = lab.agentes
    for _ in range(n_frames):
        for kid in agentes.keys():
            agentes[kid].vaguear()
        # Atualiza "frame"
        update()
        sleep(intervalo_entre_frames)


def agente_com_um_destino():
    """ Agente caminha para um destino aleatoriamente sorteado """

    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0

    agente = lab.add_pacman(id)
    ghost = lab.add_fantasma(2)

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




def projeto_SaferRoute():
    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    agente = lab.add_pacman(id)

    origem = agente._posicao
    destino = lab.fim_aleatorio()
    lab.desenhar_celula(origem, 'red')
    lab.desenhar_celula(destino, 'red')

    intervalo_entre_frames = 0.3

    n_fantasmas = myInput.qtd_fantasmas()  # define a quantidade de fantasmas de acordo com a aglomeração
    for id in range(1, n_fantasmas):
        lab.add_fantasma(id)
    agentes = lab.agentes
    chegou_ao_destino = False
    while (not chegou_ao_destino):
        for id in agentes.keys():
            if id != 0:
                agentes[id].vaguear()#faz os fantasmas vaguearem
        sleep(intervalo_entre_frames)
        chegou_ao_destino = agente.ir_a(destino)

        update()




def varios_agentes_percorrem_tudo():
    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    agente = lab.add_pacman(id)
    n_agentes= int(input("defina quantos agentes"))


    intervalo_entre_frames = 0.5
    agentes = lab.agentes
    chegou_ao_fim = False
    for id in range(1, n_agentes):
        lab.add_fantasma(id)


    while (not chegou_ao_fim):

        for id in agentes.keys():

            agentes[id].percorrer()

        chegou_ao_fim = agente.percorrer()
        # Atualiza "frame"
        update()
        sleep(intervalo_entre_frames)

def agente_com_n_destinos():
    n = int(input("defina o numero de N destinos"))
    for _ in range(n):
        agente_com_um_destino()
main()
