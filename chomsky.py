import inuteis
import copy

from leitura import Producao

# Chomsky ETAPA 2 (etapa 1 é a simplificação)
# Recebe:
#  gramatica:
#   [ terminais, variaveis, inicial, regras ]
# Retorna:
#  gramatica:
#   [ terminais, variaveis, inicial, regras ]
def chomskye2(gramatica):
    terminais = gramatica[0]
    variaveis = gramatica[1]
    inicial = gramatica[2]
    regras = gramatica[3]
    t1 = []

    for regra in regras:
      if len(regra.cadeia_simbolos) > 1:     #se o comprimento da produção for >= 2
        for i, simbolo in enumerate(regra.cadeia_simbolos):
          if simbolo in terminais:
            regra.cadeia_simbolos[i] = 'C' + simbolo  #transforma ele em no formato Cterminal, exemplo, terminal = a, Ca
            aux = copy.copy(regra.cadeia_simbolos[i])
            if not simbolo in t1:
              variaveis.append(aux)
              t1.append(simbolo)            #adiciona o simbolo num vetor para saber quais regras já foram criadas
              producao = Producao(aux, simbolo)          #cria regra Ca -> a
              regras.append(producao)

    return [terminais, variaveis, inicial, regras]
##fim da funcao


# Chomsky ETAPA 3
# Recebe:
#  gramatica:
#   [ terminais, variaveis, inicial, regras ]
# Retorna:
#  gramatica:
#   [ terminais, variaveis, inicial, regras ]
def chomskye3(gramatica):
  terminais = gramatica[0]
  variaveis = gramatica[1]
  inicial = gramatica[2]
  regras = gramatica[3]
  cont_nome = 1 #variavel para nomear as novas variaveis que surgem nesta etapa do algoritmo
  aux = 0
  cardinalidade = 0
  anterior = 0

  while (True):
      for regra in regras:
          if len(regra.cadeia_simbolos) > 2:
            while len(regra.cadeia_simbolos) > 2: #se o lado direito da producao for > 2, transformar em producao de tamanho 2
                nova = 'T' + str(cont_nome) 
                cont_nome += 1
                variaveis.append(nova) #adiciona a nova variavel na lista de variaveis
                cadeia = [regra.cadeia_simbolos[1], regra.cadeia_simbolos[2]]
                producao = Producao(nova, cadeia)
                regras.append(producao)
                regra.cadeia_simbolos[1] = nova
                del regra.cadeia_simbolos[2]
                cardinalidade +=1

      if cardinalidade <= anterior: #testa se o numero de producoes que chegam em vazio nao aumentou
          break
      else: #se aumentou, então repete o loop
          anterior = cardinalidade

  return[ terminais, variaveis, inicial, regras]

#fim da etapa 3 do algoritmo de Chomsky


# Algoritmo de Chomsky (utiliza as duas etapas acima)
# Recebe:
#  gramatica:
#   [ terminais, variaveis, inicial, regras ]
# Retorna:
#  gramatica:
#   [ terminais, variaveis, inicial, regras ]
def chomsky (gramatica):
  gramatica = inuteis.deleta_inuteise2(gramatica)
  terminais = gramatica[0]
  variaveis = gramatica[1]
  inicial = gramatica[2]
  regras = gramatica[3]
  retorno = 1


  for regra in regras:
      if regra.variavel == inicial:
          if (len(regra.cadeia_simbolos) == 1 and regra.cadeia_simbolos[0] == 'V'): #se tiver vazio
              retorno = 0

  if retorno == 0:
      print ('-----------------------------')
      print ("A gramática após chomsky é: ")
      print ()
      print ("A gramática possue o simbolo vazio portanto a FNC não é valida")
      print ('-----------------------------')
      print()
      print ("A gramática após a simplificação é: ")
      print ()
  else:
    print ('-----------------------------')
    print()
    print ("A gramática após a simplificação é: ")
    print ()
    print("Terminais:")
    for terminal in terminais:
      print(terminal)
    #
    print("Variaveis:")
    for variavel in variaveis:
      print(variavel)
    #
    print("Inicial:")
    print(inicial)
    #
    print("Regras:")
    for regra in regras:
      print(regra.variavel + ' -> ', end='')
      for simbolo in regra.cadeia_simbolos:
        print(simbolo ,end='')
      print()
    print ('-----------------------------')
    print ("A gramática após Chomsky é: ")
    print()
      
    gramatica = chomskye2(gramatica)
    gramatica = chomskye3 (gramatica)
    terminais = gramatica[0]
    variaveis = gramatica[1]
    inicial = gramatica[2]
    regras = gramatica[3]

  return [terminais, variaveis, inicial, regras]
# Fim Algoritmo de Chomsky