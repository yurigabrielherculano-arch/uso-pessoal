tabela = 'palmeiras','flamengo','atletico pr','fluminense','bahia','bargantino','cruzeiro','botafogo','corinthians','atletico mg','coritiba','são paulo','vitoria','mirasol','santos','internacional','gremio','vasco','remo','chapecoence'
print('-=-'*14)
print(f'lista dos times do braileirão: {tabela} ')
print('-=-'*14)
print(f'os 5 primeiros são : {tabela[:5]}')
print('-=-'*14)
print(f'os 4 ultimos são : {tabela[16:]}')
print('-=-'*14)
print('os times em ordem alfabetica são :',sorted(tabela))
print('-=-'*14)
for pos, tab in  enumerate(tabela):
    if tab == 'botafogo':
        print(f'o botafogo esta na posião {pos +1}° posiçaõ')