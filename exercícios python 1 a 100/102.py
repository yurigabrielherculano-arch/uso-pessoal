def fatorial(n, show=False):

    """
    :param n: início da fatorial
    :param show: mostrar a conta ou não
    :return: valor do fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f


print(fatorial(5, show= True))

