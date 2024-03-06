import estado_imc as calcular

peso = 0
altura = 0.0
nome = ""

nome = input("Qual o nome do paciente? ")

erro = True

while erro:

    try:
        peso = int(input("Qual é o peso do paciente ? "))
        erro = False
    except:
        print("Valor do peso inválido!")



erro = True

while erro:
    try:
        altura = float(input("Qual a altura do paciente ? "))
        erro = False

    except:
        print("Valor da altura inválido!")


calcular.calcular_imc(peso,altura)