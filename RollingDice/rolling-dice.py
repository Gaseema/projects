import random
def roll (sides=6):
    num_rolled = random.randit(1,sides)
    return num_rolled
def main():
     sides = 6
     rolling = True
     while rolling:
         roll_again = input("Wanna roll? ENTER=roll. Q=quit. ")
         if roll_again.lower() != "q":
             num_rolled = roll(sides)
             print("You rolled a", num_rolled)
         else:
             rolling = False

     print ("Asanti for playing.")
     
main()                    	