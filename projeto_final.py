#Grupo B: Alic Victor, Felipe Cartaxo, Franklin Pereira, George Lima

import random
from time import sleep

#Função para gerar uma matriz
def matrizGen (nLin, nCol):
    matriz = [['.'] * nCol for i in range (nLin)]
    return matriz

#Função para imprimir o tabuleiro, devidamente formatado
def printTab (matriz, player):
    tabLin = 'ABCDEFGHIJ'
    tabCol = '1234567890'
    nLin = len(matriz)
    nCol = len(matriz[0])
    print()
    print(f'Tabuleiro de {player}')
    print()
    print(' ', end='')

    #Exibição das colunas formatadas
    for (x) in range (nLin):
        sleep(0.1)
        #'if' para exibir a coluna 10
        if (x == 9):
            print(f'{tabCol[0]:>4}', end='')
            print(f'{tabCol[9]}', end='')
        else:
            print(f'{tabCol[x]:>4}', end='')
    print()

    #Exibição das linhas formatadas
    for (x) in range (nLin):
        sleep(0.1)
        print(f'{tabLin[x]:4}', end='')
        for (y) in range (nCol):
            print(f'{matriz[x][y]:4}', end='')
        print()

#Função para verificar 
def verificar(matriz, linha, coluna):
  
  #Caso esteja no canto superior esquerdo
  if linha == 0 and coluna == 0:
    i = linha
    j = coluna
    k = linha
    l = coluna
    for i in range (k, k+2):
      for j in range (l, l+2):
        if matriz[i][j] == 'N':
          pode = False
          return pode
  
  #Caso esteja na primeira linha, mas não seja nenhum dos dois cantos
  if linha == 0 and coluna > 0 and coluna < 9:
    i = linha
    j = coluna-1
    k = linha
    l = coluna-1
    for i in range (k, k+2):
      for j in range (l, l+3):
        if matriz[i][j] == 'N':
          pode = False
          return pode  
  
  #Caso esteja no canto superior direito
  if linha == 0 and coluna == 9:
    i = linha
    j = coluna-1
    k = linha
    l = coluna-1
    for i in range (k, k+2):
      for j in range (l, l+2):
        if matriz[i][j] == 'N':
          pode = False
          return pode  
  
  #Caso esteja no canto inferior esquerdo
  if linha == 9 and coluna == 0:
    i = linha-1
    j = coluna
    k = linha-1
    l = coluna
    for i in range (k, k+2):
      for j in range (l, l+2):
        if matriz[i][j] == 'N':
          pode = False
          return pode  
  
  #Caso esteja no canto inferior direito
  if linha == 9 and coluna == 9:
    i = linha-1
    j = coluna-1
    k = linha-1
    l = coluna-1
    for i in range (k, k+2):
      for j in range (l, l+2):
        if matriz[i][j] == 'N':
          pode = False
          return pode

  #Caso esteja na primeira coluna, mas não seja nenhum dos dois cantos
  if linha > 0 and linha < 9 and coluna == 0:
    i = linha-1
    j = coluna
    k = linha-1
    l = coluna
    for i in range (k, k+3):
      for j in range (l, l+2):
        if matriz[i][j] == 'N':
          pode = False
          return pode

  #Caso esteja na última coluna, mas não seja nenhum dos dois cantos
  if linha > 0 and linha < 9 and coluna == 9:
    i = linha-1
    j = coluna-1
    k = linha-1
    l = coluna-1
    for i in range (k, k+3):
      for j in range (l, l+2):
        if matriz[i][j] == 'N':
          pode = False
          return pode

  #Caso esteja na última linha, mas não seja nenhum dos dois cantos
  if linha == 9 and coluna > 0 and coluna < 9:
    i = linha-1
    j = coluna
    k = linha-1
    l = coluna
    for i in range (k, k+2):
      for j in range (l, l+2):
        if matriz[i][j] == 'N':
          pode = False
          return pode

  #Caso esteja em qualquer lugar que não seja os anteriores
  if linha > 0 and linha < 9 and coluna > 0 and coluna < 9:
    i = linha-1
    j = coluna-1
    k = linha-1
    l = coluna-1
    for i in range (k, k+3):
      for j in range (l, l+3):
        if matriz[i][j] == 'N':
          pode = False
          return pode
          
  matriz[linha][coluna] = 'N'     
  pode = True
  
  return pode  

#Função para gerar os navios aleatoriamente
def randNavios(qtnavios, matriz):
  navios = 0
  while True:
    linha = random.randint(0,9)
    coluna = random.randint(0,9)
    pode = verificar(matriz, linha, coluna)
    if pode == True:
      navios = navios + 1
      if navios == qtnavios:
        break

