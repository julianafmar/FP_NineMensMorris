# 99261 Juliana Marcelino

# R[c, l] = (c, l)

def cria_posicao(c, l):
    # str x str -> posicao
    """Recebe duas cadeias de carateres correspondentes a coluna c e a """ \
        """linha l de uma posicao e devolve a posicao correspondente."""
    if not type(c) == str or not type(l) == str or not l in ('1', '2', '3') or \
       not c in ('a', 'b', 'c'):
        raise ValueError('cria_posicao: argumentos invalidos')
    else:
        return (c, l)

def cria_copia_posicao(p):
    # posicao -> posicao
    """Recebe uma posicao p e devolve uma copia dessa posicao."""
    if eh_posicao(p):
        return (p[0], p[1])
    else:
        raise ValueError('cria_copia_posicao: argumento invalido')

def obter_pos_c(p):
    # posicao -> str
    """Recebe uma posicao p e devolve a componente c dessa mesma posicao."""
    return p[0]

def obter_pos_l(p):
    # posicao -> str
    """Recebe uma posicao p e devolve a componente l dessa mesma posicao."""
    return p[1]

def eh_posicao(arg):
    # universal -> booleano
    """Recebe um argumento arg e devolve True caso seja um TAD """ \
        """posicao e False caso contrario."""
    return type(arg) == tuple and type(arg[0]) == str and \
           type(arg[1]) == str and len(arg) == 2 and \
           obter_pos_l(arg) in ('1', '2', '3') and obter_pos_c(arg) in \
           ('a', 'b', 'c')

def posicoes_iguais(p1, p2):
    # posicao x posicao -> booleano
    """Recebe duas posicoes p1 e p2 e devolve True caso sejam """ \
        """posicoes e caso sejam iguais e False em caso contrario."""
    if not eh_posicao(p1) or not eh_posicao(p2):
        return False
    return p1 == p2

def posicao_para_str(p):
    # posicao -> str
    """Recebe uma posicao p e devolve a cadeia de carateres cl """ \
        """(coluna e linha) da posicao p."""
    return str(obter_pos_c(p)) + str(obter_pos_l(p))

def obter_posicoes_adjacentes(p):
    # posicao -> tuplo de posicoes
    """Recebe uma posicao p e devolve um tuplo com as posicoes adjacentes a """\
        """essa posicao p de acordo com a ordem de leitura do tabuleiro."""
    if posicoes_iguais(p, cria_posicao('a', '1')):
        return cria_posicao('b', '1'), cria_posicao('a', '2'), \
               cria_posicao('b', '2')
    if posicoes_iguais(p, cria_posicao('a', '2')):
        return cria_posicao('a', '1'), cria_posicao('b', '2'), \
               cria_posicao('a', '3')
    if posicoes_iguais(p, cria_posicao('a', '3')):
        return cria_posicao('a', '2'), cria_posicao('b', '2'), \
               cria_posicao('b', '3')
    if posicoes_iguais(p, cria_posicao('b', '1')):
        return cria_posicao('a', '1'), cria_posicao('c', '1'), \
               cria_posicao('b', '2')
    if posicoes_iguais(p, cria_posicao('b', '2')):
        return cria_posicao('a', '1'), cria_posicao('b', '1'), \
               cria_posicao('c', '1'), cria_posicao('a', '2'), \
               cria_posicao('c', '2'), cria_posicao('a', '3'), \
               cria_posicao('b', '3'), cria_posicao('c', '3')
    if posicoes_iguais(p, cria_posicao('b', '3')):
        return cria_posicao('b', '2'), cria_posicao('a', '3'), \
               cria_posicao('c', '3')
    if posicoes_iguais(p, cria_posicao('c', '1')):
        return cria_posicao('b', '1'), cria_posicao('b', '2'), \
               cria_posicao('c', '2')
    if posicoes_iguais(p, cria_posicao('c', '2')):
        return cria_posicao('c', '1'), cria_posicao('b', '2'), \
               cria_posicao('c', '3')
    if posicoes_iguais(p, cria_posicao('c', '3')):
        return cria_posicao('b', '2'), cria_posicao('c', '2'), \
               cria_posicao('b', '3')

# R[s] = [s]

def cria_peca(s):
    # str -> peca
    """Recebe uma cadeia de carateres s que identifica um dos jogadores """ \
        """('X' ou 'O') ou peca livre (' ') e devolve a peca correspondente."""
    if not type(s) == str or not s in ('X', 'O', ' '):
        raise ValueError('cria_peca: argumento invalido')
    else:
        return [s]

