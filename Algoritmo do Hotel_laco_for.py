# Pergunta ao usuário em qual andar ele está
andar_usuario = int(input("Em que andar você está? "))

# Mensagem informativa
print(f"Você está no {andar_usuario}º andar. Desça mais um andar até chegar no 0º (térreo).")

# Laço para descer andares, exceto o 13
for i in range(andar_usuario, -1, -1):
    if i == 13:
        print("Esse andar está indisponível, vá para o próximo.")
        continue
    
    print(f"Você está no {i}º andar.")
    
    # Solicita o próximo andar
    novo_andar = int(input("Para qual andar você quer ir agora? Digite o nº do seu próximo andar, por gentileza: "))
    
    if novo_andar > i:
        print("Você só pode descer para andares abaixo do atual.")
        continue
    elif novo_andar == 13:
        print("Esse andar está indisponível, vá para o próximo.")
        continue
    elif novo_andar < 0:
        print("Não há andares abaixo do térreo. Você deve parar no 0º andar.")
        novo_andar = 0
    
    if novo_andar == 0:
        print("Chegamos ao térreo, não há mais andares disponíveis, é hora de descer!")
        break
    
    # Atualiza o andar atual
    i = novo_andar