#Função para realizar as jogadas
def jogada (matriz, lin, col):
    acertou = True
    while (acertou):
        print()
        if (matriz[lin][col] == 'N'):
            print('FOGO!')
            matriz[lin][col] = 'F'
            break
        elif (matriz[lin][col] == 'A' or (matriz[lin][col] == 'F')):
            print('Você já atirou nesta posição, atire novamente.')
            break
        else:
            acertou = False
            print('ÁGUA!')
            matriz[lin][col] = 'A'
            break
    
    print('-'*45)

    return matriz

#Função para converter o tiro das linhas em um número
def linConv (tiro):
  lin = 'ABCDEFGHIJ'  
  for i in range (10):
    if tiro == lin[i]:
      result = i
      return result

def colConv (tiro):
  for i in range (1, 11):
   if (tiro == i):
    result = i-1
    return result

#Função para verificar se há navios no tabuleiro
def navExist (matriz):
    navCount = 0
    for (x) in range (10):
        for (y) in range (10):
            if (matriz[x][y] == 'N'):
                navCount += 1   
    return navCount

#Função para realizar os respectivos turnos dos jogadores e verificar se há um vencedor
def atirar(matriz, player, matriz_semN, player2):
  vencedor = False
  
  while vencedor == False:
   if (navExist(matriz) == 0):
     vencedor = True
     print()
     print('Fim de jogo!')
     print(f'{player} venceu!')
     print()
     return vencedor    

   print()
   print(f'Turno de {player}!')
   
   #Turno do jogador
   while True:
    tiroLin1 = input('- Linha (A a J): ').upper()
    if tiroLin1 >= 'A' and tiroLin1 <= 'J':
     tiroLin1 = linConv(tiroLin1)
     break
   while True:
    tiroCol1 = int(input('- Coluna (1 a 10) ou 0 para opções: '))
    if tiroCol1 >= 1 and tiroCol1 <= 10:
     tiroCol1 = colConv(tiroCol1)
     break
    if tiroCol1 == 0:
      opcao = int(input("\nDigite 1 para encerrar a partida!\nDigite 2 para mostrar os navios.\nDigite qualquer outro número para voltar ao jogo.\n"))
      if opcao == 1:
        desistencia = 1
        print(f'O jogador {player} desistiu, portanto o vencedor é o jogador {player2}')
        return desistencia
      elif opcao == 2:
        printTab(matriz, player2)
      else:
        continue     
   matriz = jogada(matriz, tiroLin1, tiroCol1)    
   
   #Lógica para computar a jogada
   if (matriz[tiroLin1][tiroCol1] == 'F'):
    matriz_semN[tiroLin1][tiroCol1] = 'F'
    printTab(matriz_semN, player2)
    continue

   else:
    matriz_semN[tiroLin1][tiroCol1] = 'A'
    printTab(matriz_semN, player2)
    return vencedor

# ----------------------- Programa principal ----------------------------
nLin = 10
nCol = 10

print('-------------- BATALHA NAVAL ---------------')
print()

#Leitura dos respectivos nomes dos jogadores
player1 = input('Informe o nome do jogador 1: ').upper()
player2 = input('Informe o nome do jogador 2: ').upper()

#Leitura da quantidade de navios e validação do mesmo
while (True):
        numNavios = int(input('Informe quantos navios cada jogador terá: '))
        if (numNavios > 0 and numNavios <= 10):
            print()
            break
        else:
            print('Valor inválido! Informe um valor inteiro de 1 a 10.')
            print()       

#Geração dos tabuleiros
matrizPlayer1 = matrizGen (nLin, nCol)
matrizPlayer2 = matrizGen (nLin, nCol)
matriz_semN1 = matrizGen (nLin, nCol)
matriz_semN2 = matrizGen (nLin, nCol)

#Geração dos tabuleiros com os navios posicionados
randNavios(numNavios, matrizPlayer1)
randNavios(numNavios, matrizPlayer2)

#Início de partida
vencedor = False

# ----------------------- Início da partida ----------------------------
print('------------ INÍCIO DE PARTIDA -------------')
print('Deseja realizar uma partida de teste? S/N')
test = input().upper()

#Opção para realizar testes, ou seja, para imprimir o tabuleiro com ou sem os navios
if (test == 'S'):
  printTab(matrizPlayer1, player1)
  printTab(matrizPlayer2, player2)

vencedor = False
while vencedor == False:
  vencedor = atirar(matrizPlayer2, player1, matriz_semN1, player2)
  if vencedor == True:
    break 
  vencedor = atirar(matrizPlayer1, player2, matriz_semN2, player1)
  if vencedor == True:
    break

#Impressão dos tabuleiros após o fim da partida
printTab(matrizPlayer1, player1)
printTab(matrizPlayer2, player2)