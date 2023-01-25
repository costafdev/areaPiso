from retangulo import Retangulo
import math

print('=-='*25)
while True: #deixa o programa aberto
    pisoladoA = float(input('Digite um lado do piso: '))
    pisoladoB = float(input('Digite um segundo lado do piso: '))
    print('=+='*20)
    piso = Retangulo(pisoladoA, pisoladoB)
    areaPiso = piso.area()
    print('=+='*20)
    azuladoA = float(input('Informe um lado do azuleijo: '))
    azuladoB = float(input('O outro lado: '))
    print('=+='*20)
    azu = Retangulo(azuladoA,azuladoB)
    areaAzu = azu.area()
    print('=+='*20)
    qtdAzu = areaPiso/areaAzu
    if areaPiso%areaAzu == 0:
        print(f'A quantidade certa para preencher o piso sao {qtdAzu} azuleijos')
    else:
        print(f'A quantidade minima é {math.ceil(qtdAzu)}')