def cria_copia_peca(j):
    # peca -> peca
    """Recebe uma peca j e devolve uma copia dessa peca."""
    if eh_peca(j):
        return [j[0]]
    else:
        raise ValueError('cria_copia_peca: argumento invalido')

def eh_peca(arg):
    # universal -> booleano
    """Recebe um argumento arg e devolve True caso o argumento seja um TAD """ \
        """peca e False caso contrario."""
    return type(arg) == list and len(arg) == 1 and type(arg[0]) == str and \
           arg[0] in ('X', 'O', ' ')

def pecas_iguais(j1, j2):
    # peca x peca -> booleano
    """Recebe j1 e j2 e devolve True caso sejam pecas e iguais e False """ \
        """em caso contrario."""
    if not eh_peca(j1) or not eh_peca(j2):
        return False
    return j1[0] == j2[0]

def peca_para_str(j):
    # peca -> str
    """Recebe uma peca j e devolve a cadeia de carateres que representa """ \
        """o jogador dono da peca."""
    return '[' + j[0] + ']'

def peca_para_inteiro(j):
    # peca -> N
    """Recebe uma peca e devolve um numero inteiro 1, -1 ou 0 dependendo """ \
        """se a peca e do jogador 'X', 'O' ou livre, respetivamente"""
    if pecas_iguais(j, cria_peca('X')):
        return 1
    if pecas_iguais(j, cria_peca('O')):
        return -1
    if pecas_iguais(j, cria_peca(' ')):
        return 0

# R[tabuleiro] = {'a1' : peca, 'a2' : peca, 'a3' : peca, 'b1' : peca, 'b2' : 
# peca, 'b3' : peca, 'c1' : peca, 'c2' : peca, 'c3' : peca}

def cria_tabuleiro():
    # {} -> tabuleiro
    """Devolve um tabuleiro de jogo do moinho de 3x3 sem posicoes """ \
        """ocupadas por pecas."""
    return {'a1' : ' ', 'a2' : ' ', 'a3' : ' ', 'b1' : ' ', \
            'b2' : ' ', 'b3' : ' ', 'c1' : ' ', 'c2' : ' ', \
            'c3' : ' '}

def cria_copia_tabuleiro(t):
    # tabuleiro -> tabuleiro
    """Recebe um tabuleiro t e devolve uma copia nova desse tabuleiro."""
    if eh_tabuleiro(t):
        tab = {}
        for i in ('a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'):
            tab[i] = t[i]
        return tab
    else:
        raise ValueError('cria_copia_tabuleiro: argumento invalido')

def obter_peca(t, p):
    # tabuleiro x posicao -> peca
    """Recebe um tabuleiro t e uma posicao p e devolve a peca na posicao """ \
        """p do tabuleiro t. Caso a posicao nao esteja ocupada devolve """ \
        """uma peca livre."""
    return [t[posicao_para_str(p)]]

def obter_vetor(t, s):
    # tabuleiro x str -> tuplo de pecas
    """Recebe um tabuleiro t e uma cadeia de carateres s e devolve todas """ \
        """as pecas da linha identificada por s."""
    if s == '1':
        return ([t['a1']], [t['b1']], [t['c1']])
    if s == '2':
        return ([t['a2']], [t['b2']], [t['c2']])
    if s == '3':
        return ([t['a3']], [t['b3']], [t['c3']])
    if s == 'a':
        return ([t['a1']], [t['a2']], [t['a3']])
    if s == 'b':
        return ([t['b1']], [t['b2']], [t['b3']])
    if s == 'c':
        return ([t['c1']], [t['c2']], [t['c3']])

def coloca_peca(t, j, p):
    # tabuleiro x peca x posicao -> tabuleiro
    """Recebe um tabuleiro t, uma peca j e e uma posicao p e devolve o """ \
        """proprio tabuleiro com a peca j na posicao p."""
    t[posicao_para_str(p)] = j[0]
    return t

def remove_peca(t, p):
    # tabuleiro x posicao -> tabuleiro
    """Recebe um tabuleiro t e uma posicao p e devolve o proprio tabuleiro """ \
        """sem a peca na posicao p."""
    t[posicao_para_str(p)] = ' '
    return t

