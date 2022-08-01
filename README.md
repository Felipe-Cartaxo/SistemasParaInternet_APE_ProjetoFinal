# Algoritmo e Programação Estruturada - Projeto Final

### Descrição

* Batalha Naval é um jogo de tabuleiro em que os dois jogadores têm de adivinhar
onde estão localizados os navios do oponente. O objetivo é derrubar primeiro todos
os navios do adversário.

* Desenvolva um programa, utilizando a linguagem Python, que simule o jogo
Batalha Naval, com dois jogadores, onde cada um irá atacar a frota de navios do
outro. O tabuleiro de cada jogador deverá ser representado por uma matriz quadrada de
ordem 10, sendo as linhas identificadas por letras (A a J) e as colunas por números
(1 a 10).
* A frota de cada jogador será composta por navios, onde cada um deles ocupará
uma célula da matriz.
* A quantidade de navios da frota será igual para ambos jogadores e deverá ser
definida pelo usuário no início de jogo (máximo de 10).
* Ao ser iniciado um novo jogo, a frota de cada jogador deverá ser posicionada no
respectivo tabuleiro de forma aleatória pelo computador. Essa alocação deverá ser
feita colocando-se a letra “N” na célula onde ele estiver posicionado. Obs: um
navio não pode ficar encostado em outro (nem adjacente e nem diagonal).
* Após os navios terem sido posicionados, o jogo continua numa série de tiros, que
consiste no jogador escolher uma coordenada (linha x coluna) para tentar atingir
algum navio do oponente.
* Se o tiro for certeiro deverá aparecer a palavra “FOGO” e na posição do tiro ser
exibida a letra “F”. Esse mesmo jogador continuará atirando até errar.
Caso contrário, deverá aparecer a palavra “ÁGUA” e na posição do tiro ser exibido
a letra “A”. Nesse caso, a vez de jogar passará para o outro jogador.
* Os dois tabuleiros devem ficar sempre visíveis na tela. Vale ressaltar que,
inicialmente, as frotas não devem aparecer nos tabuleiros, irão aparecer
gradativamente à medida que os navios forem sendo atingidos.
* O jogo é encerrado quando um jogador afundar todos os navios do seu oponente.
* ATENÇÃO: para fins de teste, o programa deverá permitir tornar visível as frotas.

### Grupo responsável pelo projeto

* Felipe Cartaxo
* Alic
* Franklin
* George Lima

### Funcionalidades adicionais

Além de atender às demandas do projeto, optamos por incluir algumas funcionalidades adicionais, tais como:

<<<<<<< HEAD
* Antes de iniciar a partida propriamente dita, perguntar ao usuário se a partida em questão será uma partida normal ou uma partida de testes. Caso opte pela partida de testes, a localização dos navios será mostrada desde o começo
=======
* Antes de iniciar a partida propriamente dita, perguntar ao usuário se a partidar em questão será uma partida normal ou uma partida de testes. Caso opte pela partida de testes, a localização dos navios será mostrada desde o começo
>>>>>>> b88d818623a3fafec2821a057f17d1bf3067fbd7
* Incluir uma funcionalidade onde, ao final de cada turno, questione se o usuário deseja se render
* Incluir uma funcionalidade onde, ao final de cada um dos turnos, questione se o usuário em questão deseja ou não visualizar a localização dos navios
