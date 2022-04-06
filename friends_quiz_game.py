print("Can you pass the 'Friends' game quiz!")

playing = input("Do you want to play? ").lower()
if playing.lower() != "yes":
    quit()
print ("OK! Let's play:)")
score= 0

answer = input("1. Which character has a twin ")
if answer.lower() == "phoebe":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
    
    
answer = input("2. Who was Monica's first kiss ")
if answer.lower() == "chandler":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
    

answer = input("3. What is the name of Phoebe's jingle honoring her mother the cat? ")
if answer.lower() == "smelly cat":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
    

answer = input("4. What is Joey's favorite food? ")
if answer.lower() == "sandwiches":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

answer = input("5. How many sisters does Joey have? ")
if answer == "7":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

answer = input("6. Who hates Thanksgiving? ")
if answer.lower() == "chandler":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

answer = input("7. Who is the manager of Central Perk? ")
if answer.lower() == "gunther":
    print("Correct!")
    score +=  1 
else:
    print("Incorrect!")

answer = input("8. How may friends are there? ")
if answer.lower() == "6":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

answer = input("9. Who does Gunther have a crush on? ")
if answer.lower() == "rachel":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

answer = input("10. What is the name of the coffee shop that the friends always go to? ")
if answer.lower() == "central perk":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str(score/10*100) + "%.")
