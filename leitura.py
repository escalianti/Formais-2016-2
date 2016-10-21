
def ler_gramatica(caminho_arquivo):
	with open(caminho_arquivo) as arquivo:
	   for linha in arquivo:
	   		itens = linha.split('->')
	   		variavel_temp = itens[0]
	   		cadeia_temp = itens[1]