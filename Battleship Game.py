
import random
# -----------------------------------------------------------------------------
# Battleship Game - Assignment 4 - CMPUT 175 - Winter 2015
# -----------------------------------------------------------------------------

class BattleshipGame:
    def __init__(self):
        self.computerShips = {"A":5,
                              "B":4,
                              "S":3,
                              "D":3,
                              "P":2}
        self.userShips = {"A":5,
                          "B":4,
                          "S":3,
                          "D":3,
                          "P":2}
        
        #setup blank 10x10 board
        self.userBoard=[[" " for i in range(10)] for j in range(10)]
        self.computerBoard=[[" " for i in range(10)] for j in range(10)]
        #setup init rounds
        self.rounds=0
        # setup computer and user infor
        self.computerHits=0
        self.computerMiss=0
        self.userHits=0
        self.userMiss=0
       
# ---------------------------------------------------------------------------  

    def incrementRounds(self):
            self.rounds+=1
# ---------------------------------------------------------------------------
            
    def setComputerHitsAndMiss(self):
        self.computerHits=0
        self.computerMiss=0
        for i in range(10):
            for j in range(10):
                # setup computerHits and computerMiss
                if self.userBoard[i][j]=="#":
                    self.computerHits+=1
                elif self.userBoard[i][j]=="*":
                    self.computerMiss+=1
                    
# --------------------------------------------------------------------------

    def setUserHitsAndMiss(self):
        self.userMiss=0
        self.userHits=0
        for i in range(10):
            for j in range(10):
                # setup userHits and userMiss
                if self.computerBoard[i][j]=="#":
                    self.userHits+=1  
                elif self.computerBoard[i][j]=="*":
                    self.userMiss+=1
            
# ---------------------------------------------------------------------------

    def getHits(self,computer):
        # return computer Hits
        if computer:
            return self.computerHits
        # return user Hits
        else:
            return self.userHits
      
# --------------------------------------------------------------------------  
    def getMisses(self,computer):
        # return computer Misses
        if computer:
            return self.computerMiss
        else:
            return self.userMiss
        
# ---------------------------------------------------------------------------

    def drawBoards(self,hide):
        shipsNameDict={"S":"Submarine","D":"Destroyer","A":"Aircraft Carrier","B":"Battleship","P":"Patrol Boat"}
        print ("     Computer's board:          User's board:         at round: ", self.rounds)
        print ("    1 2 3 4 5 6 7 8 9 10      1 2 3 4 5 6 7 8 9 10                   Computer Status:  User Status:")
        labels=['A','B','C','D','E','F','G','H','I','J']
        t=0
        k=0
        for i in range(10):
            print (" %c |" % (labels[i]), end="")   # Computer's board
        #print the board values, and cell dividers
            for j in range(10):
                if self.computerBoard[i][j] == "*" or self.computerBoard[i][j] == "#" or not hide:
                    print (self.computerBoard[i][j]+"|", end="")
                else: 
                    print (' |', end="")   
            print ("   %c |" % (labels[i]), end="") # User's board
        #print the board values, and cell dividers
            for j in range(10):             
                print (self.userBoard[i][j]+"|", end="")
            # implement drawboard    
            if labels[i]=="A":
                print("  Nbr. of hits  :  "+"%02d"%(self.getHits(True))+" "*16+"%02d"%(self.getHits(False)), end="")  
            elif labels[i]=="B":
                print("  Nbr. of misses:  "+"%02d"%(self.getMisses(True))+" "*16+"%02d"%(self.getMisses(False)), end="")
            elif labels[i]=="C":
                print("  Ships sunk    :  "+"%02d"%(len(self.getEnemyFleet(True)[1]))+" "*16+"%02d"%(len(self.getEnemyFleet(False)[1])), end="")
            else:
                # make sure index does not out of range 
                if t < len(self.getEnemyFleet(True)[1]) or k < len(self.getEnemyFleet(False)[1]):
                    if self.getEnemyFleet(True)[1] == [] and self.getEnemyFleet(False)[1] == []: # if both empty
                        print("")
                    else:
                        # find the smallest length, and print out them
                        if len(self.getEnemyFleet(True)[1]) > len(self.getEnemyFleet(False)[1]):
                            # print the rest of the ship of the longer one
                            if k < len(self.getEnemyFleet(False)[1]):   
                                print("                   "+"%-18s"%(shipsNameDict[self.getEnemyFleet(True)[1][t]])+"%-18s"%(shipsNameDict[self.getEnemyFleet(False)[1][k]]), end="")
                                k+=1
                                t+=1
                            else:
                                print("                   "+"%-18s"%(shipsNameDict[self.getEnemyFleet(True)[1][t]]), end="")
                                t+=1
                        # if the length is equal
                        elif len(self.getEnemyFleet(True)[1]) == len(self.getEnemyFleet(False)[1]):
                            print("                   "+"%-18s"%(shipsNameDict[self.getEnemyFleet(True)[1][t]])+"%-18s"%(shipsNameDict[self.getEnemyFleet(False)[1][k]]), end="")
                            t+=1
                            k+=1
                        else:
                            if t < len(self.getEnemyFleet(True)[1]):
                                print("                   "+"%-18s"%(shipsNameDict[self.getEnemyFleet(True)[1][t]])+"%-18s"%(shipsNameDict[self.getEnemyFleet(False)[1][k]]), end="")
                                k+=1
                                t+=1
                            else:  
                                print("                   "+" "*18+"%-18s"%(shipsNameDict[self.getEnemyFleet(False)[1][k]]), end="") 
                                k+=1
            print ("")
