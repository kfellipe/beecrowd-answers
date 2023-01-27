"""
Enunciado

Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada

Leia três valores de ponto flutuante (double) A, B e C.

Saída

Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular".
Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo.
Imprima sempre o final de linha após cada mensagem.

CÓDIGO FONTE
"""
values = input().split(" ")
A,B,C = float(values[0]), float(values[1]), float(values[2])

delta = (B ** 2) - 4 * A * C

if(A == 0 or delta < 0):
    print("Impossivel calcular")
else:
    x1 = (-B + delta ** (1 / 2)) / (2 * A)
    x2 = (-B - delta ** (1 / 2)) / (2 * A)
    print(f"R1 = {x1:.5f}\nR2 = {x2:.5f}")