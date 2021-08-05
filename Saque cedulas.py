c100=0
c50=0
c20=0
c10=0
c5=0
c2=0
c1=0
valor_saque = int(input('Qual o valor que deseja sacar? \n'))
maximo_cedula = int(input('Qual o valor máximo da cédula que deseja receber? (1 - 2 - 5 - 10 - 20 - 50 - 100) \n'))
while maximo_cedula !=1 and maximo_cedula!=2 and maximo_cedula!=5 and maximo_cedula!=10 and maximo_cedula!=20 and maximo_cedula!=50 and maximo_cedula !=100:
    print ('Valor de cédula inexistente')
    maximo_cedula = int(input('Qual o valor máximo da cédula que deseja receber? (1 - 2 - 5 - 10 - 20 - 50 - 100) \n'))
while valor_saque<maximo_cedula:
    maximo_cedula = int(input('Valor do saque menor que a cédula escolhida. Qual o valor máximo da cédula que deseja receber? (1 - 2 - 5 - 10 - 20 - 50 - 100 \n'))
n_cedula = int(valor_saque/maximo_cedula)
if valor_saque % maximo_cedula ==0:
    print ('Cédulas:')
    print (f'{n_cedula} de R$ {maximo_cedula}')
    exit()
while valor_saque>=1:
    if maximo_cedula == 100:
        while valor_saque>=maximo_cedula:
               valor_saque = valor_saque-100
               c100=c100+1
        while valor_saque >= 50:
               valor_saque = valor_saque - 50
               c50 = c50 + 1
        while valor_saque >= 20:
                valor_saque = valor_saque - 20
                c20 = c20 + 1
        while valor_saque >= 10:
                valor_saque = valor_saque - 10
                c10 = c10 + 1
        while valor_saque >= 5:
                valor_saque = valor_saque - 5
                c5 = c5 + 1
        while valor_saque >= 2:
                valor_saque = valor_saque - 2
                c2 = c2 + 1
        while valor_saque >= 1:
                valor_saque = valor_saque - 1
                c1 = c1 + 1
        print('Cédulas:')
        print(f'{c100} de R$ 100')
        print(f'{c50} de R$ 50')
        print(f'{c20} de R$ 20')
        print(f'{c10} de R$ 10')
        print(f'{c5} de R$ 5')
        print(f'{c2} de R$ 2')
        print(f'{c1} de R$ 1')

    elif maximo_cedula == 50:
        while valor_saque>=maximo_cedula:
            valor_saque = valor_saque-50
            c50=c50+1
        while valor_saque>=20:
            valor_saque = valor_saque-20
            c20=c20+1
        while valor_saque>=10:
            valor_saque = valor_saque-10
            c10=c10+1
        while valor_saque>=5:
            valor_saque = valor_saque-5
            c5=c5+1
        while valor_saque>=2:
            valor_saque = valor_saque-2
            c2=c2+1
        while valor_saque>=1:
            valor_saque = valor_saque-1
            c1=c1+1
        print('Cédulas:')
        print(f'{c50} de R$ 50')
        print(f'{c20} de R$ 20')
        print(f'{c10} de R$ 10')
        print(f'{c5} de R$ 5')
        print(f'{c2} de R$ 2')
        print(f'{c1} de R$ 1')

    elif maximo_cedula == 20:
        while valor_saque>=maximo_cedula:
            valor_saque = valor_saque-20
            c20=c20+1
        while valor_saque>=10:
            valor_saque = valor_saque-10
            c10=c10+1
        while valor_saque>=5:
            valor_saque = valor_saque-5
            c5=c5+1
        while valor_saque>=2:
            valor_saque = valor_saque-2
            c2=c2+1
        while valor_saque>=1:
            valor_saque = valor_saque-1
            c1=c1+1
        print('Cédulas:')
        print(f'{c20} de R$ 20')
        print(f'{c10} de R$ 10')
        print(f'{c5} de R$ 5')
        print(f'{c2} de R$ 2')
        print(f'{c1} de R$ 1')

    elif maximo_cedula == 10:
        while valor_saque >= maximo_cedula:
            valor_saque = valor_saque - 10
            c10 = c10 + 1
        while valor_saque >= 5:
            valor_saque = valor_saque - 5
            c5 = c5 + 1
        while valor_saque >= 2:
            valor_saque = valor_saque - 2
            c2 = c2 + 1
        while valor_saque >= 1:
            valor_saque = valor_saque - 1
            c1 = c1 + 1
        print('Cédulas:')
        print(f'{c10} de R$ 10')
        print(f'{c5} de R$ 5')
        print(f'{c2} de R$ 2')
        print(f'{c1} de R$ 1')

    elif maximo_cedula == 5:
        while valor_saque >= maximo_cedula:
            valor_saque = valor_saque - 5
            c5 = c5 + 1
        while valor_saque >= 2:
            valor_saque = valor_saque - 2
            c2 = c2 + 1
        while valor_saque >= 1:
            valor_saque = valor_saque - 1
            c1 = c1 + 1
        print('Cédulas:')
        print(f'{c5} de R$ 5')
        print(f'{c2} de R$ 2')
        print(f'{c1} de R$ 1')

    elif maximo_cedula == 2:
        while valor_saque >= maximo_cedula:
            valor_saque = valor_saque - 2
            c2 = c2 + 1
        while valor_saque >= 1:
            valor_saque = valor_saque - 1
            c1 = c1 + 1
        print('Cédulas:')
        print(f'{c2} de R$ 2')
        print(f'{c1} de R$ 1')

    elif maximo_cedula == 1:
        valor_saque = valor_saque/1
        print(f'{valor_saque} de R$ 1')