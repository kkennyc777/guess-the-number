import random
import time
#variables
player_name = ""
attempts = 10
failed_attempts = 0
game_won = False
game_dificulty = 0
#Show Welcome
print ("Welcome to Guess the Number!")
time.sleep(0.5)
#Ask for name
player_name = input ("What's your name?: ")
time.sleep(0.5)
print ("Hi " + player_name + "!")
time.sleep (0.5)
#Set Dificulty
Dificulty = input ("Please type 1, 2 or 3 to choose your dificulty: \n 1(easy): Number Range 100\n 2(medium): Number Range 500\n 3(Hard): Number Range 1000\n : ")
#Generate a random number
if Dificulty == "1":
    game_dificulty += 1
    secret_number = random.randrange(101)
    print ("Please choose a number between 0 and 100.")
    print (secret_number)
elif Dificulty == "2":
    game_dificulty += 2
    secret_number = random.randrange(501)
    print ("Please choose a number between 0 and 500.")
    print (secret_number)
elif Dificulty == "3":
    game_dificulty += 3
    secret_number = random.randrange(1001)
    print(secret_number)
    print ("Please choose a number between 0 and 1000.")
else:
    print ("Please enter a valid number.")
#Loop
time.sleep(1.5)
while attempts > 0 and not game_won:
    #Ask for the player's number
    try:
        player_guess = int(input ("Your number: "))
    #Verify if the user enters text
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
            if attempts == 0:
                print("Game over.")
                SystemExit           
        continue
    #Verify if the user enters a higher number than the specified range
    if game_dificulty == 1 and player_guess > 100:
        print ("Please enter a valid number.")
        failed_attempts +=1
        if failed_attempts == 3:
            attempts -=1
            failed_attempts = 0
            print ("You have loss an attempt, please enter a valid number")
            time.sleep(0.5)
            print("Remaining attempts: " + str(attempts))
            time.sleep(0.5)
    elif game_dificulty == 2 and player_guess > 500:
        print ("Please enter a valid number.")
        failed_attempts +=1
        if failed_attempts == 3:
            attempts -=1
            failed_attempts = 0
            print ("You have loss an attempt, please enter a valid number")
            time.sleep(0.5)
            print("Remaining attempts: " + str(attempts))
            time.sleep(0.5)
    elif game_dificulty == 3 and player_guess > 1000:
        print ("Please enter a valid number.")
        failed_attempts +=1
        if failed_attempts == 3:
            attempts -=1
            failed_attempts = 0
            print ("You have loss an attempt, please enter a valid number")
            time.sleep(0.5)
            print("Remaining attempts: " + str(attempts))
            time.sleep(0.5)
    #Give hint
    elif secret_number < player_guess:
        #Update attempts
        attempts -=1
        time.sleep(0.5)
        print ("Try a Lower number!")
        time.sleep(0.5)
        print("Remaining attempts: " + str(attempts))
        print(secret_number)
        time.sleep(0.5)
    #Give hint
    elif secret_number > player_guess:
        #Update attempts
        attempts -=1
        time.sleep (0.5)
        print ("Try a Higher number!")
        time.sleep(0.5)
        print("Remaining attempts: " + str(attempts))
        print(secret_number)
        time.sleep(0.5)
    elif secret_number == player_guess:
        #Won?
        game_won = True
        print ("Congratulations! you have won the game.")
    else:
        print ("GAME OVER.  Try again!")
