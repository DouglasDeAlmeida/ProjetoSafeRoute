#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from celula import Celula
from time import sleep
from turtle import *

class Waze:

    def __init__(self, labirinto):
        """ Construtor. Inicializa o objeto com uma referência ao labirinto,
            uma lista de coordenadas a ser seguida pelo agente, e um atributo
            que indica se o percurso já foi finalizado.
        """
        self.labirinto = labirinto
        self.lst_coord = []
        self.finalizado = None

    def obter_prox_coord(self):
        """ Retorna a próxima coordenada ao agente """
        if (self.esta_sem_coord()):
            return
        item = self.lst_coord.pop(0)
        # Caso a lista fique vazia após a retirada (pop) do elemento,
        # significa que o percurso acabou
        if (self.esta_sem_coord()):
            self.finalizado = True
        return item

    def fim_percurso(self):
        """ Mostra se o percurso está finalizado (True ou False) """
        return self.finalizado == True

    def esta_sem_coord(self):
        """ Mostra se a lista de coordenadas está vazia (True ou False) """
        return len(self.lst_coord) == 0

    def gerar_percurso(self, celula):
        """ Gera um percurso no labirinto a partir de uma determinada célula """
        visitadas = [] # Indica quais células já foram visitadas
        # lst_coord: indica as coordenadas que o agente deve seguir para
        #            percorrer todo o labirinto
        lst_coord = []

        # Algoritmo de busca em profundidade
        #self.__dfs(celula, visitadas, lst_coord)
        self.__dfs(celula, visitadas, lst_coord)

        #self.lst_coord = lst_coord
        self.lst_coord = lst_coord

        # Logo após ter gerado o percurso, o agente ainda não o percorreu.
        # Por esta razão, este atributo é inicializado como False
        self.finalizado = False

    def __dfs(self, celula, visitadas, lst_coord):
        """ Implementação do algoritmo de busca em profundidade """
        if (celula in visitadas):
            return
        lab = self.labirinto # Para melhorar a legibilidade
        lst_coord.append(celula)
        visitadas.append(celula)

        vizinhas = lab.obter_vizinhos(celula)
        for cel_vizinha in vizinhas:
            if (cel_vizinha not in visitadas):
                self.__dfs(cel_vizinha, visitadas, lst_coord)
                lst_coord.append(celula)
    """
    ROTA
    """
    def add_destino(self, cel_destino):
        self.cel_destino = cel_destino

    def chegou_ao_destino(self, pos_agente):
        return pos_agente == self.cel_destino

    def gerar_rota(self, pos_agente):
        """ Gera uma rota a partir do parâmetro cel_origem """
        lab = self.labirinto # Para melhorar a legibilidade
        self.lst_coord = self.__aestrela(pos_agente, self.cel_destino)

    def rastrear_caminho(self, destino):
        """ Rastreia a origem de cada célula a partir do destino """
        caminho = []
        atual = destino
        while atual is not None:
            caminho.insert(0, atual)
            atual = atual.pai
        return caminho

    def obter_vizinhos(self, celula):
        """ Retorna os vizinhos de uma célula utilizando um outro método
         TODO: adicionar o celula ocupada o if"""

        #if (lab.eh_caminho(vlin, vcol) == True) and (lab.eh_celula_ocupada(vlin, vcol) == False):
        #and (lab.eh_celula_ocupada(vlin, vcol)==False)
        lab = self.labirinto # Para aumentar a legibilidade
        lst_vizinhos = []
        for factor in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Fatores para obter os vizinhos
            i, j = factor
            lin, col = celula._coord_matr
            vlin, vcol = lin + i, col + j

            if (lab.eh_caminho(vlin, vcol) == True):
                vizinho = lab.criar_celula(pai=celula, coord_matr=(vlin,vcol))
                lst_vizinhos.append(vizinho)
        return lst_vizinhos

    def encontrar_min_F(self, atual, lst):
        """ Retorna o índice e a menor celula (F) da lista """
        menor_index = 0
        for index, item in enumerate(lst):
            if item.f < atual.f:
                atual = item
                menor_index = index
        return menor_index, atual

    def __aestrela(self, origem, destino):
        """ Executa o algoritmo A* """
        lab = self.labirinto # Para aumentar a legibilidade

        lst_abertos = [] # representa as células em verde
        lst_fechados = [] # representa as células em vermelho

        lst_abertos.append(origem)
        while (len(lst_abertos) > 0):
            atual = lst_abertos[0]
            # Seleciona a célula com min F da lista de abertos
            index, atual = self.encontrar_min_F(atual, lst_abertos)
            # Retira o menor da lista de abertos
            lst_abertos.pop(index)
            # Inclui o menor na lista de fechados
            lst_fechados.append(atual) # pintar o elemento de vermelho

            # Encontrou o destino
            if (atual == destino):
                # Rastreia o caminho de volta à origem
                return self.rastrear_caminho(atual)

            # Encontra os vizinhos da célula atual
            lst_vizinhos = self.obter_vizinhos(atual)

            # Percorre os vizinhos
            for vizinho in lst_vizinhos:
                # Se o vizinho já estiver na lista de fechados, pule pro próximo
                if (vizinho in lst_fechados):
                    continue

                #  atualiza os valores de F, G, H do vizinho
                vizinho.g = atual.g + 1
                # coordenada matricial do vizinho em análise
                coord_vori = vizinho._coord_matr
                # coordenada matricial do destino
                coord_dest = destino._coord_matr
                # calcula o H (distância manhattan até o destino)
                vizinho.h = lab.dist_manhattan(coord_vori, coord_dest)
                # calcula o F do vizinho
                vizinho.f = vizinho.g + vizinho.h

                if (vizinho not in lst_abertos):
                    # Add o vizinho na lista de abertos
                    lst_abertos.append(vizinho)
