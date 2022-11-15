import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro')
else:
    print('Tudo OK, consegui asceder o site com sucesso')
    #print(site.read()) #Para ler o conteudo HTML do site