def move_peca(t, p1, p2):
    # tabuleiro x posicao x posicao -> tabuleiro
    """Recebe o tabuleiro t e as posicoes p1 e p2 e modifica """ \
        """destrutivamente o tabuleiro t, movendo a peca que se encontra """ \
        """na posicao p1 para a posicao p2 e devolve o proprio tabuleiro."""
    x = obter_peca(t, posicao_para_str(p1))
    return coloca_peca(remove_peca(t, posicao_para_str(p1)), x,\
                       posicao_para_str(p2))

def eh_tabuleiro(arg):
    # universal -> booleano
    """Recebe um argumento arg e devolve True caso o seu argumento seja """ \
        """um TAD tabuleiro e False caso contrario."""
    x = 0
    y = 0
    for i in ('a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'):
        if not i in arg or type(arg[i]) != str or not arg[i] in ('X', 'O', ' '):
            return False
        if arg[i] == 'X':
            x += 1
        if arg[i] == 'O':
            y += 1
    for s in ('a', 'b', 'c', '1', '2', '3'):
        vet = obter_vetor(arg, s)
        if vet[0] == vet[1] == vet[2] == cria_peca('X'):
            for r in ('a', 'b', 'c', '1', '2', '3'):
                vet = obter_vetor(arg, r)
                if vet[0] == vet[1] == vet[2] == cria_peca('O'):
                    return False
    return type(arg) == dict and 0 <= x <= 3 and 0 <= y <= 3 and \
           (x - y == 1 or x - y == -1 or x - y == 0) and len(arg) == 9

def eh_posicao_livre(t, p):
    # tabuleiro x posicao -> booleano
    """Recebe um tabuleiro t e uma posicao p e devolve True apenas caso """ \
        """a posicao p do tabuleiro esteja livre e False caso contrario."""
    return t[posicao_para_str(p)] == ' '

def tabuleiros_iguais(t1, t2):
    # tabuleiro x tabuleiro -> booleano
    """Recebe dois tabuleiros t1 e t2 e devolve True caso eles sejam """ \
        """iguais e False caso contrario."""
    if not eh_tabuleiro(t1) or not eh_tabuleiro(t2):
        return False    
    for i in ('a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'):
        if t1[i] != t2[i]:
            return False
    return True

def tabuleiro_para_str(t):
    # tabuleiro -> str
    """Recebe um tabuleiro t e devolve a cadeia de caracteres que """ \
        """representa o tabuleiro."""
    return '   a   b   c\n1 [' + t['a1'] + ']-[' + t['b1'] + ']-[' + \
           t['c1'] + ']\n   | \\ | / |\n2 [' + t['a2'] + ']-[' + t['b2'] + \
           ']-[' + t['c2'] + ']\n   | / | \\ |\n3 [' + t['a3'] + ']-[' + \
           t['b3'] +']-[' + t['c3'] + ']'

def tuplo_para_tabuleiro(t):
    # tuplo -> tabuleiro
    """Recebe um tuplo t com 3 tuplos, cada um com 3 valores inteiros """ \
        """iguais a -1, 1 ou 0 que representam respetivamente 'O', 'X' """ \
        """e ' ' e devolve o tabuleiro correspondente."""
    tab = {}
    pos = {'1' : 'X', '-1' : 'O', '0' : ' '}
    x = 0    
    for i in t:
        y = 0
        for j in i:
            if y == 0:
                tab['a' + str(x + 1)] = pos[str(j)]
            if y == 1:
                tab['b' + str(x + 1)] = pos[str(j)]
            if y == 2:
                tab['c' + str(x + 1)] = pos[str(j)]
            y += 1
        x += 1
    return tab

def obter_ganhador(t):
    # tabuleiro -> peca
    """Recebe um tabuleiro t e devolve uma peca do jogador que tenha as """ \
        """suas 3 pecas em linha na vertical ou na horizontal no """ \
        """tabuleiro. Caso nao exista um ganhador devolve uma peca livre."""
    for s in ('1', '2', '3', 'a', 'b', 'c'):
        v = obter_vetor(t, s)
        if pecas_iguais(v[0], v[1]) and pecas_iguais(v[1], v[2]):
            return v[0]
    return cria_peca(' ')

