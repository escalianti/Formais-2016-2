import simples

# Funcao para eliminar producoes inuteis
# Recebe:
#  gramatica:
#   [ terminais, variaveis, inicial, regras ]
# Retorna:
#  gramatica:
#   [ terminais, variaveis, inicial, regras ]
def deleta_inuteis (gramatica): #algoritmo para simplificaçao da glc. Etapa 1: exclui simbolos inuteis
    terminais = gramatica [0]
    variaveis = gramatica [1]
    inicial = gramatica [2]
    regras = gramatica [3]
    v1 = [] #conjunto de variaveis que resultam da etapa 1 do algortimo, que sao variaveis que chegam em terminal
    r1 = [] #lista de regras que serão mantidas após exclusão das producoes inuteis
    cardinalidade = 0 #flag para manter o loop
    anterior = 0
    is_inutil = 0


    while (True):
        for i,regra in enumerate(regras):   #testa se tem inumeros terminais encadeados
            is_simb = 1
            for simb in regra.cadeia_simbolos:
              if simb in terminais: 
                continue
              else:
                is_simb = 0
            #testa se vai para apenas uma variavel ou terminal
            if len(regra.cadeia_simbolos) == 1 or is_simb == 1:
                #testa se vai para terminal, vazio ou terminal indiretamente
                prod = regra.cadeia_simbolos[0]
                if (prod == 'V') or (prod in v1) or is_simb ==1:
                    r1.append(regra)
                    if not regra.variavel in v1:
                        v1.append(regra.variavel) #adiciona as variaveis que vão para um terminal diretamente
                    del regras[i] #deleta regra original depois de adicionar em v1
                    cardinalidade += 1
                    continue

            else:
                for simbolo in regra.cadeia_simbolos: #testa cadeia de simbolos nas producoes procurando simbolos inuteis
                    if simbolo in variaveis: #se for uma variável, testa se atinge um terminal
                        if simbolo in v1:
                            continue
                        else:
                            is_inutil = 1
                    else:
                        continue

                if is_inutil == 0: #se a producao atingir um terminal, adicionar na nova gramatica
                    r1.append(regra)
                    if not regra.variavel in v1:
                        v1.append(regra.variavel) #adiciona as variaveis que atingem um terminal indiretamente
                    del regras[i]
                    cardinalidade += 1
                    continue

            is_inutil = 0 #reinicia a variavel para proxima iteracao

        if cardinalidade <= anterior: #testa se o numero de producoes que chegam em terminais nao aumentou
            break
        else: #se aumentou, então repete o loop
            anterior = cardinalidade

 

    return [terminais,v1,inicial,r1] #retorna a nova gramatica num array simples
##fim da funcao



# Começo da etapa 2
# Deleta variaveis que não são atingidas 
# Recebe:
#  gramatica:
#   [ terminais, variaveis, inicial, regras ]
# Retorna:
#  gramatica:
#   [ terminais, variaveis, inicial, regras ]
def deleta_inuteise2 (gramatica):
    gram = simples.subs_variaveise2(gramatica)
    resultado_leitura = deleta_inuteis(gram)
    terminais = resultado_leitura[0]
    variaveis = resultado_leitura[1]
    inicial = resultado_leitura[2]
    regras = resultado_leitura[3]
    v2 = [] #conjunto de variaveis que resultam da etapa 2 do algortimo
    r2 = [] #lista de regras que serão mantidas após exclusão das producoes inuteis
    t2 = [] #lista de terminais que resultam da etapa 2 do algoritmo
    cardinalidade = 0
    anterior = 0

    v2.append(inicial) #adiciona a variavel inicial a v2

  

    while (True):
      for i, regra in enumerate(regras):
        if regra.variavel in v2:        #se a variavel da regra está em v2
          r2.append(regra)
          for simbolo in regra.cadeia_simbolos:          #para cada simbolo gerado pela variavel
            if simbolo in terminais and not simbolo in t2:  #se for terminal e não estiver contido ainda em t2
              t2.append(simbolo)
            elif simbolo in variaveis and not simbolo in v2:  #se for variavel e não estiver contido ainda em v2
              v2.append(simbolo)
          del regras[i]
          cardinalidade +=1
      if cardinalidade <= anterior:
        break
      else:
        anterior = cardinalidade


            
                
    
    return [t2,v2,inicial,r2] 
##fim da função
