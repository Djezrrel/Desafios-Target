def fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

# alterar o -numero- conforme desejado
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
print(fibonacci(numero))
