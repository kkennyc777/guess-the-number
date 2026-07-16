import random
import time
#variables
player_name = ""
attempts = 10
failed_attempts = 0
game_won = False
#Mostrar Bienvenida
print ("Welcome to Guess the Number!")
time.sleep (1)
#Pedir Nombre
player_name = input ("What's your name? ")
time.sleep(1)
print ("Good Luck " + player_name + "!")
#Generar Numero Secreto
secret_number = random.randrange(101)
#Loop
time.sleep(1)
while attempts > 0 and not game_won:
    player_guess = int(input ("Guess the number! between 0 and 100: "))
    if player_guess > 100:
        failed_attempts +1
        if failed_attempts == 3:
            attempts -1
            failed_attempts = 0
            print ("You have loss an attempt, please input a correct number")
    elif secret_number < player_guess:
        attempts -=1
        time.sleep(0.5)
        print ("Try a Lower number!")
        print("Remaining attempts: " + str(attempts))
    elif secret_number > player_guess:
        attempts -=1
        time.sleep (0.5)
        print ("Try a Higher number!")
        print("Remaining attempts: " + str(attempts))
    elif secret_number == player_guess:
        game_won = True
        print ("Congratulations! you have won the game.")


#Inicializar Intentos
#Preguntar el número del jugador
#Ganó?
#Dar Pista
#Actualizar Intentos
#Repetir