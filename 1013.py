"""
Enunciado

Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.

Entrada

O arquivo de entrada contém três valores inteiros.

Saída

Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

CÓDIGO FONTE
"""
values=input().split(" ")
values=[int(item) for item in values]

high=0;

for item in values:
    if item > high:
        high=item

print(f"{high} eh o maior")