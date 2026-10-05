# Batalha Naval

> **Aviso:** esta versão é uma porcaria, bem simples, feita só para a avaliação.
> Se quiser ver algo interessante, vá em **https://github.com/audreifilhorossato/batalha-naval**

Jogo de Batalha Naval para o terminal, feito em Python. Você contra o computador.

## Arquivos

- `programa.py`: o jogo (é este que você roda)
- `funcoes.py`: as funções usadas pelo jogo

Os dois precisam estar na mesma pasta.

## Como rodar

```
python programa.py
```

## Como jogar

1. **Posicione sua frota.** Para cada navio, informe a linha (0 a 9), a coluna (0 a 9) e a orientação (`1` vertical, `2` horizontal). O submarino não pede orientação.

   | Navio            | Tamanho | Quantidade |
   |------------------|---------|------------|
   | Porta-aviões     | 4       | 1          |
   | Navio-tanque     | 3       | 2          |
   | Contratorpedeiro | 2       | 3          |
   | Submarino        | 1       | 4          |

2. **Ataque.** A cada rodada, escolha uma linha e uma coluna do tabuleiro do oponente (à direita).
3. **O oponente ataca de volta** uma posição sorteada do seu tabuleiro (à esquerda).
4. Quem afundar todos os navios do outro primeiro vence.

## Legenda

- `0`: água (ou posição ainda não atacada)
- `1`: seu navio
- `X`: tiro que acertou um navio
- `-`: tiro na água

## Observações

- A frota do oponente é sempre a mesma.
- Por causa do `random.seed(1)` em `programa.py`, o oponente ataca sempre na mesma ordem. Para ataques diferentes a cada partida, apague essa linha.
- Digite apenas números: letras ou campo vazio fazem o programa parar com erro.