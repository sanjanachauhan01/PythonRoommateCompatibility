import compatibility

def information(): 
  print("\nPlease enter your information for the following questions")

  "Shower preference (night shower or morning shower"
  
  shower = input("Enter 'Y' if you shower at night, and 'N' if you don't: \n").lower()
  valid_answers = ["y", "n"]
  while shower not in valid_answers:
    shower = input("Please try again, enter either 'Y' or 'N'").lower()
  nightShower = False
  if (shower == 'y'):
    nightShower = True

    "Cleanliness from scale of 1-10"
  
  clean = input("Rate how clean you keep your room by entering a number between 1-10:  \n")
  while not clean.isdigit() or int(clean) < 1 or int(clean) > 10:
    clean = input("Entering a number between 1-10:  \n")
  clean = int(clean)

  "Temperature in farenheit"
  
  temp = input("Please enter what temperature, in F,  you prefer to keep your room at: \n")
  while not temp.isdigit():
    temp = input("Please enter a valid temperature")
  temp = int(temp)
  "Pet in dorm, yes or no"
  
  pet = input("If you are bringing a pet or are okay with your roommate having a pet, please enter 'Y', else, 'N': \n").lower()
  while pet not in valid_answers:
    pet = input("Please try again, enter either 'Y' or 'N'").lower()
  yesPet = False
  if (pet == 'y'):
    yesPet = True
  
  sleep = input("Please enter the time you go to sleep in military time (ex 11pm is 23) \n")
  clock = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
  while not sleep.isdigit() or int(sleep) not in clock:
    sleep = input("Please try again and enter a valid time")
  sleep = int(sleep)
  
  awake = input("PLease enter the time you wake up in military time (ex 11pm is 23) \n")
  while not awake.isdigit() or int(awake) not in clock:
    awake = input("Please try again and enter a valid time")
  awake = int(awake)
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
  
  
  
  
  
  
  
  
  