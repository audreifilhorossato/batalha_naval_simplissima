def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])
        elif orientacao == 'horizontal':
            posicoes.append([linha, coluna + i])
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = []
    frota[nome_navio].append(posicoes)
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        tabuleiro.append([0] * 10)

    for navios in frota.values():
        for navio in navios:
            for linha, coluna in navio:
                tabuleiro[linha][coluna] = 1

    return tabuleiro

def afundados(frota, tabuleiro):
    contador = 0
    for navios in frota.values():
        for navio in navios:
            afundado = True
            for linha, coluna in navio:
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
            if afundado:
                contador += 1
    return contador

