import compatibility


def information(): 
  print("\nPlease enter your information for the   following questions")
  shower = input("Enter 'Y' if you shower at night, and 'N' if you don't: \n")
  nightShower = False
  if (shower == "Y" or shower == "N"):
    if(shower == "Y"):
      nightShower = True
  else:
    print("Wrong input, try program again")
    quit()
  clean = input("Rate how clean you keep your room by entering a number between 1-10:  \n")
  try:
    clean = int(clean)
  except(ValueError):
    print("Not a valid input, quitting program")
    quit()         
  check = False
  for x in range(1,11):
    if x == clean:
      check = True
  if(not check):
    print("Wrong input, try program again")
    quit()
  temp = input("Please enter what temperature, in F,  you prefer to keep your room at: \n")
  try:
    temp = int(temp)
  except ValueError:
    print("Something went wrong")
    quit()
  pet = input("If you are bringing a pet or are okay with your roommate having a pet, please enter 'Y', else, 'N': \n")
  yesPet = False
  if (pet == 'Y' or pet == 'N'):
    if(pet == 'Y'):
      yesPet = True
  else:
    print("Something went wrong")
    quit()
  sleep = input("Please enter the time you go to sleep in military time (ex 11pm is 23) \n")
  try:
    sleep = float(sleep)
  except ValueError:
    print("Something went wrong")
    quit()
  clock = []
  validInput = False
  for x in range(0,24):
    clock.append(x)
  for t in clock:
    if (sleep == t):
      validInput = True
  if not validInput:
    print("That's not a valid time, quiting program")
    quit()
  validInput = False
  awake = input("PLease enter the time you wake up in military time (ex 11pm is 23) \n")
  try:
    awake = float(awake)
  except ValueError:
    print("Something went wrong")
    quit()
  for t in clock:
    if (awake == t):
      validInput = True
  if not validInput:
    print("That's not a valid time, quiting program")
    quit()
  return [nightShower, clean, temp, yesPet, sleep, awake]
  
  
    
print("Hello, and welcome to the Roommate Compatibility Program")
num = input("Please enter '1' if you want to check your compatibility with your roommate: \n")
if(num == '1'):
  print("Please start by answering the following questions with your own prefereances or answers")
  roommate1 = information()
  print("Thank you. Now please answer the following questions with your roommates preferences or answers")
  roommate2 = information()
  print("Thank you, please wait as we calculate the compatibility")
  r1 = compatibility.Roommate(roommate1)
  r2 = compatibility.Roommate(roommate2)
  percent = r1.compare(r2)
  print(str(percent) + "% compatibility")
  
  
  
  
  
  
  
  
  