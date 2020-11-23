#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

class Matriz:
    def __init__(self):
        self._visited = []
        self._queue = []
        self._cmp_conexas = {}
        self._matriz = None
        self.dim = None

    def aleatoria(self, dimensao):
        """ Cria uma matriz aleatória conexa """
        self.dim = dimensao
        self._matriz = np.random.randint(2,size=(dimensao,dimensao))
        self.__marcar_cmp_conexas()
        self.__conectar_cmp_conexas()
        self.__renumerar_cmp_conexas()
        return self._matriz

    def ler_fixa(self):
        #não tem = 4 , 5 , 6, 7, 9, 10, 11
        # , 14, 15 , 16, 17, 18, 19 , 20,
        return  [[2,2,2,50,12,12,12,12,3,3,3,3,30,30,30,30,30,99,99,99],
                 [2,2,2,1,12,12,12,12,3,3,3,3,30,30,30,30,30,99,99,99],
                 [2,2,2,69,1,69,69,1,69,1,1,69,1,1,69,1,1,1,3,3],
                 [2,2,2,1,13,13,13,13,13,13,13,13,13,13,1,13,13,69,3,3],
                 [50,1,1,1,13,13,13,69,25,25,25,25,25,25,25,13,13,1,3,3],
                 [2,2,2,1,13,13,13,1,25,13,1,13,1,13,25,13,13,1,12,12],
                 [2,2,2,1,13,13,13,1,25,25,25,25,25,25,25,1,1,69,12,12],
                 [2,2,2,69,1,1,1,1,25,13,1,13,1,13,25,13,13,1,12,12],
                 [2,2,2,1,13,13,13,69,25,25,25,25,25,25,25,13,13,1,30,30],
                 [2,2,2,1,13,13,13,13,13,13,1,13,13,13,13,13,13,1,30,30],
                 [50,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,50],
                 [50,1,69,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,50],
                 [2,2,2,1,0,0,0,0,0,1,8,8,8,1,8,8,8,1,8,8],
                 [2,2,2,1,0,0,0,0,0,1,8,8,8,1,8,8,8,1,8,8],
                 [2,2,2,1,0,0,0,0,0,1,8,8,8,1,8,8,8,1,8,8],
                 [2,2,2,1,1,69,1,1,1,1,1,69,1,1,1,1,1,1,8,8],
                 [0,0,0,0,1,0,0,1,0,0,0,1,8,8,1,8,8,1,8,8],
                 [0,0,0,0,1,0,0,1,0,0,0,1,8,8,1,8,8,1,8,8],
                 [0,0,0,0,1,1,1,1,1,1,69,1,1,1,69,1,1,1,8,8],
                 [0,0,0,0,1,0,0,50,0,0,0,1,8,8,8,8,8,50,8,8]]
