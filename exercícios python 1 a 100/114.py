import urllib.request
import urllib
try:
    site = urllib.request.urlopen('https://pudim.com')
except urllib.error.URLError:
    print('\033[0;31mo site pudim não esta funcionando no momento\033[m')
else:
    print('site pudim acessado com sucesso')
    print(site.read())
