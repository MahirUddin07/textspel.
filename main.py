print('Välkommen till spelet Flykten till frihet!')
name = input('Vad vill du ha för username?: ')
age = int(input('Hur gammal är du?: '))

if age >= 15:
    print('Du får börja spela!')
elif age < 15:
    print('Tyvärr kan ej spelas! ')

with open('Resemål', 'r') as file:
    lista = file.read().splitlines()

resmål = input('Vart vill du resa?: ')

if resmål == 'Resmål1':
    for Resmål1 in lista:
        print(Resmål1)

elif resmål == 'Resmål2':
    for Resmål2 in lista:
        print(Resmål2)

elif resmål == 'Resmål3':
    for resmål3 in lista:
        print(Resmål3)

elif


elif


elif

elif

elif

elif

else:
    print('Resmålet är inte känt.')




