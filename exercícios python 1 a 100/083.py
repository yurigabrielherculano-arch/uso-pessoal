n = str(input('digite uma expressão:'))
pilha = []
for exp in pilha:
    if exp == '(':
        pilha.append(exp)
    elif exp == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(exp)
            break
if len(pilha) == 0:
    print('sua expressão está correta')
else:
    print('sua expressão esta errada')