def obter_posicoes_livres(t):
    # tabuleiro -> tuplo de posicoes
    """Recebe um tabuleiro t e devolve um tuplo com as posicoes nao """ \
        """ocupadas pelas pecas de qualquer um dos dois jogadores na """ \
        """ordem de leitura do tabuleiro."""
    pos = ()
    for s in ('1', '2', '3'):
        v = obter_vetor(t, s)
        if pecas_iguais(v[0], cria_peca(' ')):
            pos = pos + (cria_posicao('a', s), )
        if pecas_iguais(v[1], cria_peca(' ')):
            pos = pos + (cria_posicao('b', s), )
        if pecas_iguais(v[2], cria_peca(' ')):
            pos = pos + (cria_posicao('c', s), )
    return pos

def obter_posicoes_jogador(t, j):
    # tabuleiro x peca -> tuplo de posicoes
    """Recebe um tabuleiro t e uma peca j e devolve um tuplo com as """ \
        """posicoes ocupadas pelas pecas j de um dos dois jogadores na """ \
        """ordem de leitura do tabuleiro."""
    pos = ()
    for s in ('1', '2', '3'):
        v = obter_vetor(t, s)
        if pecas_iguais(v[0], j):
            pos = pos + (cria_posicao('a', s), )
        if pecas_iguais(v[1], j):
            pos = pos + (cria_posicao('b', s), )
        if pecas_iguais(v[2], j):
            pos = pos + (cria_posicao('c', s), )
    return pos

def obter_movimento_manual(t, j):
    # tabuleiro x peca -> tuplo de posicoes
    """Recebe um tabuleiro t e uma peca j e devolve um tuplo com uma ou """ \
        """duas posicoes que representam uma posicao ou um movimento """ \
        """introduzido manualmente pelo jogador. Na fase de colocacao, o """ \
        """tuplo contem apenas a posicao escolhida pelo utilizador onde """ \
        """colocar uma nova peca. Na fase de movimento, o tuplo contem a """ \
        """posicao de origem da peca que se deseja movimentar e a posicao """ \
        """de destino."""
    if len(obter_posicoes_livres(t)) == 3:
        x = str(input('Turno do jogador. Escolha um movimento: '))
        if not type(x) == str or not len(x) == 4 or not x[0] in \
           ('a', 'b', 'c') or not x[1] in ('1', '2', '3') or not x[2] in \
           ('a', 'b', 'c') or not x[3] in ('1', '2', '3') or \
           j[0] != t[x[0] + x[1]]:
            raise ValueError('obter_movimento_manual: escolha invalida')
        if posicoes_iguais(cria_posicao(x[0], x[1]), cria_posicao(x[2], x[3])):
            for n in obter_posicoes_jogador(t, j):
                for y in obter_posicoes_adjacentes(n):
                    if y in obter_posicoes_livres(t):
                        raise ValueError\
                              ('obter_movimento_manual: escolha invalida')
            return (cria_posicao(x[0], x[1]), cria_posicao(x[2], x[3]))
        if not cria_posicao(x[2], x[3]) in obter_posicoes_adjacentes\
           (cria_posicao(x[0], x[1])):
            raise ValueError('obter_movimento_manual: escolha invalida')
        if not cria_posicao(x[2], x[3]) in obter_posicoes_livres(t):
            raise ValueError('obter_movimento_manual: escolha invalida')
        return (cria_posicao(x[0], x[1]), cria_posicao(x[2], x[3]))
    else:
        x = str(input('Turno do jogador. Escolha uma posicao: '))
        if not len(x) == 2 or not x[0] in ('a', 'b', 'c') or not x[1] in \
           ('1', '2', '3') or not cria_posicao(x[0], x[1]) in \
           obter_posicoes_livres(t) :
            raise ValueError('obter_movimento_manual: escolha invalida')
        return (cria_posicao(x[0], x[1]), )

def obter_movimento_auto(t, j, dif):
    # tabuleiro x peca x str -> tuplo de posicoes
    """Recebe um tabuleiro t, uma peca j e uma cadeia de carateres dif e """ \
        """devolve um tuplo com uma posicao (na fase de colocacao) ou """ \
        """duas posicoes (na fase de movimento) que representam uma """ \
        """posicao ou um movimento escolhido automaticamente."""
    if pecas_iguais(j, cria_peca('X')):
        auto = cria_peca('O')
    if pecas_iguais(j, cria_peca('O')):
        auto = cria_peca('X')
    if dif == 'facil':
        if len(obter_posicoes_livres(t)) == 3:
            c = obter_posicoes_jogador(t, j)
            for x in c:
                p = obter_posicoes_adjacentes(cria_posicao(str(x[0]), \
                                                           str(x[1])))
                for y in p:
                    if y in obter_posicoes_livres(t):
                        return (x, y)
        else:
            return estrategia(t, j, auto)
    if dif == 'normal':
        if len(obter_posicoes_livres(t)) == 3:
            return (minimax(t, j, 1, ()))[1]
        else:
            return estrategia(t, j, auto)
    if dif == 'dificil':
        if len(obter_posicoes_livres(t)) == 3:
            mov = (minimax(t, j, 5, ()))[1]
            return mov[0], mov[1]
        else:
            return estrategia(t, j, auto)

