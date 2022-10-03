from string import ascii_lowercase

#menu
print("Que tipo de operação?: ")
print("1: Criptografar")
print("2: Descriptografar\n")
opcao = input('Operação: ')

if opcao == str(1) or opcao == str(2):

    frase = str.lower(input('Escreva uma mensagem: \n'))
    rot = int(input('Digite uma chave: '))

    if opcao == str(1):
        # Criptografar
        crip = ''
        for letra in frase:
            if letra == '':
                crip += letra
            elif letra not in ascii_lowercase:
                crip += letra
            else:
                pos = ascii_lowercase.find(letra) + rot
                letra = ascii_lowercase[pos % 26]
                crip += letra
        print(crip)

    if opcao == str(2):
        # Descriptografar
        descrip = ''
        for letra in frase:
            if letra == '':
                descrip += letra
            elif letra not in ascii_lowercase:
                descrip += letra
            else:
                pos = ascii_lowercase.find(letra) - rot
                letra = ascii_lowercase[pos % 26]
                descrip += letra
        print(descrip)
