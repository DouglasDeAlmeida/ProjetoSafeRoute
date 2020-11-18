#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from turtledemo.clock import setup

from utils import floor
from turtle import *
import numpy as np
from celula import Celula

# Acrescenta esta biblioteca ao labirinto
from matriz import Matriz
from agente import Agente

class Labirinto:

    def __init__(self, dim, tam_celula=None):
        """ Construtor do Labirinto """
        self._dim = dim # Atributo que armazena a dimensão da matriz
        # tam_celula: Atributo que armazena o tamanho da célula
        if (not tam_celula):
            self._tam_celula = 20
        else:
            self._tam_celula = tam_celula

        self._turtle = Turtle() # A tartaruga que desenha o caminho do labirinto
        self._turtle.hideturtle() # Esconde a tartaruga

        # Código novo
        self.agentes = {}
        self.criar_matriz(self._dim)
        self.criar_tela()

    def criar_celula(self, pai=None, coord_matr=None, coord_turt=None):
        """ Cria uma célula com o tamanho de célula e dimensão de _matriz
            definidas como atributos na classe Labirinto
        """
        return Celula(pai=pai, coord_matr=coord_matr, coord_turt=coord_turt, tam_cel=self._tam_celula, dim=self._dim)

    def criar_matriz(self, dimensao):
        """ Cria uma matriz """
        #self._matriz = Matriz().aleatoria(dimensao)
        self._matriz = Matriz().ler_fixa()

    def criar_tela(self, p1=420, p2=420, p3=370, p4=0):
        """ Cria uma tela do Turtle """
        tracer(False)
        hideturtle()
        bgcolor('white')
        setup(p1, p2, p3, p4)
        self.criar_labirinto()

    def criar_labirinto(self, p1=720, p2=720, p3=70, p4=0):
        """ Cria o gráfico do labirinto baseado nos valores da matriz """
        setup(p1, p2, p3, p4)

        # Para cada linha da matriz
        for lin in range(self._dim):
            # Para cada coluna da matriz
            for col in range(self._dim):
                # Testa se a coordenada da matriz (lin, col) é caminho (=1)
                if (self._matriz[lin][col] == 1):
                    # Em caso positivo, transforma em coordenada Turtle.
                    # Atenção: Numa coordenada Turtle (x,y), o eixo x refere-se à coluna e o eixo y à linha
                    # Numa coordenada da matriz (lin, col), o primeiro elemento é a linha e o segundo a coluna

                    celula = self.criar_celula(coord_matr=(lin, col))
                    # Pinta a celula na posição (x,y) com a cor especificada
                    self.desenhar_celula(celula, 'azure3')

                elif (self._matriz[lin][col] == 69):
                    celula = self.criar_celula(coord_matr=(lin, col))

                    self.desenhar_celula(celula, 'azure3')

                elif (self._matriz[lin][col] == 0):
                    celula = self.criar_celula(coord_matr=(lin, col))

                    self.desenhar_celula(celula, 'black')

                elif (self._matriz[lin][col] == 2):
                    celula = self.criar_celula(coord_matr=(lin, col))

                    self.desenhar_celula(celula, 'pink')
                elif (self._matriz[lin][col] == 3):
                    celula = self.criar_celula(coord_matr=(lin, col))

                    self.desenhar_celula(celula, 'gold')
                elif (self._matriz[lin][col] == 4):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'violet')
                elif (self._matriz[lin][col] == 5):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'maroon')
                elif (self._matriz[lin][col] == 6):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'chocolate')
                elif (self._matriz[lin][col] == 7):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'cyan')
                elif (self._matriz[lin][col] == 8):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'navy')
                elif (self._matriz[lin][col] == 9):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkGreen')

                elif (self._matriz[lin][col] == 12):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'AntiqueWhite')
                elif (self._matriz[lin][col] == 13):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'bisque4')
                elif (self._matriz[lin][col] == 14):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'Cadetblue')
                elif (self._matriz[lin][col] == 15):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkOrchid')
                elif (self._matriz[lin][col] == 16):

                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkViolet')

                elif (self._matriz[lin][col] == 17):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkSeaGreen2')
                elif (self._matriz[lin][col] == 18):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'CornflowerBlue')
                elif (self._matriz[lin][col] == 19):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'chartreuse')
                elif (self._matriz[lin][col] == 20):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DeepSkyBlue')
                elif (self._matriz[lin][col] == 21):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkGray')
                elif (self._matriz[lin][col] == 22):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkOliveGreen')
                elif (self._matriz[lin][col] == 23):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkMagenta')
                elif (self._matriz[lin][col] == 24):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DeepPink')
                elif (self._matriz[lin][col] == 25):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'azure')
                elif (self._matriz[lin][col] == 26):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkSlateGrey')
                elif (self._matriz[lin][col] == 27):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkGrey')
                elif (self._matriz[lin][col] == 28):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'cornsilk')
                elif (self._matriz[lin][col] == 29):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'cornsilk4')
                elif (self._matriz[lin][col] == 30):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkOrange')
                elif (self._matriz[lin][col] == 32):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkGoldenrod1')
                elif (self._matriz[lin][col] == 33):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'cyan4')
                elif (self._matriz[lin][col] == 34):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'burlywood3')
                elif (self._matriz[lin][col] == 35):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'chartreuse2')
                elif (self._matriz[lin][col] == 36):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'azure4')
                elif (self._matriz[lin][col] == 37):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'azure3')
                elif (self._matriz[lin][col] == 38):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'aquamarine2')
                elif (self._matriz[lin][col] == 39):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkOrange3')
                elif (self._matriz[lin][col] == 40):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkBlue')
                elif (self._matriz[lin][col] == 41):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkTurquoise')
                elif (self._matriz[lin][col] == 42):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'chocolate4')
                elif (self._matriz[lin][col] == 43):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkSlateGrey')
                elif (self._matriz[lin][col] == 44):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DarkRed')
                elif (self._matriz[lin][col] == 45):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'DeepPink4')

                elif (self._matriz[lin][col] == 50):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'lightgreen')
                    self.desenhar_pastilha(celula, 'white')
                elif (self._matriz[lin][col] == 110):
                    celula = self.criar_celula(coord_matr=(lin, col))
                    self.desenhar_celula(celula, 'red')




    def cel_aleatoria(self):
        """ Retorna os índices de uma posição que seja caminho
        """
        i, j = np.random.randint(self._dim, size=(2))
        while (not self.eh_caminho(i, j)):
            i, j = np.random.randint(self._dim, size=(2))

        return self.criar_celula(coord_matr=(i,j))

    def fim_aleatorio(self):
        """ Retorna os índices de uma posição que seja caminho
        """
        i, j = np.random.randint(self._dim, size=(2))
        while (not self.eh_fim(i, j)):
            i, j = np.random.randint(self._dim, size=(2))

        celula = self.criar_celula(coord_matr=(i,j))
        return celula

    def inicio_aleatorio(self):
        """ Retorna os índices de uma posição que seja caminho
        """
        i, j = np.random.randint(self._dim, size=(2))
        while (not self.eh_inicio(i, j)):
            i, j = np.random.randint(self._dim, size=(2))

        celula = self.criar_celula(coord_matr=(i,j))
        return celula

    def desenhar_pastilha(self, celula, cor):
        """ Leva a tartaruga até a posição (x,y) e desenha por exemplo um círculo
            para representar a pastilha
        """
        x, y = celula.coord_turt_centralizada()
        self._turtle.up()
        self._turtle.goto(x, y)
        self._turtle.down()
        self._turtle.dot(3, cor)

    def eh_inicio(self, lin, col):
        """essa função foi criada para fazer com que o agente nasça em uma das entradas """
        if lin >= 0 and col >= 0 and \
                lin < self._dim and col < self._dim and \
                self._matriz[lin][col] == 50:
            return True
    def eh_fim(self, lin, col):
        """essa função foi criada para fazer com que o agente nasça em uma das entradas """
        if lin >= 0 and col >= 0 and \
                lin < self._dim and col < self._dim and \
                self._matriz[lin][col] == 69:
            return True

    def eh_caminho(self, lin, col):
        """ Dada uma matriz quadrada, retorna True quando (lin, col) == 1 e
            False caso contrário.
            Por exemplo, na matriz a seguir:
            [[ 1  0  0 ]
             [ 0  1  0 ]
             [ 0  0  1 ]]
            a chamada de função 'eh_caminho(0,0)' retorna True e
            a chamada de função 'eh_caminho(0,1)' retorna False
        """
        if lin >= 0 and col >= 0 and                    \
                lin < self._dim and col < self._dim and      \
                self._matriz[lin][col] == 1:
            return True
        elif lin >= 0 and col >= 0 and                    \
                lin < self._dim and col < self._dim and      \
                self._matriz[lin][col] == 50:
            return True
        elif lin >= 0 and col >= 0 and                    \
                lin < self._dim and col < self._dim and      \
                self._matriz[lin][col] == 69:
            return True

    def desenhar_celula(self, celula, cor):
        """ Dada uma coordenada (x, y) do Turtle, desenha um quadrado (célula) na posição """
        x, y = celula.coord_turtle()
        self._turtle.color(cor)
        self._turtle.up()
        self._turtle.goto(x,y)
        self._turtle.down()
        self._turtle.begin_fill()
        for _ in range(4):
            self._turtle.forward(self._tam_celula)
            self._turtle.left(90)
        self._turtle.end_fill()
        self._turtle.up()

    def obter_vizinhos(self, celula):
        """ Retorna os vizinhos de uma celula """
        lin, col = celula.coord_matriz()
        vizinhos = []

        if (self.eh_caminho(lin-1, col)):
            vz_cima = self.criar_celula(coord_matr=(lin-1, col))
            vizinhos.append(vz_cima)

        if (self.eh_caminho(lin, col-1)):
            vz_esquerdo = self.criar_celula(coord_matr=(lin, col-1))
            vizinhos.append(vz_esquerdo)

        if (self.eh_caminho(lin, col+1)):
            vz_direito = self.criar_celula(coord_matr=(lin, col+1))
            vizinhos.append(vz_direito)

        if (self.eh_caminho(lin+1, col)):
            vz_baixo = self.criar_celula(coord_matr=(lin+1, col))
            vizinhos.append(vz_baixo)

        return vizinhos

    def add_pacman(self, id):
        """ Adiciona o pacman ao labirinto """
        tam_agente = self._tam_celula
        pacman = Agente(id, tam_agente, 'yellow')
        pacman.add_labirinto(self)
        self.agentes[id] = pacman
        return pacman

    def add_fantasma(self, id):
        """ Adiciona um fantasma ao labirinto """
        tam_agente = self._tam_celula
        f = Agente(id, tam_agente, 'red')
        f.add_labirinto(self)
        self.agentes[id] = f
        return f

    def eh_celula_ocupada(self, celula, agente_id):
        """ Verifica se uma celula tem algum agente diferente do agente_id """
        # REQ
        # Deve verificar no dicionário de agentes se a célula do parâmetro está
        # sendo ocupada por algum agente
        """  for e in self.agentes:
            if e != agente_id:"""

       # return False

    def dist_manhattan(self, origem, destino):
        """ Retorna a distância manhattan entre dois pontos do labirinto """
        xo, yo = origem
        xd, yd = destino
        return abs(xo - xd) + abs(yo - yd)
