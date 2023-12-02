# Solicitar ao usuário o início e o final do intervalo
start = int(input("Digite o início do intervalo: "))
end = int(input("Digite o final do intervalo: "))

# Gerar listas de números pares e ímpares usando compreensão de lista
pares = [num for num in range(start, end+1) if num % 2 == 0]
impares = [num for num in range(start, end+1) if num % 2 != 0]

# Imprimir os resultados
print(f"Números pares no intervalo: {pares}")
print(f"Números ímpares no intervalo: {impares}")

# O programa utiliza a teoria dos conjuntos,
# onde números pares e ímpares são conjuntos distintos dentro de um intervalo.