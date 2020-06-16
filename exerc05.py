from modulos import modulos05

imposto = int(input('Digite um valor para o imposto, apenas o numero: '))
print(f'Ok, você escolheu {imposto}% de imposto sobre a mercadoria. ')
valor_mercadoria = int(input('Digite o valor da mercadoria, apenas o numero: '))
print(f'Ok, o valor da mercadoria é R$ {valor_mercadoria},00. ')
resultado = modulos05.calculo(valor_mercadoria,imposto)
print(f'O valor da mercadoria junto com o imposto é de R$ {resultado}')