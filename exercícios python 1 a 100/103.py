def ficha(jog='<desconhecido>',gol = 0):
    """
    :param jog: <desconhecido> pro casoi de não digitar nada
    :param gol: recbe 0 para varios parameros
    :param nome: nome do jogador
    :param gol: gol.isnumeric() , se o gol for um numero o int(gol)trandforma rm um numero
    :param else de gol: caso o gol for escrito ex: três ao inves de 3 ele retorna 0
    :param nome.strip(): tira os espaços se tiver vazio retorna desconhecido e o else retorna o gol e o dsconhecido
    o else retorna vazio o nome e o gol
    """
    print(f'jogador {jog} fez {gol} gols')

nome = str(input('nome do jogador:'))
gol = str(input('quantos gols:'))
if gol.isnumeric():   # se o gol for numero numerico ele mostra a quantidade de gols
    gol = int(gol) # é ooq
else:
    gol = 0
if nome.strip() == '':
    ficha(gol= gol)
else:
    ficha(nome,gol)

