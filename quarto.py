def descobrir_interruptor():
    # Ligar o primeiro interruptor
    primeiro_interruptor = True

    # Desligar o primeiro interruptor e ligar o segundo
    primeiro_interruptor = False
    segundo_interruptor = True

    # Ir para a sala das lâmpadas
    # Se a lâmpada estiver acesa, o segundo interruptor controla essa lâmpada
    # Se estiver apagada e estiver quente, o primeiro interruptor controla essa lâmpada
    # Se estiver apagada e estiver fria, o terceiro interruptor controla essa lâmpada
    sala_lampadas = input("Digite 'acesa' se a lâmpada estiver acesa, ou 'fria' se estiver fria: ")
    
    if sala_lampadas == "acesa":
        print("O segundo interruptor controla essa lâmpada.")
    elif sala_lampadas == "fria":
        print("O terceiro interruptor controla essa lâmpada.")
    else:
        print("O primeiro interruptor controla essa lâmpada.")

descobrir_interruptor()
