'''
Jogo da forca
Autor: Gustavo Carvalho (Pukki)
'''

# -=:[___________Desenho_____________]:=-
man = [' ' for x in range(7)] # Partes atuais do stick
part = [ '|', 'O', '|', '/', '\\', '/', '\\' ] # Partes do stick para adicionar
def draw(): # Função para atualizar o desenho
    print(
    """
    JOGO DA FORCA
 +---+
 {0}   |
 {1}   |
{3}{2}{4}  |
{5} {6}  |
     |
=========
    """.format(man[0], man[1], man[2], man[3], man[4], man[5], man[6]) )

forca = """
JOGO DA FORCA
+---+
    |
    |
    |
    |
    |
=========
"""
# ---------------------------------------
def ask(): # Pergunta o usuário a palavra e atribui a mesma à uma variável
    print("Digite apenas letras.\n")
    # Verifica se a palavra contém apenas letras se não executa a função novamente
    global word
    word = input("Digite sua palavra:")
    word = list( word ) if word.isalpha() else ask()
    return word
ask()
lines = ['_' for x in range( len( word ) )] # Converte o número de letras para "_" para formar o jogo
tentativas = 0
acertos = 0
erros = 0
errlist = []
maxErr = 7 if len( word ) > 7 else len( word ) # Define o limite de erros
def put(): # Nossa função que contém o algorítmo do jogo
    char = input('Digite uma letra:') # Pede uma letra para advinhar
    if isinstance(char, str) and len(char) == 1 and char.isalpha() : # Verifica se é a letra é mesmo uma letra e tem somente um caractére
        # Pegamos as variáveis fora do escopo da função
        global tentativas
        global erros
        tentativas += 1 # Inserimos uma tentativa
        if not char in word: # Se não existir essa letra na palavra saímos logo da função e adicionamos um erro
            man[erros] = part[erros] # Inserimos a parte do stick no desenho
            draw() # Atualizamos o desenho
            erros += 1
            errlist.append(char) # Colocamos a palavra na lista de erros
            return
        for l in word: # Itera sobre nossa palavra para as verificações e substituições
            if char == l: # Se a letra se encontra na nossa palavra:
                lines.pop(word.index(l)) # Retira um ponto da forca no exato local para inserir adiante a letra
                lines.insert(word.index(l), l) # Insere a letra no correto local da forca
                # -=:[_Verifica se há letras iguais na palavra e coloca-as em seu devido lugar_]:=-
                wi = word.index(l) # Pega o index da letra na lista word
                word.pop(wi) # Tira da lista
                word.insert(wi, '-') # Insere uma string qualquer no local pra manter a posição das outras letras
                # -----------------
                global acertos # Pegamos a variável acertos fora do escopo da função
                acertos += 1 # Inserimos um acerto
        draw()
        return
    print("INSIRA UMA LETRA!") # Se o jogador não digitar uma letra, exibimos seu erro e executamos novamente o jogo
    put()

print(forca) # Mostra a forca limpa
# Enquanto as linhas da forca não estiverem totalmente preenchida ou exceder o número de erros:
while( acertos != len(word) and erros != maxErr ):
    # Mostramos na tela as tentativas, erros e acertos do jogador
    print("\nTentativas: {0} | Acertos: {1} ({2}) | Erros: {3} ({4}) {5}".format(tentativas, acertos, str( len(word) ), erros, str( maxErr ),
                                                                                 '['+', '.join( errlist )+']' if len( errlist ) != 0 else '' ) )
    # Mostra na tela as linhas da forca
    print( '\n'+' '.join(lines) ) 
    print('\n')
    put() # Executa o código

if erros == maxErr: # Se você tiver errado o suficiente:
    print("Você perdeu =(")
else: # Se não:
    print("Parabéns, você ganhou!")
