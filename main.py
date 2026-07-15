import random
#variables
player_name = ""
secret_number
player_guess
attempts = 10
failed_attempts = 0
game_won = False
#Mostrar Bienvenida
print ("Welcome to Guess the Number!")
#Pedir Nombre
player_name = input ("What's your name? ")
print ("Good Luck " + player_name + "!")
#Generar Numero Secreto
secret_number = random.randrange(101)
#Loop
while attempts > 0 and not game_won:
    player_guess = int(input ("Guess the number! between 0 and 100"))
    if player_guess != int or player_guess < 100:
        failed_attempts +1
        if failed_attempts == 0:
            attempts -1
            print ("You have loss an attempt, please input a correct number")
        print ("Please try with a NUMBER between 0 and 100")
    elif secret_number < player_guess:
        attempts =-1
        player_guess = input ("Try a Lower number!")
    elif secret_number > player_guess:
        attempts =-1
        player_guess = input ("Tru a Higher number!")
    elif secret_number == player_guess:
        game_won = True
        print ("Congratulations! you have won the game.")



#Inicializar Intentos
#Preguntar el número del jugador
#Ganó?
#Dar Pista
#Actualizar Intentos
#Repetir