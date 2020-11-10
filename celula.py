#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import floor

class Celula:
    """
    O propósito desta classe é converter as coordenadas da matriz em coordenadas
    Turtle e vice-versa. Um objeto Celula criado a partir das coordenadas da matriz
    irá convertê-las na criação (i.e., no construtor) em coordenadas Turtle e vice-versa.
    """

    # Uma coordenada é apenas uma tupla
    def __init__(self, pai=None, coord_matr=None, coord_turt=None, tam_cel=None, dim=None):
        self._tam_celula = tam_cel
        self._dim = dim

        if (not coord_turt == None):
            # Se passar uma coordenada Turtle, converte pra matriz
            self._coord_turt = coord_turt
            self._coord_matr = self.em_coord_matriz(coord_turt)

        if (not coord_matr == None):
            # Se passar uma coordenada da matriz, converte pra Turtle
            self._coord_matr = coord_matr
            self._coord_turt = self.em_coord_turtle(coord_matr)

        # add os seguintes atributos
        self.pai = pai
        self.f = 0
        self.h = 0
        self.g = 0

    def em_coord_turtle(self, coord_matr):
        """ Dados os índices da matriz (lin, col), retorna as coordenadas do Turtle correspondentes.
            Por exemplo, numa matriz quadrada de dimensão 20, com tamanho de célula 20,
            a chamada de função 'em_coord_turtle(0,0)' deve retornar (-200,200) e a
            chamada de função 'em_coord_turtle(10,10)' deve retornar (0,0)
        """
        lin, col = coord_matr
        meio = self._dim // 2
        x = (col - meio) * self._tam_celula
        y = (meio - lin) * self._tam_celula
        return x, y

    def em_coord_matriz(self, coord_turt):
        """ Dada uma coordenada do Turtle (x,y), retorna os índices correspondentes da matriz
            Por exemplo, numa matriz quadrada de dimensão 20, com tamanho de célula 20,
            a chamada de função 'em_coord_matriz(-200, 200)' deve retornar (0,0) e a
            chamada de função 'em_coord_matriz(0, 0)' deve retornar (10,10).
        """
        x, y = self.chao_da_celula( coord_turt )
        meio = self._dim // 2
        lin = int(meio - (y / self._tam_celula))
        col = int(meio + (x / self._tam_celula))
        return lin, col

    def chao_da_celula(self, coord_turt):
        """ Dadas coordenadas do Turtle (x,y), retorna as coordenadas do início de uma célula.
            Por exemplo, na celula da origem com tamanho 20, a coordenada Turtle (10,10)
            representa o meio da célula. A chamada de função 'chao_da_celula(10, 10)' retorna
            as coordenadas de início dessa célula (0,0
        """
        x, y = coord_turt
        chao_x = int(floor(x, self._tam_celula))
        chao_y = int(floor(y, self._tam_celula))
        return chao_x, chao_y

    def coord_turt_centralizada(self):
        """ Retorna uma coordenada Turtle centralizada na célula """
        x, y = self.coord_turtle()
        x += self._tam_celula // 2
        y += self._tam_celula // 2
        return x, y

    def coord_matriz(self):
        """ Retorna a coordenada de matriz """
        return self._coord_matr

    def coord_turtle(self):
        """ Retorna a coordenada do Turtle """
        return self._coord_turt

    def __eq__(self, other):
        """ Compara este (self) objeto com outro (other) considerando somente
            as coordenadas da matriz
        """
        return self._coord_matr == other._coord_matr

def main():
    """ Faz um teste das conversões """
    # Dimensão de uma matriz para os testes
    dim_matriz = 20
    tam_celula = 20

    # Uma coordenada de matriz conhecida para os testes
    c_matriz = (10,10)
    cel1 = Celula(coord_matr=c_matriz, tam_cel=tam_celula, dim=dim_matriz)

    # Imprime em coordenada turtle para verificamos o resultado
    # Deve resultar em (0,0)
    print(cel1.coord_turtle())

    # Uma coordenada turtle conhecida para os testes
    c_turtle = (0,0)
    cel2 = Celula(coord_turt=c_turtle, tam_cel=tam_celula, dim=dim_matriz)

    # Imprime em coordenada de matriz para verificarmos o resultado
    # Deve resultar em (10,10)
    print(cel2.coord_matriz())

    # Deve resultar em True uma vez que apontam para a mesma célula
    print( cel1 == cel2 )

#main()
