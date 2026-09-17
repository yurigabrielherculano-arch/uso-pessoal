from biblioteca.system import cabeçario
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('houve um erro ao criar arquivo')
    else:
        print(f'arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('erro ao ler arquivo')
    else:
        cabeçario('pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado [1] = dado [1].replace('\n', '')
            print(f'{dado[0]:8}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('houve um arro na abertura no arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('houve um erro na hora de escrever no arquivo')
        else:
            print(f'novo registro de {nome}')
            a.close()


