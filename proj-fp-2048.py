# Segundo Projecto de Fundamentos de Programacao - 2048
# Grupo 22 
# Jose' Canana - 82039 
# Nelson Rodrigues - 82018 
# Miguel Ramalho - 81948

def cria_coordenada(l, c):
    '''Recebe 2 inteiros entre 1 e 4 que indicam a linha e a coluna e devolve
    a coordenada correspondente na forma de dicionario, verificando a validade 
    dos seus argumentos'''
    if l in range(1,5) and c in range(1,5):
        return (l, c)
    else:
        raise ValueError('cria_coordenada: argumentos invalidos')

def coordenada_linha(coord):
    '''Recebe uma coordenada e devolve um inteiro correspondente a linha dessa 
    coordenada'''
    return coord[0]

def coordenada_coluna(coord):
    '''Recebe uma coordenada e devolve um inteiro correspondente a coluna dessa 
    coordenada'''
    return coord[1]

def e_coordenada(coord):
    '''Recebe uma coordenada e verifica se a mesma e' valida devolvendo um valor 
    booleano'''  
    if isinstance(coord, tuple) and len(coord) == 2 and coordenada_linha(coord)\
    in range(1,5) and coordenada_coluna(coord) in range(1,5) :
        return True
    else:
        return False

def coordenadas_iguais(c1, c2):
    '''Recebe duas coordenadas e verifica se sao iguais devolvendo um valor
    booleano'''
    return c1 == c2
    
def cria_tabuleiro():
    '''Esta funcao nao recebe parametros e cria um tabuleiro representado por
    uma lista com listas correspondentes 'as linhas do tabuleiro, o valor de 
    todas as entradas e' 0 e o segundo valor da lista principal representa
    a pontuacao'''    
    return[[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], 0]

def tabuleiro_posicao(t, c):
    ''''Recebe argumentos t correspondente a um tabuleiro e c correspondente a
    coordenada verifica se o segundo argumento e' coordenada e devolve um 
    inteiro correspondente ao valor do tabuleiro na coordenada indicada'''
    if e_coordenada(c):
        return t[0][coordenada_linha(c)-1][coordenada_coluna(c)-1]
    else:
        raise ValueError('tabuleiro_posicao: argumentos invalidos')

def tabuleiro_pontuacao(t):
    '''Recebe argumento t correspondente a um tabuleiro e devolve um inteiro
    correspondente 'a pontuacao actual do tabuleiro t'''
    return t[1]
            
def tabuleiro_posicoes_vazias(t):
    '''Recebe como argumento t um tabuleiro e devolve uma lista com as
    coordenadas de todas as posicoes vazias do tabuleiro t'''
    pos_vazias = []
    for i in range(len(t[0])):
        for j in range(len(t[0][i])):
            if tabuleiro_posicao(t, cria_coordenada(i+1,j+1)) == 0:
                pos_vazias += [cria_coordenada(i+1,j+1)]
    return pos_vazias

def tabuleiro_preenche_posicao(t, c, v):
    '''Modificador que recebe como argumentos t que corresponde a um 
    tabuleiro, c correspondente a coordenada que sera' alterada e v 
    correspondente ao valor a alterar, a funcao devolve o tabuleiro modificado 
    e verifica ainda se a coordenada c e' valida e v e' um inteiro'''
    if e_coordenada(c) and isinstance(v, int):
        t[0][coordenada_linha(c)-1][coordenada_coluna(c)-1] = v
        return t
    else:
        raise ValueError('tabuleiro_preenche_posicao: argumentos invalidos')

def tabuleiro_actualiza_pontuacao(t, v):
    '''Modificador que recebe como argumentos t que corresponde a um tabuleiro
    e v que corresponde a um inteiro nao negativo multiplo de 4, a funcao devolve
    o tabuleiro acrescentando o valor v de pontos e verifica se v e' um inteiro
    nao negativo e multiplo de 4'''
    if isinstance(v, int) and v >= 0 and v % 4 == 0:
        t[1] += v   
        return t
    else:
        raise ValueError('tabuleiro_actualiza_pontuacao: argumentos invalidos')

