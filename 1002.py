"""
Enunciado

A fórmula para calcular a área de uma circuferencia é: area = n * raio ** 2. Considerando para este problema que n = 3.14159
- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por n.

Entrada

A entrada contém um valor de ponto flutuante(dupla precisão), no caso, a variável raio.

Saída

Apresentar a mensagem "A=" seguido pelo valor da variável area, com 4 casas após o ponto decimal.


CÓDIGO FONTE
"""

n = 3.14159

raio = float(input())

area = n * raio ** 2

print(f"A={area:.4f}")