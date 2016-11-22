import copy
import leitura


# Elimina produções vazias ETAPA 1
# Recebe:
#  gramatica:
#   [ terminais, variaveis, inicial, regras ]
# Retorna:
#  gramatica com variaveis que atigem simbolo vazio:
#   [ terminais, variaveis, inicial, regras, vars_simb_vazios ]
def deleta_vaziose1 (gramatica):
    terminais = gramatica[0]
    variaveis = gramatica[1]
    inicial = gramatica[2]
    regras = gramatica[3]
    v1 = [] #lista de variaveis Vε
    auxregras = copy.copy(regras)
    cardinalidade = 0 #flag para manter o loop
    anterior = 0
    is_empty = 1



    while (True):
        for i,regra in enumerate(auxregras):
            if len(regra.cadeia_simbolos) == 1:
                if (regra.cadeia_simbolos[0] in v1) or (regra.cadeia_simbolos[0] == 'V'):
                    if not regra.variavel in v1:
                        v1.append(regra.variavel) #adiciona as variaveis que vão para o simbolo vazio 
                        del auxregras[i] #deleta regra original depois de adicionar em v1
                        cardinalidade += 1
                        continue

            else:
                for simbolo in regra.cadeia_simbolos: #testa cadeia de simbolos nas producoes procurando simbolos de vazio
                        if simbolo in v1:
                            continue
                        else:
                            is_empty = 0


                if is_empty == 1: #se a producao atingir um simbolo vazio, adicionar no vetor vε
                    if not regra.variavel in v1:
                        v1.append(regra.variavel) #adiciona as variaveis que atingem um simbolo vazio indiretamente
                    del auxregras[i]
                    cardinalidade += 1
                    continue

        is_empty = 1 #reinicia a variavel para proxima iteracao

        if cardinalidade <= anterior: #testa se o numero de producoes que chegam em vazio nao aumentou
            break
        else: #se aumentou, então repete o loop
            anterior = cardinalidade


            
    return [terminais, variaveis, inicial, regras, v1]
##fim da função


# Eliminação de produções vazias ETAPA 2  (utiliza ETAPA 1 acima)
# Recebe:
#  gramatica com variaveis que atigem simbolo vazio:
#   [ terminais, variaveis, inicial, regras, vars_simb_vazios ]
# Retorna:
#  gramatica com variaveis que atigem simbolo vazio:
#   [ terminais, variaveis, inicial, regras, vars_simb_vazios ]
def deleta_vaziose2(gramatica):
    resultado_leitura = deleta_vaziose1(gramatica)
    terminais = resultado_leitura[0]
    variaveis = resultado_leitura[1]
    inicial = resultado_leitura[2]
    regras = resultado_leitura[3]
    vempty = resultado_leitura[4]
    cadeiasimbolos = []
    cardinalidade = 0
    anterior = 0

    is_equal = 0



    while (True):
      for i, regra in enumerate(regras):   ##exlui todas as regras que são do formato 'variavel -> vazio'
        for simbolo in regra.cadeia_simbolos:
            if simbolo == 'V':
              del regras[i]
              cardinalidade +=1
            elif simbolo in vempty and len(regra.cadeia_simbolos) > 1:  ##acrescenta as producoes substituindo variaveis por vazio
                  for simbolos in regra.cadeia_simbolos:
                    if simbolos != simbolo:
                      cadeiasimbolos.append(simbolos)
                  producao = leitura.Producao(regra.variavel, cadeiasimbolos)
                  for auxregra in regras:
                      if auxregra.variavel == regra.variavel:
                          if (auxregra.cadeia_simbolos == cadeiasimbolos):
                            is_equal = 1
                            
                  if is_equal == 0:
                    regras.append(producao)
                    cardinalidade +=1
                  cadeiasimbolos = []
                  is_equal = 0
      if cardinalidade <= anterior: #testa se o numero de producoes que chegam em vazio nao aumentou
              break
      else: #se aumentou, então repete o loop
              anterior = cardinalidade

    return [terminais, variaveis, inicial, regras, vempty]
                            

##fim da função
  
# Eliminação de producoes vazias ETAPA 3 (utiliza ETAPA 2 acima)
# Recebe:
#  gramatica com variaveis que atigem simbolo vazio:
#   [ terminais, variaveis, inicial, regras, vars_simb_vazios ]
# Retorna:
#  gramatica com variaveis que atigem simbolo vazio:
#   [ terminais, variaveis, inicial, regras, vars_simb_vazios ]
def deleta_vaziose3(gramatica):
    resultado_leitura = deleta_vaziose2(gramatica)
    terminais = resultado_leitura[0]
    variaveis = resultado_leitura[1]
    inicial = resultado_leitura[2]
    regras = resultado_leitura[3]
    vempty = resultado_leitura[4]

    if inicial in vempty:         ##insere a producao V na variavel inicial caso necessário
      producao = leitura.Producao(inicial, 'V')
      regras.append(producao)

    return [terminais, variaveis, inicial, regras, vempty]
##fim da funcao
