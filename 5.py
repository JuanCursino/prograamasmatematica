def soma(n):
    return sum(i for i in range(1, n) if n % i == 0)

def numeros_amigos(a, b):
    return soma(a) == b and soma(b) == a

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numeros_amigos(numero1, numero2):
    print(f"{numero1} e {numero2} são números amigáveis.")
else:
    print(f"{numero1} e {numero2} não são números amigáveis.")
    
# Números amigáveis são um conceito em teoria dos números, uma parte da matemática discreta.


