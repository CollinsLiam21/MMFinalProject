#Liam Collins
#probmap

from ggame import *

shotPlaceProbList = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,44,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

def mouseClick(event): 
    A = event.x
    B = event.y
    #Location 5
    if event.x < 150 and 300 < event.y < 500:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '0%'
        data['whichLocation'] = 5
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 4
    elif 550 < event.x < 700 and 300 < event.y < 500:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '0%'
        data['whichLocation'] = 4
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 11
    elif 150 < event.x < 237.5 and 300 < event.y < 425:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '7%'
        data['whichLocation'] = 11
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 9
    elif 462.5 < event.x < 550 and 300 < event.y < 425:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '6%'
        data['whichLocation'] = 9
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 3
    elif 237.5 < event.x < 462.5 and 300 < event.y < 425:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '15%'
        data['whichLocation'] = 3
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 12
    elif 150 < event.x < 237.5 and 425 < event.y < 500:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '20%'
        data['whichLocation'] = 12
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 10
    elif 462.5 < event.x < 550 and 425 < event.y < 500:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '20%'
        data['whichLocation'] = 10
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 7
    elif event.x < 250 and 225 < event.y < 300:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '8%'
        data['whichLocation'] = 7
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 8
    elif 450 < event.x < 700 and 225 < event.y < 300:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '8%'
        data['whichLocation'] = 8
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 15
    elif 250 < event.x < 450 and 225 < event.y < 300:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '3%'
        data['whichLocation'] = 15
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 6left
    elif event.x < 250 and 150 < event.y < 225:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '3%'
        data['whichLocation'] = 6
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 6right 
    elif 450 < event.x < 700 and 150 < event.y < 225:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '3%'
        data['whichLocation'] = 6
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 16
    elif 250 < event.x < 450 and 150 < event.y < 225:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '2%'
        data['whichLocation'] = 16
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 17
    elif event.x < 700 and 75 < event.y < 150:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '1%'
        data['whichLocation'] = 17
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 18
    elif event.x < 700 and event.y < 75:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '2%'
        data['whichLocation'] = 18
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 13
    elif 237.5 < event.x < 462.5 and 425 < event.y < 500:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '50%'
        data['whichLocation'] = 13
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #shot place 12
    elif 710 < event.x < 785 and 25 < event.y < 91.67:
        Sprite(SoccerBall, (A-10,B-10))
        Sprite(TextAsset(shotPlaceProbList[4][data['whichLocation']-1],fill=black, style='bold 15pt Times'), (900,425))
    #shot place 11
    elif 785 < event.x < 935 and 25 < event.y < 91.67:
        Sprite(SoccerBall, (A-10,B-10))
        Sprite(TextAsset(shotPlaceProbList[3][data['whichLocation']-1],fill=black, style='bold 15pt Times'), (900,425))
    #shot place 13
    elif 935 < event.x < 1010 and 25 < event.y < 91.67:
        Sprite(SoccerBall, (A-10,B-10))
        Sprite(TextAsset(shotPlaceProbList[5][data['whichLocation']-1],fill=black, style='bold 15pt Times'), (900,425))

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
orange = Color(0xFFA500,1)
white = Color(0xFFFFFF,1)

blackOutline = LineStyle(2,black)
noOutline = LineStyle(0,black)

field = RectangleAsset(700,500,blackOutline,green) #width, height, outline, fill
YardBox = RectangleAsset(400,200,blackOutline,green) #width, height, outline, fill
ChooseLocation = TextAsset('Choose_Location',fill=black, style='bold 15pt Times') #text, other options
location_13 = RectangleAsset(225,75,blackOutline,green)
SoccerBall = CircleAsset(10,blackOutline,black)
goalProb = TextAsset('Goal_Probability',fill=black, style='bold 15pt Times') #text, other options

goal = RectangleAsset(300,200,blackOutline,orange)
ChooseShotPlace = TextAsset('Choose_Shot_Place',fill=black, style='bold 15pt Times') #text, other options
#blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill
#greenEllipse = EllipseAsset(100,50,blackOutline,green) #width, height, outline, fill
#blackLine = LineAsset(50,160,blackOutline) #x_endpoint, y_endpoint, lineStyle
#redTriangle = PolygonAsset([(75,75), (100,100), (50,100)],blackOutline,red) #endpoint, outline, fill

Sprite(field)
Sprite(YardBox, (150,300))
Sprite(location_13, (237.5,425))
Sprite(goal, (710,25))
Sprite(ChooseShotPlace, (750,0))
Sprite(ChooseLocation, (5,5))
#Sprite(HalfCircleBox, (50,50))
#Sprite(blueCircle,(50,50))
#Sprite(greenEllipse,(200,50))
#Sprite(blackLine)
#Sprite(redTriangle, (175,200))
Sprite(goalProb, (705,400))

#Dictionary
data = {}
data['goalProb'] = 0
data['shotPlaceProb'] = 0
data['whichLocation'] = 0

App().listenMouseEvent('click',mouseClick)
App().run()