#0,1,2,3,

    def carregar_de(self, nome_arquivo):
        # REQ
        return [[]]

    def tracar_rota_manhattan(self, origem, destino):
        xo, yo = origem
        xd, yd = destino
        x, y = xo, yo
        dist = self.dist_manhattan(origem, destino)
        passo_x, passo_y = self.__obter_passo_manhattan(origem, destino)
        rota = []
        for i in range(dist):
            rota.append((x,y))
            if (self._matriz[x][y]==0):
                self._matriz[x][y] = 1
            andou_x = False
            if (x != xd):
                andou_x = True
                x += passo_x
            if (not andou_x and y != yd):
                y += passo_y
        rota.append((x,y))
        #self._matriz[x][y] = 1
        return rota

    def dist_manhattan(self, origem, destino):
        xo, yo = origem
        xd, yd = destino
        return abs(xo - xd) + abs(yo - yd)

    def imprimir(self):
        for i in range(self.dim):
            print(self._matriz[i])

    def __renumerar_cmp_conexas(self):
        """ Renumera as cmp conexas.
            Utilizado na criação de matriz aleatória
        """
        for i in range(self.dim):
            for j in range(self.dim):
                if (self._matriz[i][j] > 0):
                    self._matriz[i][j] = 1

    def __detectar_ciclo(self, grafo, ori, dst):
        """ Detecta se a inclusão da aresta no grafo não forma ciclo
            Utilizado na criação de matriz aleatória
        """
        # v representa uma origem, e w, um destino
        for v, w in grafo:
            if (v == dst):
                return True
        return False

    def __conectar_cmp_conexas(self):
        """ Conecta cmp conexas na matriz.
            Utilizado na crição de matriz aleatória
        """

        # Só é necessário conectar se houver mais de uma cmp conexa
        qtde_cmp_cnx = len(self._cmp_conexas)
        if (qtde_cmp_cnx < 2):
            return

        # registra as arestas de um grafo com os num das cmp conexas
        # utilizado para detectar ciclos
        arestas = []

        num_cc1 = 1
        mnr_dist = None
        for i in range(qtde_cmp_cnx-1):
            num_cc1 += 1
            lst_ori = self._cmp_conexas[num_cc1]
            # TODO melhorar esse numero grande e fixo
            mnr_dist = (10000000, None, None)
            num_cc2 = num_cc1
            for j in range(i+1, qtde_cmp_cnx):
                num_cc2 += 1
                lst_dst = self._cmp_conexas[num_cc2]
                dist, mnr_ori, mnr_dst = self.__achar_cels_proxs(lst_ori, lst_dst)
                if (dist < mnr_dist[0]):
                    mnr_dist = (dist, mnr_ori, mnr_dst)

            if (not self.__detectar_ciclo(arestas, num_cc1, num_cc2)):
                arestas.append( [num_cc1,num_cc2] )
                # Conecta as componentes
            self.tracar_rota_manhattan(mnr_dist[1],mnr_dist[2])

    def __marcar_cmp_conexas(self):
        """ Atribui um numero (i.e., marca) para cada cmp conexa
            Utilizado na criação de matriz aleatória
        """
        num_cc = 2
        for i in range(self.dim):
            for j in range(self.dim):
                if (self._matriz[i][j] == 1):
                    self._cmp_conexas[num_cc] = []
                    self.__bfs((i,j), num_cc)
                    num_cc += 1

    def __bfs(self, node, num_cc):
      """ Marca todos os elementos de uma mesma cmp conexa
          Utilizado na criação de matriz aleatória
      """
      self._queue.append(node)

      while (self._queue):
        node = self._queue.pop(0)
        lin, col = node
        # Visita a coordenada
        self._matriz[lin][col] = num_cc

        if (node not in self._cmp_conexas[num_cc]):
            self._cmp_conexas[num_cc].append(node)

        vizinhos = self.obter_vizinhos(node);

        for vizinho in vizinhos:
          self._queue.append(vizinho)
          if (vizinho not in self._cmp_conexas[num_cc]):
            self._cmp_conexas[num_cc].append(vizinho)

    def __obter_passo_manhattan(self, origem, destino):
        """ Função auxiliar para traçar uma rota manhattan.
            Utilizado na criação de matriz aleatória
        """
        xo, yo = origem
        xd, yd = destino

        if (xo < xd):
            passo_x = 1
        elif (xo > xd):
            passo_x = -1
        else:
            passo_x = 0

        if (yo < yd):
            passo_y = 1
        elif (yo > yd):
            passo_y = -1
        else:
            passo_y = 0

        return passo_x, passo_y

    def __achar_cels_proxs(self, lst_origens, lst_destinos):
        """ Encontra as coordenadas mais próximas entre duas cmp conexas
            Utilizado na criação de matriz aleatória
        """
        menor = None # menor distancia
        for ori in lst_origens:
            for dest in lst_destinos:
                distancia = self.dist_manhattan(ori,dest)
                if (not menor or distancia < menor[0]):
                    menor = (distancia, ori, dest)
        return menor

    def obter_vizinhos(self, coordenada):
        """ Retorna os vizinhos de uma celula
            Utilizado na criação de matriz aleatória
        """
        lin, col = coordenada
        vizinhos = []
        # Vizinho de cima
        if (lin > 0 and self._matriz[lin-1][col] == 1):
            vizinhos.append((lin-1, col))

        # Vizinho esquerdo
        if (col > 0 and self._matriz[lin][col-1] == 1):
            vizinhos.append((lin, col-1))

        # Vizinho direito
        if (col + 1 < self.dim and self._matriz[lin][col+1] == 1):
            vizinhos.append((lin, col+1))

        # Vizinho de baixo
        if (lin + 1 < self.dim and self._matriz[lin+1][col] == 1):
            vizinhos.append((lin+1, col))

        return vizinhos
