from datetime import datetime
dado = {}
ficha = []
dado['nome'] = str(input('nome: '))
dado['nascimento'] = int(input('nascimento:'))
dado['carteira'] = int(input('carteira  de trabalho [aperte 0 para não/ tem]:'))


dado['idade'] = (datetime.now().year - dado['nascimento'])
if dado['carteira'] != 0:
    dado['contrato'] = int(input('ano de contrato: '))
    dado['salario'] = float(input('salario: '))
    dado['aposentadoria'] = dado['idade'] + ((dado['contrato'] + 35) - datetime.now().year)

ficha.append(dado)
for k,v in dado.items():
    print(f'- {k}: {v}')





















