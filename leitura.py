##
#  Leitura da gramatica a partir de um arquivo de texto
##

import re  #importa regex

# Definicao da classe
class Producao():

  def __init__(self, variavel, cadeia_simbolos):
          self.variavel = variavel
          self.cadeia_simbolos = cadeia_simbolos
# Fim da definicao da classe

# Função para leitura da gramática a partir do arquivo de texto
# Recebe:
#  caminho do arquivo a ser lido
# Retorna:
#  [ terminais, variaveis, inicial, regras ]
def ler_gramatica(caminho_arquivo):
  leitura_atual = ''   #controle o que esta sendo lido (terminais, variaveis, etc)
  terminais = []
  variaveis = []
  inicial = ''
  regras = []

  with open(caminho_arquivo) as arquivo:   #abre o arquivo para leitura
     for linha in arquivo:   # loop que le cada linha do arquivo
         linha = linha.replace(' ', '') #remove espacos da linha
         linha = linha.replace('\t', '') #remove TABS da linha
         if not linha: # pula linha se ela eh vazia
           continue

         if linha.startswith( '#Terminais' ):  #leitura de terminais
           leitura_atual = 'terminais'
           continue
         if linha.startswith( '#Variaveis' ):  #leitura de terminais
           leitura_atual = 'variaveis'
           continue
         if linha.startswith( '#Inicial' ):  #leitura de terminais
           leitura_atual = 'inicial'
           continue
         if linha.startswith( '#Regras' ):  #leitura de terminais
           leitura_atual = 'regras'
           continue

         if leitura_atual is 'terminais':
           linha = re.sub(re.compile("#.*?\n" ) ,"" , linha) # remove comentarios da linha

           linha = linha.replace('[', '').replace(']','')  # remove os []
           terminal = linha
           terminal = terminal.replace("\n", '')
           terminais.append(terminal)

         if leitura_atual is 'variaveis':
           linha = re.sub(re.compile("#.*?\n" ) ,"" , linha) # remove comentarios da linha
           linha = linha.replace('[', '').replace(']','')  # remove os []
           variavel = linha
           variavel = variavel.replace("\n", '')
           variaveis.append(variavel)

         if leitura_atual is 'inicial':
           linha = re.sub(re.compile("#.*?\n" ) ,"" , linha) # remove comentarios da linha
           linha = linha.replace('[', '').replace(']','')  # remove os []
           inicial = inicial.replace("\n", '')
           inicial = linha;

         if leitura_atual is 'regras':
           linha = re.sub(re.compile("#.*?\n" ) ,"" , linha) # remove comentarios da linha
           itens = linha.split('>')  # separa a linha em 2

           variavel = itens[0]   #primeira parte da string
           variavel = variavel.replace('[', '').replace(']','')

           variavel = variavel.replace("\n", '')

           cadeias = itens[1]  #segunda parte da string
           cadeias = cadeias.replace("\n", '')
           regex = re.compile("\[(\w+)\]")   #monta regex pra pegar uma lista do que esta entre []
           lista_cadeias = regex.findall(cadeias)   #aplica o regex

           producao = Producao(variavel, lista_cadeias)  #cria a producao
           regras.append(producao)   #add producao na lista de producoes

  return [ terminais, variaveis, inicial, regras ]  #returna tudo num array simples
#fim ler_gramatica(caminho_arquivo)
