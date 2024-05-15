numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
operacao = input('digite a operação +, - ou *: ')

resultado = 0

def multiplicacao():
    global resultado
    resultado = numero1 * numero2
    
def soma():
    res = numero1 + numero2
    return(res)

def subitracao(n1, n2):
    return n1 - n2

if operacao == '+':
    resultado = soma()
elif operacao == '-':
    resultado = subitracao(numero1, numero2)
elif operacao == '*':
    multiplicacao()
else:
    print('operação invalida!')
    
print(resultado)