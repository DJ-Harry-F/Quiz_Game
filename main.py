print("Welcome to my computer quiz!")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")
score = 0

answer = input("What operating system am i on? ")
if answer == "Windows 10":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does MB stand for? ")
if answer == "Mega bites":
   print('Correct!')
else:
    print("Incorrect!")


answer = input("what coding language do i use the most? ")
if answer == "Python":
   print('Correct!')
else:
    print("Incorrect!")

answer = input("what type of phone do i have? ")
if answer == "Samsung S10":
   print('Correct!')
else:
    print("Incorrect!")
