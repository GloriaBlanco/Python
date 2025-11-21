import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# a variavel number = recebe um numero aleatório entre 1 e 10
number = random.randint(1,10)

# variavel isGuessRight recebe o valor False para poder entrar na loop
isGuessRight = False

# loop wh
while isGuessRight != True:
    # variavel guess recebe a entrada do usuário
    guess = input("Guess a number between 1 and 10: ")
    # condicional If/Se o que voce digitou = guess é == igual ao numbero variavel number entra no comando seguinte, senão vai pro else
    if int(guess) == number:
        # entrou aqui significa que acertou o numero
        print("You guessed {}. That is correct! You win!".format(guess))
        # informa a variavel isGuessRight = true para ele nao entrar no loop while novamente
        isGuessRight = True
    # se nao entrou no if acima entrara aqui    
    else:
        # informa que nao acertou o numero e retorna para o loop while acima
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

# obs: ele só sai do loop doo while quando acertar o numero