# --------------------------------------------------------------------------    
    
    def validatePlacement(self,computer,ship,size,x,y,ori):

        #validate the ship can be placed at the given coordinates
        # and places it if acceptable
        if ori == "v" and x+size > 10:
            return False
        elif ori == "h" and y+size > 10:
            return False
        else:
            if computer:
                board=self.computerBoard
            else:
                board=self.userBoard
            if ori == "v":
                for i in range(size):
                    if board[x+i][y] != " ":
                        return False
            elif ori == "h":
                for i in range(size):
                    if board[x][y+i] != " ":
                        return False
            # announce the ship to be placed
            if computer:
                print ("Computer placing a " + ship)
            else: 
                print ("You placed a " + ship)                
            #place the ship based on valid orientation and coordinates
            if ori == "v":
                for i in range(size):
                    board[x+i][y] = ship[0]
            else: # ori=="h"
                for i in range(size):
                    board[x][y+i] = ship[0]
        return True

# ---------------------------------------------------------------------------       
    def getEnemyFleet(self, computer):
        # returns a list of two lists. The first one has the sunken ships and the second the ships to sink
        if computer:
            fleet=self.userShips
        else:
            fleet=self.computerShips
        toSink=[]
        sunk=[]
        # check all ships in the armada of ennemy in the game instance        
        for ship in fleet.keys():
            if fleet[ship]==0:
                sunk.append(ship)
            else:
                toSink.append(ship)
        return [toSink,sunk]

# ---------------------------------------------------------------------------       
    def checkWinning(self, computer):
        # Check if there are still any pieces of ships left to hit on the board
        # board refers to either the board of the computer (if user is playing) or the user (if computer is playing)
        if computer:
            board=self.userBoard
        else:
            board=self.computerBoard
        # Loop to check all cells in the board
        # if any cell contains a char that is not empty, a miss or a hit return false        
        for i in range(10):
            for j in range(10):
                if board[i][j] != ' ' and board[i][j] != '*' and board[i][j] != '#':
                    return False
        return True

# ---------------------------------------------------------------------------       
    
    def makeA_Move(self, computer, x,y):
        if computer:
            board=self.userBoard
        else:
            board=self.computerBoard
        old=board[x][y]
        if old==" ":
            board[x][y]="*"
        elif old=="*" or old=="#":
            return old
        else:
            board[x][y]="#"
        return old
# ---------------------------------------------------------------------------       

    def checkIfSunk(self, computer,symbol):
        if computer:
            armada=self.userShips
        else:
            armada=self.computerShips
        
        # reduce size left of hit ship and check if sunk
        armada[symbol] -= 1
        if armada[symbol] == 0:
            return True
        return False
# ----------------------------------------------------------------------------
    def getPosition(self,x,y):
        # return the the position without change them
        return self.userBoard[x][y]
        
# ---------------------------------------------------------------------------       
def computerPlaceShips(game,ships):
    # Placing the computer ships in random positions
    for ship in ships.keys():
        #generate random coordinates and validate the postion
        valid = False
        while(not valid):
            x = random.randint(1,10)-1
            y = random.randint(1,10)-1
            o = random.randint(0,1)
            if o == 0: 
                ori = "v"
            else:
                ori = "h"
            valid = game.validatePlacement(True,ship,ships[ship],x,y,ori)
    
# ---------------------------------------------------------------------------       
def userPlaceShips(game,ships):
    # Placing the user ships after asking the coordinates and the orientation of each
    # Coordinates are for the bow
    for ship in ships.keys():
        #get coordinates from user and vlidate the postion
        valid = False
        while(not valid):
            game.drawBoards(True)
            print ("Placing a", ship, "of size", ships[ship])
            # reading coordinates x y of new ship
            shipCoordinates=readCoordinates()
            x=shipCoordinates[0]
            y=shipCoordinates[1]
            # reading orientation of new ship
            validOrientation=False
            while not validOrientation:
                orientation=input("This ship is vertical or horizontal (v,h)? ").lower()
                if orientation == "v" or orientation == "h":
                    validOrientation=True                
            valid = game.validatePlacement(False,ship,ships[ship],x,y,orientation)
            if not valid:
                print ("Cannot place a", ship, "there. Stern is out of the board or collides with other ship.\nPlease take a look at the board and try again.")
                input("Hit ENTER to continue")

    game.drawBoards(False)         # DEBUGGING: Cheating to see where the computer ships are
    input("Done placing user ships. Hit ENTER to continue")

