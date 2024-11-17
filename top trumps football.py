import random, os, time
print("Top Trumps\n ----------------------")

print("The category is Premier league football players")
time.sleep(5)
os.system("clear")
def prettyprint():
  
     print(f"Name\tSpeed\tDefending\tShooting")
     print("-" *60)

     for players, value in pfootball["players"].items():
        print(f"{players:<15}\t\t{value['Speed']}\t{value['Defending']}\t{value['Shooting']}")

pfootball = {
    "players": {
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
}

prettyprint()
print()
print("Loading game")
time.sleep(8)
os.system("clear")
while True:
  print("Choosing your player\n")
  player = random.choice(list(pfootball["players"].keys()))
  oplayer = random.choice(list(pfootball["players"].keys()))
  if oplayer != player:
    for players, value in pfootball.items():
      print(f"You're {player}\n")
      print(f"Speed: {pfootball['players'][player]['Speed']}\n")
      print(f"Defending: {pfootball['players'][player]['Defending']}\n")
      print(f"Shooting:  {pfootball['players'][player]['Shooting']}")
      print()
      print(f"Opponent {oplayer}\n")
      print(f"Speed: {pfootball['players'][oplayer]['Speed']}\n")
      print(f"Defending: {pfootball['players'][oplayer]['Defending']}\n")
      print(f"Shooting: {pfootball['players'][oplayer]['Shooting']}\n")
  
      
      if (
          
        pfootball['players'][player]['Speed'] + 
        pfootball['players'][player]['Shooting'] + 
        pfootball['players'][player]['Defending']
                   >
        pfootball['players'][oplayer]['Speed'] + 
        pfootball['players'][oplayer]['Shooting'] + 
        pfootball['players'][oplayer]['Defending']
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