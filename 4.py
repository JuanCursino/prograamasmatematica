# Programa para realizar operações de conjunto

conjunto1 = {1, 2, 3, 6, 8}
conjunto2 = {2, 4, 5, 6, 9}

uniao = conjunto1.union(conjunto2)         
intersecao = conjunto1.intersection(conjunto2)  
diferenca = conjunto1.difference(conjunto2)    

print(f"Conjunto 1: {conjunto1}")
print(f"Conjunto 2: {conjunto2}")
print(f"União: {uniao}")
print(f"Interseção: {intersecao}")
print(f"Diferença (Conjunto 1 - Conjunto 2): {diferenca}")

# Um conjunto é uma coleção não ordenada de elementos distintos,
# essas operações são conceitos na teoria dos conjuntos da matemática discreta.

