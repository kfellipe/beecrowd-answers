"""
Enunciado

Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
e informe-o expresso no formato horas:minutos:segundos.

Entrada

O arquivo de entrada contém um valor inteiro N.

Saída

Imprima o tempo lido no arquivo de entrada (segundos),
convertido para horas:minutos:segundos, conforme exemplo fornecido.

CÓDIGO FONTE
"""

sec = int(input())

hor,sec = divmod(sec,3600)
min,sec = divmod(sec,60)

print(f"{hor}:{min}:{sec}")