# ---------------------------------------------------------------------------       
def readCoordinates():
    # read coordinates x y on board from user and validate
    validCoordinates=False
    while not validCoordinates:
        cell=input("Enter coordinates x y (x in [A..J] and y in [1..10]):")
        cell=cell.split()
        if len(cell)==2:
            if cell[0].upper() in ['A','B','C','D','E','F','G','H','I','J'] and cell[1].isdigit():
                x=['A','B','C','D','E','F','G','H','I','J'].index(cell[0].upper())
                y=int(cell[1])-1
                if x>=0 and x<=9 and y>=0 and y<=9:
                    validCoordinates=True    
    return [x,y]
# ---------------------------------------------------------------------------       
def userMakesMove(game):
    # ask for coordinates for a move by user and try to make move
    # if move is a hit, check ship sunk and win condition 
    # return if user won 
    moveLigit=False
    while(not moveLigit):
        move=readCoordinates()
        x=move[0]
        y=move[1]
        beforeDropped = game.makeA_Move(False,x,y)
        #displaying current boards
        
        labels=['A','B','C','D','E','F','G','H','I','J']
        if beforeDropped=="*" or beforeDropped == "#":
            print ("Sorry, " + labels[x] + " " + str(y+1) + " was already played. Try again.")
        elif beforeDropped == " ":
            print ("Sorry, " + labels[x] + " " + str(y+1) + " is a miss.")
            moveLigit=True
        else:
            print ("Hit at " + labels[x] + " " + str(y+1))
            if game.checkIfSunk(False,beforeDropped): 
                print (whatShip(beforeDropped) + " sunk")
            moveLigit=True
    #input("Press RETURN to continue")    
    return game.checkWinning(False)        
        
# ----------------------------------------------------------------------
def SetTarget(game,x,y):
    # initial target if false
    target=False
    if game.getPosition(x,y)=="#": 
        # if did a hit, change target to True
        target=True
    return target
        
# ----------------------------------------------------------------------
def TargetMove(game,targetList,x,y):
    # collect four points which around the hit
    # if the point already hit, then ignore them
    if x<9 and game.getPosition(x+1,y)!= "#" and game.getPosition(x+1,y)!= "*":
        targetList.append((x+1,y))
    if x>0 and game.getPosition(x-1,y)!= "#" and game.getPosition(x-1,y)!= "*":
        targetList.append((x-1,y))
    if y>0 and game.getPosition(x,y-1)!= "#" and game.getPosition(x,y-1)!= "*":
        targetList.append((x,y-1))
    if y<9 and game.getPosition(x,y+1)!= "#" and game.getPosition(x,y+1)!= "*":
        targetList.append((x,y+1))
    # delect the same item in the list
    targetList=list(set(targetList))
                
    return targetList
# ------------------------------------------------------------------
def huntPhase(x,y,smallest):
    if x in [0,1,2,3,4,5,6,7,8]:
        if y+smallest <10:
            y+=smallest
        else:
            x+=1
            if smallest == 2 and y == 9:  # if y equal to 9, we start from point 0 in next line
                y=0
            elif smallest ==2 and y ==8:  # if y == 8, we start from point 1 in next line
                y=1
            elif smallest == 2 and y not in [8,9]:
                y+=2  # simply plus 2
            if smallest != 2:  
                y=smallest-(9-y)-1
    elif x == 9 and (9-y)>smallest:
        y+=smallest
    else: # if x, y reach the 9,9 , or out of range, computer goes back to (0,0), and start the hit again
        x=0
        y=0
    return (x,y)
