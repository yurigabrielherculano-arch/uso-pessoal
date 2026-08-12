from datetime import date
an =int(input("que ano vc quer analidsar?, coloque 0 para analisar o ano atual:"))
if an == 0:
    an = date.today().year
if an % 4 == 0 and an % 10 != 0 or an % 400 == 0:
    print("o ano {} é bissexto".format(an))
else:
    print('o ano {} não é bissexto'.format(an))