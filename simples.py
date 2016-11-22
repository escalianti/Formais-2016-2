import vazios
import leitura

# Definicao da classe
class Fecho():
    def __init__(self,variavel,cadeia_fecho):
        self.variavel = variavel
        self.cadeia_fecho = cadeia_fecho
# Fim da definicao da classe

# Exclusao de producoes que substituem variaveis
# Recebe:
#  gramatica:
#   [ terminais, variaveis, inicial, regras ]
# Retorna:
#  gramatica com fechos:
#   [ terminais, variaveis, inicial, regras, fechos ]
def subs_variaveis (gramatica):
    gramatica = vazios.deleta_vaziose3(gramatica)
    terminais = gramatica [0]
    variaveis = gramatica [1]
    inicial = gramatica [2]
    regras = gramatica [3]
    cardinalidade = 0
    anterior = 0

#ETAPA 1: CRIA O FECHO DIRETO DE CADA VARIAVEL
    fecho = [] #cria o fecho de variaveis
    for variavel in variaveis: #percorre as variaveis
        fecho_var = []
        for regra in regras: #percorre as regras
            if regra.variavel == variavel:
                if len(regra.cadeia_simbolos) == 1:
                    if (regra.cadeia_simbolos[0] in variaveis) and (not (regra.cadeia_simbolos[0] == variavel)):
                        fecho_var.append(regra.cadeia_simbolos[0])
        novo = Fecho(variavel,fecho_var)
        fecho.append(novo)

    while (True):
        for fechos in fecho:  ##para cada variavel
          for cadeia in fechos.cadeia_fecho: ##para cada variavel pertencente ao fecho da variavel fechos
                for auxfechos in fecho:  ##percorre o vetor de fechos
                    if cadeia == auxfechos.variavel: ##se a variavel pertencente ao fecho da variavel fechos for igual a variavel cadeia
                      for cadeiafechos in auxfechos.cadeia_fecho:
                        if (cadeiafechos != fechos.variavel and (not cadeiafechos in fechos.cadeia_fecho)):
                            fechos.cadeia_fecho.append(cadeiafechos)
                            cardinalidade +=1
        if cardinalidade <= anterior: #testa se o numero de producoes que chegam em vazio nao aumentou
                  break
        else: #se aumentou, então repete o loop
                  anterior = cardinalidade


    return [terminais, variaveis, inicial, regras, fecho]
                    
#FIM DA ETAPA 1

# ETAPA 2  (utiliza ETAPA 1 acima)
# Recebe:
#  gramatica com fechos:
#   [ terminais, variaveis, inicial, regras, fechos]
# Retorna:
#  gramatica:
#   [ terminais, variaveis, inicial, regras ]
def subs_variaveise2 (gramatica):
    gramatica = subs_variaveis(gramatica)
    terminais = gramatica [0]
    variaveis = gramatica [1]
    inicial = gramatica [2]
    regras = gramatica [3]
    fechos = gramatica[4]
    cardinalidade = 0
    anterior = 0
    is_equal = 0
  

    while (True):
      for i,  regra in enumerate(regras):  ##passa por todas as regras
        if len(regra.cadeia_simbolos) == 1 and regra.cadeia_simbolos[0] in variaveis: ##se for no formato A -> B
          for fecho in fechos: ##percorre os fechos
            if regra.variavel == fecho.variavel: ## se o fecho for da regra.variavel
              for var in fecho.cadeia_fecho:  ##passa por todos os fechos dessa variavel
                for auxregra in regras: ##percorre todas as regras
                  if auxregra.variavel == var:  ##se a auxregra.variavel for igual a uma variavel do fecho
                    if (len(auxregra.cadeia_simbolos) == 1 and auxregra.cadeia_simbolos[0] in variaveis):
                      continue
                    prod = leitura.Producao(regra.variavel, auxregra.cadeia_simbolos)
                    for reg in regras:
                      if reg.variavel == regra.variavel and auxregra.cadeia_simbolos == reg.cadeia_simbolos: ##procura se já existe tal regra
                        is_equal = 1
                    if is_equal ==0:  ##se não, adiciona
                      regras.append(prod)
                      cardinalidade +=1
                    is_equal = 0
          del regras[i]
      if cardinalidade <= anterior: #testa se o numero de producoes que chegam em vazio nao aumentou
                  break
      else: #se aumentou, então repete o loop
                  anterior = cardinalidade

    return [terminais, variaveis, inicial, regras]
#FIM DA ETAPA 2