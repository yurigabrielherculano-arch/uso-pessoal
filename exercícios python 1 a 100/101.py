from datetime import date
def voto(ano):
    atual = date.today().year - ano
    if atual >= 16 and atual <= 17:
        return f'vc tem {atual}, voto opcional'
    elif atual >= 18 and atual <= 69:
        return f'vc tem {atual}, voto obrigatorio'
    elif atual <= 15:
        return f'vc tem {atual}, não vota'
    elif atual >= 70:
        return f'vc tem {atual}, voto opcional'


ano = int(input('ano de nascimento:'))
print(voto(ano))








