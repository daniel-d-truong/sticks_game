import random

main = [1,1]
opponent = [1,1]

def Game():
  flag = True
  temp = random.randint(0,1)
  boo = [True, False]
  turn = boo[temp]

  print ("Directions: State ATTACK if you would like to attack your opponent. State SPLIT if you would like to split your hand. Remember, you are only allowed to a split when you have one hand with an even numbered amount of finger. State QUIT if you give up. ")
  print ("Your hand: \t\t", end='')
  print (main)
  print ("Opponent's hand: \t", end='')
  print (opponent)
  print ("--------------------------------------------------")

  while (flag == True):
    if (turn == True):
      print ("Your turn!")
      response = input ("Action: ")
      response = response.upper()
      if (response == "ATTACK"):
        Attack()
      elif (response == "SPLIT"):
        turn = Split(main, turn)
      elif (response == "QUIT"):
        print ("Game Over! You lose :( ")
        flag = False
      else:
        print ("Error. Try again!")
        turn = not turn

      print ("Your hand: \t\t", end='')
      print (main)
      print ("Opponent's hand: \t", end='')
      print (opponent)
      if (opponent.count(0) == 2):
        print ("You Win!")
        flag = False
      turn = not turn #switches turns

    else:
      print ("Opponent's turn!")
      CalculateBestMove()
      print ("Your hand: \t\t",end='')
      print (main)
      print ("Opponent's hand: \t", end='')
      print (opponent)
      if (main.count(0) == 2):
        print ("You Lose :( Better luck next time.")
        flag = False
        main[0] = 1
        main[1] = 1
        opponent[0] = 1
        opponent[1] = 1
      turn = not turn #switches turns
    print ("--------------------------------------------------")

  again = input ("Would you like to play again? (Y to play again, any other key to quit): ")
  if (again == 'Y'):
    print ("Let's Play!")
    print ("**************************************************")
    Game()
  else:
    print ("Thank you for playing!")
    return

def Attack():
  i = ["L", "R"]
  if (main.count(0) == 0):
    action = input ("You attack with (L or R): ")
    while (i.count(action) == 0):
      action = input ("Error. Only pick L or R. You attack with (L or R): ")
  else:
    print ("You attack with: ", end='')
    action = i[1-main.index(0)]
    print (action, end=" (Set by default)\n")

  if (opponent.count(0) == 0):
    victim = input ("You attack your opponent's (L or R): ")
    while (i.count(victim) == 0):
      victim = input ("Error. Only pick L or R. You attack with (L or R): ")

  else:
    print ("You attack your opponent's: ", end='')
    victim = i[1-opponent.index(0)]
    print (victim, end=" (Set by default)\n")

  temp = opponent[i.index(victim)] + main[i.index(action)]
  if (temp < 5):
    opponent[i.index(victim)] = temp
  else:
    opponent[i.index(victim)] = 0

  print ("ATTACK successful.")

def Split(hand, t): #must be even, this could be changed
  if (hand.count(0) == 0):
    if (t == True):
      print ("Unallowed to SPLIT. You have 2 hands available.")
    globTurn = not t
    return globTurn

  comp = 1-hand.index(0)
  half = hand[comp]/2

  if (hand[comp] % 2 == 0):
    hand[0] = int (half)
    hand[1] = int (half)
    print ("SPLIT successful.")
    return t
  else: #if this is changed to allow odd number splits, must account for how computer will always split if it has one hand
    if (t == True):
      print ("Unallowed to SPLIT. The amount of fingers in your hand must be even.")
    globTurn = not t
    return globTurn

def OppAttack(a, b): #a=hand of player to attack, b=hand opponent uses to atack
  item = ["L", "R"]
  print ("Opponent attacks with: ", end='')
  print (item[b])
  print ("Opponent attacks: ", end='')
  print (item[a])

  temp = main[a]+opponent[b]
  if (temp >= 5):
    main[a] = 0
  else:
    main[a] = temp

  print ("ATTACK successful")

def CalculateBestMove():
  if (CanWinTheGame() == True):
    return
  if (AvoidLosing() == True):
    return
  if (Split(opponent, False) == False): #if turn doesn't change, that means able to split
    print ("Opponent SPLITS.")
    return


  temp1 = random.randint(0,1) #player's hand
  temp2 = random.randint(0,1) #opponent's hand
  if (main.count(0) == 1):
    temp1 = 1 - main.index(0)
  if (opponent.count(0) == 1):
    temp2 = 1-opponent.index(0)
  OppAttack(temp1, temp2)


def CanWinTheGame():
  if (main.count(0) == 1):
    if main[1 - main.index(0)] + opponent[0] >= 5:
      OppAttack(1-main.index(0), 0)
      return True
    elif main[1 - main.index(0)] + opponent[1] >= 5:
      OppAttack(1-main.index(0), 1)
      return True
  return False

def AvoidLosing():
  if (opponent.count(0) == 1):
    temp0 = opponent[1-opponent.index(0)] + main[0]
    temp1 = opponent[1-opponent.index(0)] + main[1]
    if (temp0 >= 5 or temp1 + opponent[1-opponent.index(0)] == 5):
      OppAttack(0, 1-opponent.index(0))
      return True
    elif (temp1 >= 5 or temp0 + opponent[1-opponent.index(0)] == 5):
      OppAttack(1, 1-opponent.index(0))
      return True

  return False

Game()
