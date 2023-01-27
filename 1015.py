"""
Enunciado



Entrada



Saída



CÓDIGO FONTE
"""
p1=input().split(" ")
p2=input().split(" ")
p1=[float(item) for item in p1]
p2=[float(item) for item in p2]

result = (p2[0] - p1[0]) ** 2

result = (p2[1] - p1[1]) ** 2 + result

result = result ** 0.5

print(f"{result:.4f}")