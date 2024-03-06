
# Para a sequência a) 1, 3, 5, 7... ( esta adicionando 2 ao número anterior)
def proximo_elemento_sequencia_a(numero_anterior):
    return numero_anterior + 2

# Para a sequência b) 2, 4, 8, 16, 32... ____ (cada número é o dobro do anterior)
def proximo_elemento_sequencia_b(numero_anterior):
    return numero_anterior * 2

# Para a sequência c) 0, 1, 4, 9... (parecem ser os quadrados dos números naturais)
def proximo_elemento_sequencia_c(numero_anterior):
    return (numero_anterior + 1) ** 2

# Para a sequência d) 4, 16, 36...(parecem ser os quadrados dos números pares)
def proximo_elemento_sequencia_d(numero_anterior):
    return (numero_anterior + 2) ** 2

# Para a sequência e) 1, 1, 2...(parece ser a sequência de Fibonacci)
def proximo_elemento_sequencia_e(numero_anterior):
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if b > numero_anterior:
            return b

# Para a sequência f) 2,10... (números crescentes alternados)
def proximo_elemento_sequencia_f(numero_anterior):
    if numero_anterior % 2 == 0:
        return numero_anterior + 2
    else:
        return numero_anterior + 1


print("Próximo elemento da sequência a):", proximo_elemento_sequencia_a(7))
print("Próximo elemento da sequência b):", proximo_elemento_sequencia_b(64))
print("Próximo elemento da sequência c):", proximo_elemento_sequencia_c(36))
print("Próximo elemento da sequência d):", proximo_elemento_sequencia_d(64))
print("Próximo elemento da sequência e):", proximo_elemento_sequencia_e(8))
print("Próximo elemento da sequência f):", proximo_elemento_sequencia_f(19))
