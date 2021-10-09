#cops and robbers game by nick, nikita, kavi, and aaron

#import 
import user
import buildings 

#functions
#motion function contains all cop and robber movements 
def motion(turn_count):
  while turn_count%2 == 0: #even turns are cop
    print("_"*60)#line to separate turns
    print("Cop:")
    print (cop.locate())
    #print grid
    grid(cop,robber,safehouse)
    
    control=str(input("Enter Movement (Up, Down, Left, Right):"))
  #cops controls
    if control.lower()=="up":#walk up
      cop.walk_up()
      turn_count += 1
    elif control.lower()=="down":#walk down
      cop.walk_down()
      turn_count += 1
    elif control.lower()=="left":#walk left
      cop.walk_left()
      turn_count += 1
    elif control.lower()=="right":#walk right
      cop.walk_right()
      turn_count += 1
    else:
      print("You have entered an invalid input")
      turn_count = 0 #restart cops turn until valid input
  while turn_count%2 ==1: #odd turns are robber
    print("_"*60)#line to separate turns
    print("Robber:")
    print(robber.locate())
    #print grid
    grid(cop,robber,safehouse)
    control=str(input("Enter Movement (Up, Down, Left, Right):"))
    #cops controls
    if control.lower() == "up":
      robber.walk_up()
      turn_count += 1
    elif control.lower() == "down":
      robber.walk_down()
      turn_count += 1
    elif control=="left":
      robber.walk_left()
      turn_count += 1
    elif control=="right":
      robber.walk_right()
      turn_count += 1
    else:
      print("You have entered an invalid input")
      turn_count = 1
      


#create a grid to locate users 
def grid(cop,robber,safehouse):
  print()
  rows,cols = (9,9) #set size coordinates
  arr = [['#' for i in range(cols)] for j in range(rows)] # # are blank spaces
  #place positions
  arr[cop.lat][cop.lon] = 'C' #locate cops
  arr[robber.lat][robber.lon] = 'R' #locate robbers
  arr[safehouse.lat][safehouse.lon] = '$' #loate safehouse

  for row in arr: 
    print(row) 
  print()


#Initial Positions
cop = user.Cop_Robber('Cop',4,4) #cop starts between robber and safehouse
robber = user.Cop_Robber ('Robber',0,0)
safehouse=buildings.Safehouse('Safehouse',8,8)

#Main Program

#EIntroduction
print("Welcome to Cops and Robbers!")
print("_"*60)

#Goals
print("There are 2 players - The Cop (C) and the Robber (R)")
print("The Cop's Mission: Catch the Robber")
print("The Robber's Mission: Reach The Safehouse ($) at Coordinates:(1,9) \n")


print("_"*60)
#starting positions
print ('Starting Positions:')
print(cop.locate(),'\n')
print(robber.locate())

#game statements
#while in play
#if turn 0 = cop, if turn = 1 robber
turn_count = 0  
while cop.position()!=robber.position:
  #Alternating Turns in function
  motion(turn_count)
  
  #Game Ending Statements
  if cop.position()==robber.position():
    print("\nCAUGHT!! See you in court...")
    break
  elif safehouse.position()==robber.position():
    print("\nSAFE!!! Play again soon...")
    break
