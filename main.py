import leitura  # para ler gramatica do arquivo
import impressao # para imprimir gramatica na tela
import chomsky
import sys  #argumentos por linha de comando

# Colocar 'True' quando quiser passar o nome do arquivo como argumento do programa (no terminal)
nome_arquivo_por_argumento = False

# caminho do arquivo que contem a gramatica
if(nome_arquivo_por_argumento):
  if(len(sys.argv) < 2):
    print("Erro! Formato: "+sys.argv[0]+" arquivo")
    exit(1)
  nome_gramatica = sys.argv[1]
else:
  # Pede o nome do arquivo ao usuario
  nome_gramatica = input("Digite o nome do arquivo de gramatica: ")


###
###

# Le a gramatica do arquivo
resultado_leitura = leitura.ler_gramatica(nome_gramatica)

# Imprime a gramatica na tela
impressao.imprimir_gramatica(resultado_leitura)

# Chomsky
resultado_leitura = chomsky.chomsky(resultado_leitura)

# Imprime a gramatica na tela
impressao.imprimir_gramatica(resultado_leitura)