def tabuleiro_transposto(t):
    '''Recebe um  tabuleiro como argumento e devolve esse tabuleiro transposto
    como se fosse uma matriz'''
    tcopia = copia_tabuleiro(t)
    for linha in range(4):
        for coluna in range(4):
            t[0][linha][coluna] = tcopia[0][coluna][linha] 
    return t
    
def tabuleiro_reduz(t, d):
    '''Modificador que recebe como argumentos t que corresponde a um 
    tabuleiro e d, uma cadeia de caracteres correspondente a uma das 4 accoes
    possiveis ('N','S','E','W'). Esta funcao modifica o tabuleiro reduzindo-o
    na direccao d de acordo com as regras do jogo. A funcao devolve o
    tabuleiro t modificado e a sua pontuacao actualizada verificando ainda se
    d e' uma jogada valida'''
    if d in ('W', 'E', 'N', 'S'):
        # se  a direcao N ou S transpoe tabuleiro
        if d == 'N' or d == 'S':
            tabuleiro_transposto(t)
        # dependendo da direcao a coluna inicial varia
        if d == 'W' or d == 'N':
            col_ini = 1
        else:
            col_ini = -4
        for linha in range(1, 5):
            if tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini))) != 0 or\
            tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+1))) != 0 or\
            tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+2))) != 0 or\
            tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+3))) != 0:
                # se alguma das colunas na linha for diferente de 0
                # 'arrasta' o tabuleiro dependendo da direcao desejada para 
                # os zeros entre os valores diferentes de 0
                # repete o mesmo procedimento para as 3 primeiras colunas
                # testa se a coluna esta' a 0 e 'arrasta' as colunas ate essa coluna
                # passar a ter um valor diferente de 0 
                if tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini))) == 0:
                    while tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini))) == 0:
                        # podia ter implementado um ciclo for mas penso que assim seria mais legivel
                        tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini)), tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+1))))
                        tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+1)), tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+2))))
                        tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+2)), tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+3))))
                        tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+3)), 0)
                if tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+1))) == 0 and \
                (tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+2))) != 0 or \
                tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+3))) != 0):
                    while tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+1))) == 0:
                        tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+1)), tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+2))))
                        tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+2)), tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+3))))
                        tabuleiro_preenche_posicao(t, cria_coordenada(linha,abs(col_ini+3)), 0)
                if tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+2))) == 0 and \
                tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+3))) != 0:
                    while tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+2))) == 0:    #nao precisa de while neste caso mas torna-se mais legivel
                        tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+2)), tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+3))))
                        tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+3)), 0)
                # testa pares de colunas e se forem iguais 'junta-os' e 'arrasta'
                # o tabuleiro actualizando antes a pontuacao
                if tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini))) == tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+1))):
                    tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini)), tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini)))*2)
                    tabuleiro_actualiza_pontuacao(t, tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini))))
                    tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+1)), tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+2))))
                    tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+2)), tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+3))))
                    tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+3)), 0)   
                if tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+1))) == tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+2))):
                    tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+1)), tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+1)))*2)
                    tabuleiro_actualiza_pontuacao(t, tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+1))))
                    tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+2)), tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+3))))
                    tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+3)), 0)                
                if tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+2))) == tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+3))):
                    tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+2)), tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+2)))*2)
                    tabuleiro_actualiza_pontuacao(t, tabuleiro_posicao(t, cria_coordenada(linha, abs(col_ini+2))))
                    tabuleiro_preenche_posicao(t, cria_coordenada(linha, abs(col_ini+3)), 0)             
        # reinicia tabuleiro se tiver sido transposto
        if d == 'N' or d == 'S':
            tabuleiro_transposto(t)        
        return t
    else:
        raise ValueError('tabuleiro_reduz: argumentos invalidos')
                    
