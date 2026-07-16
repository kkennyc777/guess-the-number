import random
import time
#variables
player_name = ""
attempts = 10
failed_attempts = 0
game_won = False
#Mostrar Bienvenida
print ("Welcome to Guess the Number!")
time.sleep (0.5)
#Pedir Nombre
player_name = input ("What's your name? ")
time.sleep(0.5)
print ("Good Luck " + player_name + "!")
time.sleep(0.5)
print ("Please choose a number between 0 and 100.")
#Generar Numero Secreto
secret_number = random.randrange(101)
#Loop
time.sleep(0.5)
while attempts > 0 and not game_won:
    #Preguntar el número del jugador
    try:
        player_guess = int(input ("Your number: "))
    except ValueError:
        print("Please enter a valid number")
        time.sleep(0.5)
        failed_attempts += 1
        if failed_attempts == 3:
            attempts -= 1
            failed_attempts = 0
            print ("You have loss an attempt, please enter a valid number")
            time.sleep(0.5)
            print("Remaining attempts: " + str(attempts))
            time.sleep(0.5)           
        continue
    if player_guess > 100:
        print ("Please enter a valid number.")
        failed_attempts +=1
        if failed_attempts == 3:
            attempts -=1
            failed_attempts = 0
            print ("You have loss an attempt, please enter a valid number")
            time.sleep(0.5)
            print("Remaining attempts: " + str(attempts))
            time.sleep(0.5)
    #Dar Pista
    elif secret_number < player_guess:
        #Actualizar Intentos
        attempts -=1
        time.sleep(0.5)
        print ("Try a Lower number!")
        time.sleep(0.5)
        print("Remaining attempts: " + str(attempts))
        time.sleep(0.5)
    #Dar Pista
    elif secret_number > player_guess:
        #Actualizar Intentos
        attempts -=1
        time.sleep (0.5)
        print ("Try a Higher number!")
        time.sleep(0.5)
        print("Remaining attempts: " + str(attempts))
        time.sleep(0.5)
    else:
        secret_number == player_guess
        #Ganó?
        game_won = True
        print ("Congratulations! you have won the game.")