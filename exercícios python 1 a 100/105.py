def notas(*n, sit=False):
    boletim = {}
    boletim['total'] = len(n)
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['media'] =sum(n) / len(n)
    if sit:
        if boletim['media'] >= 5 and boletim['media'] <= 6:
            boletim['situação'] = 'rasoavel'
        elif boletim['media'] >=2:
            boletim['situação'] = 'ruim'
        elif boletim['media'] >=7 and boletim['media'] <=8:
            boletim['situação'] = 'boa'
        elif boletim['media'] >= 9:
            boletim['situação'] = 'muito boa'
    return boletim




resp = notas(5.5,7,8,2.2,9,10,0,sit=True)
print(resp)

