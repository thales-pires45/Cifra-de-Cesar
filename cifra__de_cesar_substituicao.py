dicionario = {}

dicionario [''] = ''
dicionario ['a'] = 'v'
dicionario ['b'] = 'j'
dicionario ['c'] = 'w'
dicionario ['d'] = 'k'
dicionario ['e'] = 'x'
dicionario ['f'] = 'l'
dicionario ['g'] = 'y'
dicionario ['h'] = 'm'
dicionario ['i'] = 'z'
dicionario ['j'] = 'a'
dicionario ['k'] = 'n'
dicionario ['l'] = 'b'
dicionario ['m'] = 'o'
dicionario ['n'] = 'c'
dicionario ['o'] = 'p'
dicionario ['p'] = 'd'
dicionario ['q'] = 'q'
dicionario ['r'] = 'e'
dicionario ['s'] = 'r'
dicionario ['t'] = 'f'
dicionario ['u'] = 's'
dicionario ['v'] = 'g'
dicionario ['w'] = 't'
dicionario ['y'] = 'h'
dicionario ['x'] = 'u'
dicionario ['z'] = 'i'
dicionario [','] = ','
dicionario ['.'] = '.'
dicionario ['!'] = '!'
dicionario ['ç'] = 'ç'


# Inverter o dicionário para de descriptografar
dicionario_reverso = {str(v): str(k) for k, v in dicionario.items()}

# Menu
print("Que Tipo de Operação?:")
print("1: Criptografar")
print("2: Descriptografar ")
opcao = input('Operação: ')

if opcao == str(1) or opcao == str(2):
    frase = str.lower(input('Escreva a mensagem: '))
    #Criptografado
    if opcao == str(1):
        crip = ""
        for letra in frase:
            if letra in dicionario:
                crip = crip + str(dicionario[letra])
            else:
                crip = crip + letra
        print(crip)

    #Descriptografado
    if opcao == str(2):
       descrip = ""
       for letra in frase:
           if letra in dicionario_reverso:
               descrip = descrip + str(dicionario_reverso[letra])
           else:
               descrip = descrip + letra
       print(descrip)

else:
    print("Erro, digite uma das opções a baixo")