def e_tabuleiro(t):
    '''Esta funcao recebe um argumento universal e verifica se o argumento e um
    tabuleiro devolvendo um valor booleano.'''
    if not isinstance(t,list) or len(t) != 2 or not isinstance(t[0], list) or \
    len(t[0]) != 4 or not isinstance(t[1], int) or t[1] < 0:
        return False
    for linha in range(4):
        if not isinstance(t[0][linha], list) or len(t[0][linha]) != 4:
            return False
        for coluna in range(1,5):
            if not isinstance(tabuleiro_posicao(t, cria_coordenada(linha+1, coluna)), int)\
            or tabuleiro_posicao(t, cria_coordenada(linha+1, coluna)) < 0:
                return False
    else:
        return True
            
def copia_tabuleiro(t):
    '''Recebe um argumento do tipo tabuleiro e devolve uma copia'''
    from copy import deepcopy
    return deepcopy(t)

def tabuleiro_terminado(t):
    '''Esta funcao recebe um argumento do tipo tabuleiro verifica se o tabuleiro
    t esta preenchido e nao existam movimentos possiveis e devolve um valor
    booleano'''
    if tabuleiro_posicoes_vazias(t) == []:
        tabuleiro_inicial = copia_tabuleiro(t)
        return tabuleiros_iguais(tabuleiro_inicial, tabuleiro_reduz(t, 'N')) and \
        tabuleiros_iguais(tabuleiro_inicial, tabuleiro_reduz(t, 'S')) and \
        tabuleiros_iguais(tabuleiro_inicial, tabuleiro_reduz(t, 'E')) and \
        tabuleiros_iguais(tabuleiro_inicial, tabuleiro_reduz(t, 'W'))
    else:
        return False     

def tabuleiros_iguais(t1, t2):
    '''Recebe dois tabuleiros e verifica se sao iguais devolvendo um valor
    booleano'''
    return t1 == t2

def escreve_tabuleiro(t):
    '''Esta funcao recebe um argumento do tipo tabuleiro e escreve no ecra uma
    representacao externa do tabuleiro 2048 verificando primeiro se o tabuleiro
    e valido'''
    if e_tabuleiro(t):
        for linha in range(1, 5):
            for coluna in range(1, 5):
                print('[', tabuleiro_posicao(t, cria_coordenada(linha, coluna)), ']', end=' ')
            print()
        print('Pontuacao:', tabuleiro_pontuacao(t))
    
    else:
        raise ValueError('escreve_tabuleiro: argumentos invalidos')

def pede_jogada():
    '''Funcao nao recebe qualquer argumento apenas pede que o utilizador 
    introduza uma das direcoes N, S, E ou W e verifica se e' uma direcao
    valida devolvendo uma cadeia de caracteres correspondente 'a jogada ou
    pedindo nova jogada caso nao seja valida'''
    d = str(input('Introduza uma jogada (N, S, E, W): '))
    if d in ('N', 'S', 'E', 'W'):
        return d
    else:
        print('Jogada invalida.')
        return pede_jogada()
        
def preenche_posicao_aleatoria(t):
    '''Recebe um argumento do tipo tabuleiro e preenche uma posicao livre 
    escolhida aleatoriamente com um dos valores 2 ou 4 de acordo com as 
    probabilidades do jogo'''
    from random import sample
    coord_aleatoria = sample(tabuleiro_posicoes_vazias(t), 1)
    valor_aleatorio = sample([4,2,2,2,2], 1)
    # coord_aleatoria[0] e valor_aleatorio[0] pois sample devolve listas
    tabuleiro_preenche_posicao(t, coord_aleatoria[0], valor_aleatorio[0])
    return t

def jogo_2048():
    '''Esta funcao nao recebe argumentos e permite que o jogo possa ser 
    jogado, em cada turno a funcao escreve o tabuleiro no ecra e pede ao 
    utilizador uma nova jogada, se a jogada for valida actualiza o 
    tabuleiro, e repete ate o jogo terminar caso contrario deve pedir uma 
    nova jogada'''
    t = cria_tabuleiro()
    preenche_posicao_aleatoria(t)
    preenche_posicao_aleatoria(t)
    escreve_tabuleiro(t)
    while not tabuleiro_terminado(t):
        if not tabuleiros_iguais(copia_tabuleiro(t), tabuleiro_reduz(t, pede_jogada())):
            preenche_posicao_aleatoria(t)
            escreve_tabuleiro(t)
        else:
            escreve_tabuleiro(t)

jogo_2048()
