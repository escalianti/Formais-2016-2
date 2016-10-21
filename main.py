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

import leitura