def estrategia(t, j, auto):
    # tabuleiro x peca x peca -> tuplo de posicoes
    """Recebe um tabuleiro t e duas pecas j e auto que representam o """ \
        """jogador humano e o computador e devolve um tuplo com uma """ \
        """posicao correspondente a fase de colocacao."""
    for s in ('1', '2', '3'):
        v = obter_vetor(t, s)
        if v[1] == v[2] == j and v[0] == cria_peca(' '):
            return (('a', s), )
        if v[0] == v[2] == j and v[1] == cria_peca(' '):
            return (('b', s), )
        if v[0] == v[1] == j and v[2] == cria_peca(' '):
            return (('c', s), )
    for s in ('a', 'b', 'c'):
        v = obter_vetor(t, s)
        if v[1] == v[2] == j and v[0] == cria_peca(' '):
            return ((s, '1'), )
        if v[0] == v[2] == j and v[1] == cria_peca(' '):
            return ((s, '2'), )
        if v[0] == v[1] == j and v[2] == cria_peca(' '):
            return ((s, '3'), )
    for s in ('1', '2', '3'):
        v = obter_vetor(t, s)
        if v[1] == v[2] == auto and v[0] == cria_peca(' '):
            return (('a', s), )
        if v[0] == v[2] == auto and v[1] == cria_peca(' '):
            return (('b', s), )
        if v[0] == v[1] == auto and v[2] == cria_peca(' '):
            return (('c', s), )
    for s in ('a', 'b', 'c'):
        v = obter_vetor(t, s)
        if v[1] == v[2] == auto and v[0] == cria_peca(' '):
            return ((s, '1'), )
        if v[0] == v[2] == auto and v[1] == cria_peca(' '):
            return ((s, '2'), )
        if v[0] == v[1] == auto and v[2] == cria_peca(' '):
            return ((s, '3'), )
    if cria_posicao('b', '2') in obter_posicoes_livres(t):
        return (cria_posicao('b', '2'), )
    for p in ('a1', 'c1', 'a3', 'c3'):
        if cria_posicao(p[0], p[1]) in obter_posicoes_livres(t):
            return ((p[0], p[1]), )
    for p in ('b1', 'a2', 'c2', 'b3'):
        if cria_posicao(p[0], p[1]) in obter_posicoes_livres(t):
            return ((p[0], p[1]), )

def minimax(tabuleiro, jogador, profundidade, seq_movimentos):
    # tabuleiro x peca x inteiro x tuplo -> tuplo de posicoes
    """Recebe um tabuleiro, a peca do jogador, um inteiro que corresponde """ \
        """a profundidade e um tuplo e devolve um tuplo com duas posicoes """ \
        """correspondentes a fase de movimento."""
    melhor_seq_movimentos = ()
    if pecas_iguais(jogador, cria_peca('X')):
        outro_jogador = cria_peca('O')
    if pecas_iguais(jogador, cria_peca('O')):
        outro_jogador = cria_peca('X')
    if pecas_iguais(obter_ganhador(tabuleiro), cria_peca('X')):
        valor_tabuleiro = 1
    elif pecas_iguais(obter_ganhador(tabuleiro), cria_peca('O')):
        valor_tabuleiro = -1
    else:
        valor_tabuleiro = 0
    if not pecas_iguais(obter_ganhador(tabuleiro), cria_peca(' ')) or \
       profundidade == 0:
        return valor_tabuleiro, seq_movimentos
    else:
        melhor_resultado = peca_para_inteiro(outro_jogador)
        for x in obter_posicoes_jogador(tabuleiro, jogador):
            for y in obter_posicoes_adjacentes(x):
                if y in obter_posicoes_livres(tabuleiro):
                    novo_movimento = (x, y)
                    copia_tabuleiro = cria_copia_tabuleiro(tabuleiro)
                    novo_tabuleiro = move_peca(copia_tabuleiro, \
                                               novo_movimento[0], \
                                               novo_movimento[1])
                    novo_resultado, nova_seq_movimentos = minimax\
                        (novo_tabuleiro, outro_jogador, profundidade - 1, \
                         seq_movimentos + novo_movimento)
                    if melhor_seq_movimentos == () or \
                       (pecas_iguais(jogador, cria_peca('X')) and \
                        novo_resultado > melhor_resultado) or \
                       (pecas_iguais(jogador, cria_peca('O')) and \
                        novo_resultado < melhor_resultado):
                        melhor_resultado, melhor_seq_movimentos = \
                            novo_resultado, nova_seq_movimentos
        return melhor_resultado, melhor_seq_movimentos

