## Funcoes de impressao de gramatica na tela
#

def imprimir_gramatica(gramatica):
	# Obtem os resultados a partir do array de resultado
	terminais = gramatica[0]
	variaveis = gramatica[1]
	inicial = gramatica[2]
	regras = gramatica[3]

	# Imprime na tela a gramatica
	print("Gramática fornecida: ")
	print()
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