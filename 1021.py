"""
Enunciado

Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2.
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada

O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída

Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.
Obs: Utilize ponto (.) para separar a parte decimal.

CÓDIGO FONTE
"""
cedulas={"100":0,"50":0,"20":0,"10":0,"5":0,"2":0}
cedulas_values=[100,50,20,10,5,2]
moedas={"1.0":0,"0.5":0,"0.25":0,"0.1":0,"0.05":0,"0.01":0}
moedas_values=[1.0,0.5,0.25,0.1,0.05,0.01]

valor = float(input())

for cedula in cedulas_values:
    while True:
        if(valor >= cedula):
            cedulas[str(cedula)]+=1
            valor-=cedula
        else:
            break

for moeda in moedas_values:
    while True:
        if(valor >= moeda):
            moedas[str(moeda)]+=1
            valor-=moeda
        else:
            break

print("NOTAS:")
for item in cedulas:
    print(f"{cedulas[item]} nota(s) de R$ {float(item):.2f}")

print("MOEDAS:")
for item in moedas:
    print(f"{moedas[item]} moeda(s) de R$ {float(item):.2f}")