ficha = {}
ficha['nome'] = str(input('nome do aluno:'))
ficha['media'] = float(input('media:'))
if ficha['media'] >= 7:
    ficha['situacao'] = 'Aprovado'
elif 5 <= ficha['media'] < 7:
    ficha['situacao'] = 'recuperação'
else:
    ficha['situacao'] = 'Reprovado'
for k,v in ficha.items():
    print(f'{k} é igual a {v}')