# -------------------------------------------------------------------
def computerMakesMove(game,i,targetList,target,hit,shipSize,huntData,smallest):
    # huntData is use to remember the data of hunt phase
    # generate coordinates for a move by computer and try to make move
    # if move is a hit, check ship sunk and win condition 
    # return if computer won
    Ships = {"A":5,"B":4,"S":3,"D":3,"P":2} 
    # the first hit
    if i==0:
        # the first step is a random 
        moveLigit=False
        while (not moveLigit):
            x=random.randint(1,10)-1
            y=random.randint(1,10)-1
            beforeDropped=game.makeA_Move(True,x,y)
            if beforeDropped!="*" and beforeDropped != "#":
                moveLigit=True
        huntData=(x,y)
        target=SetTarget(game,x,y)  # set target
        if target:  # if computer makes a hit, collect the points around it
            targetList=TargetMove(game,targetList,x,y) 
            hit+=1  # did a hit, hit plus one
    # second move to infinity
    else:
        if target== False:   # if target if false, go hunt phase
            moveLigit=False
            while(not moveLigit):
                huntData=huntPhase(huntData[0],huntData[1],smallest)
                x=huntData[0] # x
                y=huntData[1] # y
                beforeDropped = game.makeA_Move(True,x,y)
                if beforeDropped!="*" and beforeDropped != "#":
                    moveLigit=True
            target=SetTarget(game,x,y)  # check if did a hit
            if target:  # if did a hit, collect points
                targetList=TargetMove(game,targetList,x,y)
                hit+=1 # did a hit, hit plus one
        # target phase           
        elif target==True:
            while True:
                item=targetList[0]
                x=item[0]
                y=item[1]
                beforeDropped = game.makeA_Move(True,x,y)
                if beforeDropped=="*" or beforeDropped=="#":  # if the position already hited, chose the other point
                    targetList.remove(item)
                else:   # if the position is valied, stop the while loop
                    break
            if beforeDropped != " ":   # if did a hit, collect the points, and hit plus one
                hit+=1
                targetList=TargetMove(game,targetList,x,y)
                targetList.remove(item)  
    #displaying current boards
    labels=['A','B','C','D','E','F','G','H','I','J']
    if beforeDropped == " ":
        print ("Sorry computer, " + labels[x] + " " + str(y+1) + " is a miss.")
        
    else:    
        print ("Computer did a Hit at " + labels[x] + " " + str(y+1))
        target=True
        if game.checkIfSunk(True,beforeDropped): # check if the ship is sunk
            print (whatShip(beforeDropped) + " sunk")
            tosink=game.getEnemyFleet(True)[0]
            if "P" in tosink: 
                smallest=2
            elif "S" in tosink or "D" in tosink:
                smallest=3
            elif "B" in tosink:
                smallest=4
            else:
                smallest=5
            shipSize+=Ships[beforeDropped]  # count the size of ships that sunk
            
            if hit <= shipSize:  # if hit less or equal to ships size, leave target and change to hunt phase
                target=False   
                targetList=[]
                hit=0
                shipSize=0
    return (game.checkWinning(True), targetList, target,hit,shipSize,huntData,smallest)   # return all the variables
# ----------------------------------------------------------------------
def whatShip(symbol):
    # converting the symbol of a ship to the full name and returning it
    if symbol == "A":
        ship = "Aircraft Carrier"
    elif symbol == "B":
        ship = "Battleship"
    elif symbol == "S":
        ship = "Submarine" 
    elif symbol == "D":
        ship = "Destroyer"
    elif symbol == "P": 
        ship = "Patrol Boat"
    return ship    
    
# #############################################################################
def main():
    # initial set for target, targetlist,hit and shipSize
    target=False    
    targetList=[]
    hit=0
    shipSize=0
    huntData=(0,0)
    smallest=2
    ships = {"Aircraft Carrier":5,
             "Battleship":4,
             "Submarine":3,
             "Destroyer":3,
             "Patrol Boat":2}    
    game=BattleshipGame()                   # create instance of the game
    computerPlaceShips(game,ships)          # Computer places its armada
    userPlaceShips(game,ships)              # User places the armada
    gameOver=False
    i=0
    # game main loop
    while(not gameOver): 
        game.incrementRounds()
       
        #user move
        winning=userMakesMove(game)
        game.setUserHitsAndMiss()
        game.drawBoards(True)
        #check if user won
        if winning:
            print ("Congratulations! User WON!")
            gameOver=True
        else:
            # display what remains of the fleet
            armada=game.getEnemyFleet(False)
            print ("Ships to sink:[", end="")
            for ship in armada[0]:
                print (whatShip(ship), " ", end="")
            print ("]  Ships sunk:[",end="")
            for ship in armada[1]:
                print (whatShip(ship), " ", end="")
            print("]")
            
        
            #computer move
            infor=computerMakesMove(game,i,targetList,target,hit,shipSize,huntData,smallest)
            # update all the infor data
            winning=infor[0]
            targetList=infor[1]
            target=infor[2]
            hit=infor[3]
            shipSize=infor[4]
            huntData=infor[5]
            smallest=infor[6]
            i+=1
            game.setComputerHitsAndMiss()
            game.drawBoards(True)
        
            #check if computer won
            if winning:
                print ("Sorry! Computer WON! Here is what the board looked like:")
                # display boards without hiding the computer ships
                game.drawBoards(False)
                gameOver=True      
        
        
# ############################################################################# 
    
if __name__=="__main__":
    main()