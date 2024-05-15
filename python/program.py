# nomes = ['aline', 'rita', 'ana', 'sergiio', 'gustavo', 'bernado', 'bruno']

# for n in nomes:
#     print(n)
    
    
# numero = int(input("digite um numero: "))

# for n in range(1, 11):
#     resultado = numero * n
#     print(f"{numero} * {n} = {resultado}")
    
    
qtdNotas = int(input("quantas notas: "))


arn = []

for n in range(qtdNotas):
    notas = int(input("nota: "))
    arn.append(notas)

for a in arn:
    calc = a + a 
    media = calc / qtdNotas

print(media)