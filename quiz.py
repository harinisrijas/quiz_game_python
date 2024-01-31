print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print ("Okay! Let's play :)")
score = 0

#question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Oops! Incorrect")
    
#question 2
answer = input("What does AVI stand for? ")
if answer.lower() == "audio video interleave":
    print('Correct!')
    score += 1
else:
    print("Oops! Incorrect")
    
#question 3
answer = input("What does CD stand for? ")
if answer.lower() == "compact disk":
    print('Correct!')
    score += 1
else:
    print("Oops! Incorrect")
 
#question 4   
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Oops! Incorrect")
    
#question 5
answer = input("What does HSS stand for? ")
if answer.lower() == "harini srija s":
    print('Correct!')
    score += 1
else:
    print("Oops! Incorrect")
    
print("You got " + str(score) + "question correct!")
print("You got " + str((score / 5) * 100) + "%.")
