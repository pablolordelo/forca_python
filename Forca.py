from palavra_forca import palavra

letras_usadas = []
chances = 4
ganhou = False

# Criando a lógica do loopu

chances_iniciais = chances

while True:
    for letra in palavra:
        if letra.lower() in letras_usadas:
            print(letra.lower(), end = " ")
        else:
            print("_", end = " ")
        
    print(f" Você tem {chances} chances e utilizou as letras {letras_usadas}")

    # Solicitar que o usuário escolha uma letra
    letra_escolhida = input("Escolha uma letra: ")

    # Salvar letra escolhida
    if letra_escolhida.lower() not in letras_usadas:
        letras_usadas.append(letra_escolhida.lower())

    # Verificar se o usuário errou a letra e reduz uma chance
    if letra_escolhida.lower() not in palavra.lower():
        chances -= 1
    
    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usadas:
            ganhou = False


    if chances == 0 or ganhou == True:
        break


if ganhou:
    print("\n" f"Parabêns, você acertou a palavra:  {palavra} \n")
else:
    print ("\n" f"Você utilizou todas as {chances_iniciais} chances, mas não acertou a palavra: {palavra} e utilizou as letras {letras_usadas} \n")