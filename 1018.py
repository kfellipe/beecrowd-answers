"""
Enunciado

Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada

O arquivo de entrada contém um valor inteiro N(0 < N < 1000000)

Saída

Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárioas, conforme o exemplo fornecido.
Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: "Presentation Error".

CÓDIGO FONTE
"""
index=0
array_notas=[100,50,20,10,5,2,1]
notas=[0,0,0,0,0,0,0]
current = array_notas[index]

saque = int(input())
saque_print = saque

while True:
    if(saque >= current):
        notas[index]+=1
        saque-=current
    elif(saque == 0):
        break
    else:
        index+=1
        current=array_notas[index]

index=0
print(f"{saque_print}")
for nota in notas:
    print(f"{nota} nota(s) de R$ {array_notas[index]},00")
    index+=1