def moinho(jog, dif):
    # str x str -> str
    """Recebe duas cadeias de carateres que representam a peca com que """ \
        """deseja jogar o jogador humano e a dificuldade pretendida e """ \
        """devolve uma cadeia de carateres que representa a peca """ \
        """ganhadora. Esta funcao permite jogar um jogo do moinho completo """ \
        """de um jogador contra o computador."""
    if not jog in ('[X]', '[O]') or type(jog) != str:
        raise ValueError('moinho: argumentos invalidos')
    if not dif in ('facil', 'normal', 'dificil') or type(dif) != str:
        raise ValueError('moinho: argumentos invalidos')
    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade ' + dif + '.')
    tab = cria_tabuleiro()
    print(tabuleiro_para_str(tab))
    while len(obter_posicoes_livres(tab)) > 3:
        if jog == '[X]':
            tab = coloca_peca(tab, cria_peca(jog[1]), \
                              obter_movimento_manual(tab, cria_peca(jog[1]))[0])
            print(tabuleiro_para_str(tab))
            if not pecas_iguais(obter_ganhador(tab), cria_peca(' ')):
                return peca_para_str(obter_ganhador(tab))
            print('Turno do computador (' + dif + '):')
            tab = coloca_peca(tab, cria_peca('O'), \
                              obter_movimento_auto(tab, \
                                                   cria_peca(jog[1]), dif)[0])
            print(tabuleiro_para_str(tab))
            if not pecas_iguais(obter_ganhador(tab), cria_peca(' ')):
                return peca_para_str(obter_ganhador(tab))
        if jog == '[O]':
            print('Turno do computador (' + dif + '):')
            tab = coloca_peca(tab, cria_peca('X'), \
                              obter_movimento_auto(tab, cria_peca\
                                                   (jog[1]), dif)[0])
            print(tabuleiro_para_str(tab))
            if not pecas_iguais(obter_ganhador(tab), cria_peca(' ')):
                return peca_para_str(obter_ganhador(tab))
            tab = coloca_peca(tab, cria_peca(jog[1]), \
                              obter_movimento_manual(tab, cria_peca(jog[1]))[0])
            print(tabuleiro_para_str(tab))
            if not pecas_iguais(obter_ganhador(tab), cria_peca(' ')):
                return peca_para_str(obter_ganhador(tab))
    while len(obter_posicoes_livres(tab)) == 3:
        if jog == '[X]':
            mov = obter_movimento_manual(tab, cria_peca(jog[1]))
            tab = move_peca(tab, mov[0], mov[1])
            print(tabuleiro_para_str(tab))
            if not pecas_iguais(obter_ganhador(tab), cria_peca(' ')):
                return peca_para_str(obter_ganhador(tab))
            print('Turno do computador (' + dif + '):')
            mov_auto = obter_movimento_auto(tab, cria_peca('O'), dif)
            tab = move_peca(tab, mov_auto[0], mov_auto[1])
            print(tabuleiro_para_str(tab))
            if not pecas_iguais(obter_ganhador(tab), cria_peca(' ')):
                return peca_para_str(obter_ganhador(tab))
        if jog == '[O]':
            print('Turno do computador (' + dif + '):')
            mov_auto = obter_movimento_auto(tab, cria_peca('X'), dif)
            tab = move_peca(tab, mov_auto[0], mov_auto[1])
            print(tabuleiro_para_str(tab))
            if not pecas_iguais(obter_ganhador(tab), cria_peca(' ')):
                return peca_para_str(obter_ganhador(tab))
            mov = obter_movimento_manual(tab, cria_peca(jog[1]))
            tab = move_peca(tab, mov[0], mov[1])
            print(tabuleiro_para_str(tab))
            if not pecas_iguais(obter_ganhador(tab), cria_peca(' ')):
                return peca_para_str(obter_ganhador(tab))