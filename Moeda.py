def aumentar(preço=0, taxa=0, formato=False):
    resultado = preço + (preço * taxa/100)
    return resultado if formato is False else moeda(resultado)


def dobro(preço=0, formato=False):
    resultado = preço * 2
    return resultado if not formato else moeda(resultado)


def metade(preço, formato=False):
    resultado = preço / 2
    return resultado if not formato else moeda(resultado)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')  #formata


def diminuir(preço=0, taxa=0, formato=False):
    resultado = preço - (preço * taxa / 100)
    return resultado if formato is False else moeda(resultado)

def resumo(preço=0, taxaa=10, taxab=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Aumentar 10%: \t\t{aumentar(preço, taxaa, True)}')
    print(f'Diminuir 10%: \t\t{diminuir(preço, taxab, True)}')
    print('-' * 30)
