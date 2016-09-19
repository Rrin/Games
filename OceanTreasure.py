# 2015/3/7
import random
class OceanTreasure:
    def __init__(self):
        self.__board=[['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]
        # get the treasure coordinates
        self.__chests=[]
        count=0
        while count<3:
            chest=[random.randint(0,59),random.randint(0,14)]
            # make sure there is no treasure in the same coordinate
            if chest not in self.__chests:
                self.__chests.append(chest)
                count+=1
                # using  for test the class and programm
                # self.__board[chest[1]][chest[0]]="."
                
# returns the list of coordinates of the chests still to be found
    def getChests(self):
        return self.__chests
# retyrns the number of treasure chests still to be found
    def getTreasuresLeft(self):
        return len(self.__chests)
# change the matrix__board, x should be between 0 and 59, y between 0 and 14
    def dropSonar(self,x,y,sonar):
        if(0<=x<=59):
            self.__x=x
        if(0<=y<=14):
            self.__y=y
        # change the sonar to the user enter coordinate
        self.__board[int(self.__y)][int(self.__x)]=sonar
# check the distance from the three treasure    
    def checkDistance(self,x,y):
        if(type(x)==int)and(type(y)==int):
            self.__x=x
            self.__y=y
        # set closest to a very bigger numbe
        closest=100
        # check the distance
        for i in range (0,len(self.__chests)):
            # return 0 if the coordinates correspond to the exact position of a treasure chest
            if [self.__x, self.__y]==self.__chests[i]:
                self.__chests.remove(self.__chests[i])
                return 0
           
            # return a positive distance if the closest hiddenh chest is on the x axis and a negative distance if the closest hidden chest is on the y axis and still in the range
        for i in range (0,len(self.__chests)):
            # find the c value for each of the treasure
            xValue=abs(self.__chests[i][0]-self.__x)
            yValue=abs(self.__chests[i][1]-self.__y)
            c_value=(xValue**2 + yValue**2)
            c_value=c_value**(0.5)
            if c_value<closest:
                closest=c_value
                position=i
        xValue=abs(self.__chests[position][0]-self.__x)
        yValue=abs(self.__chests[position][1]-self.__y)  
        if (xValue <10) and (yValue<6):
            if (xValue==0):
                return (-1)*yValue
            elif (yValue==0):
                return xValue
            elif (xValue < (2*yValue)):
                return xValue
            else:
                return (-1)*yValue
    # if distance out of range, return "O"
        else:
            return "O"

# draw the ocean with the sonar devices
    def drawBoard(self):
        print("    "+" "*9+"1"+" "*9+"2"+" "*9+"3"+" "*9+"4"+" "*9+"5")
        print("   "+"0123456789"*6) 
        count=0
        for i in range (0, len(self.__board)):
            if count<10:
                print(" "+str(count)+" "+"".join(self.__board[i])+" "+str(count))
            else:
                print(str(count)+" "+"".join(self.__board[i])+" "+str(count))
            count+=1
        print("    "+" "*9+"1"+" "*9+"2"+" "*9+"3"+" "*9+"4"+" "*9+"5")
        print("   "+"0123456789"*6) 

# check if sonarPosition is an interger
def is_Value(sonarPosition):
    try:
        sonarPosition=sonarPosition.split()
        int(sonarPosition[0])
        int(sonarPosition[1])
    except Exception:
        return False
    else:
        return True
# check if sonarPosition is valued
def isValue(sonarPosition):
        if (int(sonarPosition[0]) < 0) or (int(sonarPosition[0])>59) or (int(sonarPosition[1])>14) or (int(sonarPosition[1])<0):
            return False
        else:
            return True
#-------------------------------------------------------------------------------------------------------------    
#start the program
a=OceanTreasure()
numberSonar=20
sonarPositions=[]
a.drawBoard()
print("You have 20 devices available. Treasure found: 0. Still to be found: 3.\n")
print("Where do you want to drop your sonar?")
sonarPosition=input("Enter coordinates x y (x in [0..59] and y in [0..14]) or (Q to quit and H for help): ")

while (is_Value(sonarPosition)!=True):
    if (sonarPosition in ['Q','H','q','h']):
        break
    else:
        print("Where do you want to drop your sonar?")
        sonarPosition=input("Enter coordinates x y (x in [0..59] and y in [0..14]) or (Q to quit and H for help): ")

while (a.getTreasuresLeft()!=0) or (numberSonar!=0):
# if quit the game, print thanks and chests
    if sonarPosition in ["Q","q"]:
        print("The chests were in:", a.getChests())
        print("Thank you for playing Ocean Treasures")
        break
    else: 
    # if ask how to play, say the rules but not quit the game
        if sonarPosition in ['h','H']:
            print('You have a total of 20 sonar devices and there are 3 treasure chests to find, randomly scattered in the ocean. The game ends when you do not have sonar devices left or you found all three chests.\nTo find a chest you need to drop a sonar device at the exact x,y coordinates of the chest. In that case the sonar would indicate "X".\nThe sonar devices are twice as sensitive on the column axis than the rows. It can detect a chest 9 units away on both sides of the x axis and 5 units away on the y axis.\nIf the sonar is dropped too far (more than 9 units away on the x axis and 6 on the y axis) from a chest, the sonar would indicate "O",\n meaning nothing detected. Again, the maximum range of the sonar device is 9 units on the x axis and 5 units on the y axis.\nIf the sonar is less than 10 units away from a chest on the x axis, the sonar would indicate the distance (1, 2, ..., 9).\nOn the y axis, if the sonar device is closer than 6 units, closer on the y than the x axis and still in the range\nthe sonar would indicate a for 1, b for 2, c for 3, d for 4 and e for 5 distance units.\n ')     
        # print numbers
        else:
            sonarPosition=sonarPosition.split()
            sonarPosition=[int(sonarPosition[0]),int(sonarPosition[1])]
            # check if numbers are valued
            if isValue(sonarPosition):
                numberSonar-=1
            # check if drop sonar in the same position
                if sonarPosition in sonarPositions:
                    print("You already dropped a sonar there. You lost another sonar device")
            # start to find the treasure        
                else:
                    sonarPositions.append(sonarPosition)
                    distance=a.checkDistance(sonarPosition[0],sonarPosition[1])
                    if distance == 0:
                        a.dropSonar(sonarPosition[0],sonarPosition[1],"X")
                    elif distance=="O":
                        a.dropSonar(sonarPosition[0],sonarPosition[1],"O")                        
                    elif distance < 0:
                        distance=(-1)*distance
                        if distance ==1:
                            a.dropSonar(sonarPosition[0],sonarPosition[1],"a")
                        elif distance == 2:
                            a.dropSonar(sonarPosition[0],sonarPosition[1],"b")
                        elif distance == 3:
                            a.dropSonar(sonarPosition[0],sonarPosition[1],"c")
                        elif distance == 4:
                            a.dropSonar(sonarPosition[0],sonarPosition[1],"d")
                        elif distance == 5:
                            a.dropSonar(sonarPosition[0],sonarPosition[1],"e")
                    else:
                        if (distance >9):
                            a.dropSonar(sonarPosition[0],sonarPosition[1],"O")
                        else:
                            a.dropSonar(sonarPosition[0],sonarPosition[1],str(distance))
                    a.drawBoard()
                    print("You have", numberSonar, "devices avaiable. Treasure found:", a.getTreasuresLeft(), "Still to be found:", (3-(a.getTreasuresLeft())))
    # update sonar position
    if (a.getTreasuresLeft()==0) or (numberSonar==0):
        break
    else:
        print("Where do you want to drop your sonar?")
        sonarPosition=input("Enter coordinates x y (x in [0..59] and y in [0..14]) or (Q to quit and H for help): ")    
if a.getTreasuresLeft()==0:
    print("Well done! You found all the 3 treasure Chests using", numberSonar, "out of 20 sonar devices.")
if numberSonar==0:
    print("You lost all your 20 sonar devises.")
    print("The remaining chests were in:", a.getChests())
