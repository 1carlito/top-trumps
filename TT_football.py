import random, os, time
print("Top Trumps\n ----------------------")



def prettyprint():
  
     print(f"Name\tSpeed\tDefending\tShooting")
     print("-" *60)

     for players, value in PFOOTBALL["players"].items():
        print(f"{players:<15}\t\t{value['Speed']}\t{value['Defending']}\t{value['Shooting']}\n")



PFOOTBALL = {
        "Alexander Isak": {"Shooting": 85, "Speed": 88, "Defending": 50},
        "Emili martinez": {"Shooting": 20, "Speed": 40, "Defending": 90},
        "Bruno Fernandes": {"Shooting": 90, "Speed": 75, "Defending": 65},
        "Ollie Watkins": {"Shooting": 83, "Speed": 85, "Defending": 40},
        "Martin Odegaard": {"Shooting": 87, "Speed": 70, "Defending": 60},
        "Trent A Arnold": {"Shooting": 70, "Speed": 78, "Defending": 85},
        "Alisson Becker": {"Shooting": 15, "Speed": 50, "Defending": 95},
        "Son Heung-min": {"Shooting": 89, "Speed": 90, "Defending": 50},
        "Bernardo Silva": {"Shooting": 85, "Speed": 80, "Defending": 65}
  }


print("The category is Premier league football players")
time.sleep(5)
os.system("clear")

prettyprint()

prettyprint()
print("Loading game")


time.sleep(3)
os.system("clear")
while True:
  print("Choosing your player\n")
  
  player = random.sample(list(PFOOTBALL.keys())2)
  oplayer = random.sample(list(PFOOTBALL.keys())2)

  if oplayer != player:

    for players, in PFOOTBALL.items():
      print(f"You're {player}\n")



      print(f"Speed: {PFOOTBALL[player]['Speed']}\n")
      print(f"Defending: {PFOOTBALL[player]['Defending']}\n")
      print(f"Shooting:  {PFOOTBALL[player]['Shooting']}")
      print()
      print(f"Opponent {oplayer}\n")
      print(f"Speed: {PFOOTBALL[oplayer]['Speed']}\n")
      print(f"Defending: {PFOOTBALL[oplayer]['Defending']}\n")
      print(f"Shooting: {PFOOTBALL[oplayer]['Shooting']}\n")
  

      if (
        PFOOTBALL[player]['Speed'] + 
        PFOOTBALL[player]['Shooting'] + 
        PFOOTBALL[player]['Defending']
                   >
        PFOOTBALL[oplayer]['Speed'] + 
        PFOOTBALL[oplayer]['Shooting'] + 
        PFOOTBALL[oplayer]['Defending']
):            
           print(f"{player} wins!")
           time.sleep(7)
           os.system("clear")
      else:
         print(f"{oplayer} wins!\n")
  else:
    continue
  
    
  time.sleep(7)
  os.system("clear")     
  playagain = input("Play again (Y/N)").upper()
       
  if playagain == "N":
    print("Ok thanks")
    break

  elif playagain == "Y":
    continue
            
  else:
    print("Ivalid input")
    break
