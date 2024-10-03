
print('CALCULADORA DE IMC')

nome = input('Digite seu nome: ').capitalize().strip()
print(f'Seja bem vindo(a), {nome}! \n Para calcular seu IMC iremos precisar de algumas informações: ')

while True:
    try:
        peso = float(input('Qual seu peso? (em kg) '))
        break
    except ValueError:
        print('Tente novamente digitando o peso da forma requerida.')

while True:
    try:
        altura = input('Qual sua altura? (metro e cm, separados por ponto): ')
        if "." in altura:
            altura = float(altura)
            break
        else:
            print("Formato inválido! A altura deve ser no formato decimal (ex: 1.75).")
    except ValueError:
        print("Valor inválido! Por favor, insira um número válido para a altura.")


calculo_imc = peso / (altura ** 2)

if calculo_imc < 20:
    faixa = 'abaixo do peso'
elif 20 <= calculo_imc < 25:
    faixa = 'peso ideal'
elif 25 <= calculo_imc < 30:
    faixa = 'acima do peso'
elif 30 <= calculo_imc < 35:
    faixa = 'obesidade'
else:
    faixa= 'obesidade mórbida'

print('RELATÓRIO FINAL')
print(f'Nome: {nome} \n Peso: {peso} \n Altura: {altura} \n IMC: {calculo_imc :.2f} \n {faixa}')

