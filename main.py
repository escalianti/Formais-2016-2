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

lista_producoes = []

variavel = 'S'
cadeia_simbolos = []
cadeia_simbolos.append('A')
cadeia_simbolos.append('B')
cadeia_simbolos.append('a')
producao = Producao(variavel, cadeia_simbolos) #cria a producao

lista_producoes.append(producao) # add a producao na lista

variavel = 'S'
cadeia_simbolos = []
cadeia_simbolos.append('b')
producao = Producao(variavel, cadeia_simbolos) #cria a producao

lista_producoes.append(producao) # add a producao na lista

variavel = 'A'
cadeia_simbolos = []
cadeia_simbolos.append('a')
producao = Producao(variavel, cadeia_simbolos) #cria a producao

lista_producoes.append(producao) # add a producao na lista

variavel = 'B'
cadeia_simbolos = []
cadeia_simbolos.append('b')
producao = Producao(variavel, cadeia_simbolos) #cria a producao

lista_producoes.append(producao)

variavel = 'B'
cadeia_simbolos = []
cadeia_simbolos.append('V')
producao = Producao(variavel, cadeia_simbolos) # add a producao na lista




print ("fim.")
