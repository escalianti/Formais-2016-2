import re  #importa regex

# Definicao da classe
class Producao():

	def __init__(self, variavel, cadeia_simbolos):
	        self.variavel = variavel
	        self.cadeia_simbolos = cadeia_simbolos

# Fim da definicao da classe


#  Exemplo de arquivo:
#  [ S ] -> [ A ] [ B ] [ a ]
#  [ S ] -> [ b ]
#  [ A ] -> [ a ]
#  [ B ] -> [ b ]
#  [ B ] -> [ V ]
#


def ler_gramatica(caminho_arquivo):
	leitura_atual = ''   #controle o que esta sendo lido (terminais, variaveis, etc)
	terminais = []
	variaveis = []
	inicial = ''
	regras = []

	with open(caminho_arquivo) as arquivo:
	   for linha in arquivo:
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

nome_gramatica = input("Digite o nome do arquivo de gramatica: ")

resultado_leitura = ler_gramatica(nome_gramatica)

terminais = resultado_leitura[0]
variaveis = resultado_leitura[1]
inicial = resultado_leitura[2]
regras = resultado_leitura[3]


print("Terminais:")
for terminal in terminais:
	print(terminal)

print("Variaveis:")
for variavel in variaveis:
	print(variavel)

print("Inicial:")
print(inicial)

print("Regras:")
for regra in regras:
	print(regra.variavel + ' -> ', end='')
	for simbolo in regra.cadeia_simbolos:
		print(simbolo ,end='')
	print()
