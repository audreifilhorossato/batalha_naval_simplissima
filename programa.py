import random
from funcoes import define_posicoes, preenche_frota, posicao_valida, posiciona_frota, faz_jogada, afundados, monta_tabuleiros

random.seed(1)


embarcacoes = [
    ['porta-aviões', 4, 1],
    ['navio-tanque', 3, 2],
    ['contratorpedeiro', 2, 3],
    ['submarino', 1, 4],
]


frota = {}

for nome, tamanho, quantidade in embarcacoes:
    for i in range(quantidade):
        valida = False
        while not valida:
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            if nome == 'submarino':
                orientacao = 'horizontal'
            else:
                opcao = int(input('[1] Vertical [2] Horizontal >'))
                if opcao == 1:
                    orientacao = 'vertical'
                else:
                    orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valida = True
            else:
                print('Esta posição não está válida!')


frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}


tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)


total_navios = 0
for navios in frota_oponente.values():
    total_navios += len(navios)

total_navios_jogador = 0
for navios in frota.values():
    total_navios_jogador += len(navios)

posicoes_atacadas = []
posicoes_oponente = []


jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    posicao_inedita = False
    while not posicao_inedita:
        linha_valida = False
        while not linha_valida:
            linha = int(input('Jogador, qual linha deseja atacar? '))
            if 0 <= linha <= 9:
                linha_valida = True
            else:
                print('Linha inválida!')

        coluna_valida = False
        while not coluna_valida:
            coluna = int(input('Jogador, qual coluna deseja atacar? '))
            if 0 <= coluna <= 9:
                coluna_valida = True
            else:
                print('Coluna inválida!')

        if [linha, coluna] in posicoes_atacadas:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        else:
            posicao_inedita = True

    posicoes_atacadas.append([linha, coluna])
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    else:

        sorteio_valido = False
        while not sorteio_valido:
            linha_op = random.randint(0, 9)
            coluna_op = random.randint(0, 9)
            if [linha_op, coluna_op] not in posicoes_oponente:
                sorteio_valido = True

        posicoes_oponente.append([linha_op, coluna_op])
        print(f'Seu oponente está atacando na linha {linha_op} e coluna {coluna_op}')
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_op, coluna_op)

        if afundados(frota, tabuleiro_jogador) == total_navios_jogador:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False