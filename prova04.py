inicio = int(input('Digite o inicio da sequência: '))
fim = int(input('Digite o fim da sequência: ')) + 1
soma = 0

if fim < inicio:
    print("O numero de fim deve ser maior ou igual ao de inicio")     

else:
    for i in range(inicio, fim):
        if i % 2 == 0:
            soma += i

    if soma != 0:
        print(f'A soma dos números pares desta sequência é {soma}')
    else:
        print("Não há números pares no intervalo.") 
