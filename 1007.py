"""
Enunciado

Leia quatro valores inteiros A, B, C e D.
A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada

O arquivo de entrada contém 4 valores inteiros.

Saída

Imprima a mensagem DIFERENCA com todas as letras maiúsculas, com um espaço em branco antes e depois da igualdade.


CÓDIGO FONTE
"""

A,B,C,D = int(input()),int(input()),int(input()),int(input())

DIFERENCA = (( A * B ) - ( C * D ))

print(f"DIFERENCA = {DIFERENCA}")