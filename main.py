# Definicao da classe
class Producao():

	def __init__(self, variavel, terminais):
	        self.variavel = variavel
	        self.terminais = terminais

# Fim da definicao da classe


#  Exemplo de arquivo:
#  [ S ] -> [ A ] [ B ] [ a ]
#  [ S ] -> [ b ]
#  [ A ] -> [ a ]
#  [ B ] -> [ b ]
#  [ B ] -> [ V ] 
#

lista_producoes = []

variavel = 'S'
terminais = []
terminais.append('A')
terminais.append('B')
terminais.append('a')
producao = Producao(variavel, terminais) #cria a producao

lista_producoes.append(producao) # add a producao na lista

variavel = 'S'
terminais = []
terminais.append('b')
producao = Producao(variavel, terminais) #cria a producao

lista_producoes.append(producao) # add a producao na lista

variavel = 'A'
terminais = []
terminais.append('a')
producao = Producao(variavel, terminais) #cria a producao

lista_producoes.append(producao) # add a producao na lista

variavel = 'B'
terminais = []
terminais.append('b')
producao = Producao(variavel, terminais) #cria a producao

lista_producoes.append(producao)

variavel = 'B'
terminais = []
terminais.append('V')
producao = Producao(variavel, terminais) # add a producao na lista




print ("fim.")
