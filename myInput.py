
import agora

def entrada():

    greetings = "Bem vindo ao Safe-Route, nosso objetivo é fazer uma simulação do melhor horario para" \
                " ir ao shopping, assim como a melhor rota para chegar a loja desejada. Para começar digite" \
                " um dia da semana - ATENÇÃO, DIGITE ASSIM: segunda, terca, quarta, quinta, sexta...\n"

    segunda = {10: 27, 11: 35.25, 12: 45.75, 13: 49.5, 14: 53.25, 15: 55.5, 16: 54.75, 17: 51, 18: 44.25, 19: 36,
               20: 26.25, 21: 18}

    terca = {10: 30.75, 11: 45.5, 12: 49.5, 13: 57, 14: 62, 15: 63, 16: 62, 17: 57, 18: 48, 19: 39, 20: 30, 21: 21}

    quarta = {10: 32.25, 11: 42, 12: 51, 13: 59, 14: 65, 15: 68, 16: 67, 17: 62, 18: 54, 19: 43, 20: 32, 21: 22}

    quinta = {10: 32, 11: 43, 12: 54, 13: 63, 14: 68, 15: 70, 16: 67, 17: 63, 18: 56, 19: 47, 20: 36, 21: 25}

    sexta = {10: 34, 11: 45, 12: 55, 13: 65, 14: 72, 15: 75, 16: 73, 17: 67, 18: 58, 19: 48, 20: 36, 21: 25}

    sabado = {10: 22, 11: 31, 12: 42, 13: 52, 14: 59, 15: 63, 16: 63, 17: 61, 18: 58, 19: 50, 20: 38, 21: 25}

    domingo = {10: 4, 11: 7, 12: 13, 13: 22, 14: 31, 15: 36, 16: 37, 17: 36, 18: 34, 19: 31, 20: 22, 21: 13}

    print(greetings)
    z = input("dia da semana ")
    b = int(input("agora digite um horario - ATENÇÃO, DIGITE ASSIM: 10, 11, 12, 13, 14... "))
    if z == 'segunda':

        nivel_aglomeracao = segunda.get(b)
        return nivel_aglomeracao
    elif z == 'terca':
        nivel_aglomeracao = terca.get(b)
        return nivel_aglomeracao
    elif z == 'quarta':
        nivel_aglomeracao = quarta.get(b)
        return nivel_aglomeracao
    elif z == 'quinta':
        nivel_aglomeracao = quinta.get(b)
        return nivel_aglomeracao
    elif z == 'sexta':
        nivel_aglomeracao = sexta.get(b)
        return nivel_aglomeracao
    elif z == 'sabado':
        nivel_aglomeracao = sabado.get(b)
        return nivel_aglomeracao
    elif z == 'domingo':
        nivel_aglomeracao = domingo.get(b)
        return nivel_aglomeracao

def visita():
    visita = (input("Usuario! Se desejar fazer uma visitar imediata ao Shopping\n" 
                    "para obter nivel de aglomeracao em  tempo real - digite: agora.\n"
                    "Caso queira fazer uma simulação para um dia e horario específico digite: sou o rei da cocada preta :"))
    if visita == "agora":
        visita = agora.classificacao_metricas_observadas()
        return visita
    else:
        visita = entrada()
        return visita

def qtd_fantasmas():
    nivel_aglomeracao = visita()
    if nivel_aglomeracao <= 30:
        v = print('Nivel de aglomeração baixo')
        #fazer 2 fantasmas
        nGhosts = 10
        return nGhosts
    elif (nivel_aglomeracao > 30 and nivel_aglomeracao<= 65):
        v =print('Nivel de algomeração medio')
        #fazer 6 fantasmas
        nGhosts = 30
        return nGhosts
    elif (nivel_aglomeracao > 65):
        v =print('Nivel de aglomeração alto')
        #fazer 10 fantasmas
        nGhosts = 60
        return nGhosts



