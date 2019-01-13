#Liam Collins
#probmap

from ggame import *

shotPlaceProbList = [[58,53,21,0,42,44],[7,10,5,0,6,9],[12,30,15,0,17,33],[30,8,20,0,33,14],[13,33,7,0,15,36],[48,64,37,0,39,71],[38,14,9,0,39,16],[80,46,34,0,81,52],[87,86,68,0,82,84],[15,15,2,0,16,17],[4,8,0.6,0,9,5],[1,9,5,0,7,7],[0,20,0,0,0,8]]
righty = [[65,56,25,0,58,52],[7,11,3,0,6,8],[13,38,11,'NA',42,31],[31,7,21,'NA',35,15],[13,33,7,0,25,44],[42,67,37,0,57,80],[39,13,9,0,51,19],[82,45,35,0,80,72],[85,85,67,0,91,92],[14,15,9,0,22,23],[6,4,1,0,11,7],[0,5,5,0,12,9],[0,25,0,0,0,11]]
lefty = [[57,59,24,0,54,64],[8,10,8,0,6,12],[11,26,18,'NA',16,33],[25,13,18,0,50,25],[11,33,5,0,16,46],[51,61,31,0,46,83],[32,14,8,0,45,0],[89,31,32,0,100,71],[90,88,71,0,90,89],[17,14,2,0,16,0],[0,15,0,0,17,0],[0,8,13,0,0,0],[0,0,0,'NA',0,'NA']]
header = [[48,45,11,0,30,34],['NA','NA',0,'NA','NA','NA'],[0,50,6,0,5,50],[27,7,0,0,14,0],[22,45,13,0,0,50],[50,63,34,0,34,72],[29,24,17,0,8,0],[75,49,33,0,79,35],[88,89,66,0,82,81],[14,8,0,0,0,0],['NA','NA','NA','NA','NA','NA'],['NA',0,'NA','NA','NA','NA'],['NA','NA','NA','NA','NA','NA']]

def mouseClick(event): 
    A = event.x
    B = event.y
    '''#Location 5
    if event.x < 150 and 300 < event.y < 500:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '0%'
        data['whichLocation'] = 2
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 4
    elif 550 < event.x < 700 and 300 < event.y < 500:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '0%'
        data['whichLocation'] = 1
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))'''
    #Location 11
    if 150 < event.x < 237.5 and 300 < event.y < 425:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '7%'
        data['whichLocation'] = 8
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 9
    elif 462.5 < event.x < 550 and 300 < event.y < 425:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '6%'
        data['whichLocation'] = 6
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 3
    elif 237.5 < event.x < 462.5 and 300 < event.y < 425:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '15%'
        data['whichLocation'] = 2
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 12
    elif 150 < event.x < 237.5 and 425 < event.y < 500:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '20%'
        data['whichLocation'] = 9
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 10
    elif 462.5 < event.x < 550 and 425 < event.y < 500:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '20%'
        data['whichLocation'] = 7
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 7
    elif event.x < 250 and 225 < event.y < 300:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '8%'
        data['whichLocation'] = 4
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 8
    elif 450 < event.x < 700 and 225 < event.y < 300:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '8%'
        data['whichLocation'] = 5
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 15
    elif 250 < event.x < 450 and 225 < event.y < 300:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '3%'
        data['whichLocation'] = 11
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 6left
    elif event.x < 250 and 150 < event.y < 225:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '3%'
        data['whichLocation'] = 3
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 6right 
    elif 450 < event.x < 700 and 150 < event.y < 225:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '3%'
        data['whichLocation'] = 3
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 16
    elif 250 < event.x < 450 and 150 < event.y < 225:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '2%'
        data['whichLocation'] = 12
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 17
    elif event.x < 700 and 75 < event.y < 150:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '1%'
        data['whichLocation'] = 13
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 18
    elif event.x < 700 and event.y < 75:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '2%'
        data['whichLocation'] = 14
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #Location 13
    elif 237.5 < event.x < 462.5 and 425 < event.y < 500:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '50%'
        data['whichLocation'] = 10
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 15pt Times'), (900,400))
    #shot place 12
    if 710 < event.x < 785 and 25 < event.y < 91.67:
        data['shotPlace'] = 4
        Sprite(SoccerBall, (A-10,B-10))
        Sprite(TextAsset(shotPlaceProbList[data['whichLocation']-2][data['shotPlace']],fill=black, style='bold 15pt Times'), (900,425))
        bodyPart()
    #shot place 11
    elif 785 < event.x < 935 and 25 < event.y < 91.67:
        data['shotPlace'] = 3
        Sprite(SoccerBall, (A-10,B-10))
        Sprite(TextAsset(shotPlaceProbList[data['whichLocation']-2][data['shotPlace']],fill=black, style='bold 15pt Times'), (900,425))
        bodyPart()
    #shot place 13
    elif 935 < event.x < 1010 and 25 < event.y < 91.67:
        data['shotPlace'] = 5
        Sprite(SoccerBall, (A-10,B-10))
        Sprite(TextAsset(shotPlaceProbList[data['whichLocation']-2][data['shotPlace']],fill=black, style='bold 15pt Times'), (900,425))
        bodyPart()
    #shot place 5
    elif 710 < event.x < 1010 and 91.67 < event.y < 158.34:
        data['shotPlace'] = 2
        Sprite(SoccerBall, (A-10,B-10))
        Sprite(TextAsset(shotPlaceProbList[data['whichLocation']-2][data['shotPlace']],fill=black, style='bold 15pt Times'), (900,425))
        bodyPart()
    #shot place 3
    elif 710 < event.x < 860 and 158.34 < event.y < 225:
        data['shotPlace'] = 0
        Sprite(SoccerBall, (A-10,B-10))
        Sprite(TextAsset(shotPlaceProbList[data['whichLocation']-2][data['shotPlace']],fill=black, style='bold 15pt Times'), (900,425))
        bodyPart()
    #shot place 4
    elif 860 < event.x < 1010 and 158.34 < event.y < 225:
        data['shotPlace'] = 1
        Sprite(SoccerBall, (A-10,B-10))
        Sprite(TextAsset(shotPlaceProbList[data['whichLocation']-2][data['shotPlace']],fill=black, style='bold 15pt Times'), (900,425))
        bodyPart()
    
def bodyPart():
    bodyPart = int(input('Righty (1), Lefty (2), or Header (3)? '))
    if bodyPart == 1:
        Sprite(TextAsset(righty[data['whichLocation']-2][data['shotPlace']],fill=black, style='bold 15pt Times'), (900,450))
    elif bodyPart == 2:
        Sprite(TextAsset(lefty[data['whichLocation']-2][data['shotPlace']],fill=black, style='bold 15pt Times'), (900,450))
    elif bodyPart == 3:
        Sprite(TextAsset(header[data['whichLocation']-2][data['shotPlace']],fill=black, style='bold 15pt Times'), (900,450))
        

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
goalProbWithShotPlace = TextAsset('With_Shot_Place',fill=black, style='bold 15pt Times')
goalProbWithBodypart = TextAsset('With_Body_Part',fill=black, style='bold 15pt Times')

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
Sprite(goalProb, (705,400))
Sprite(goalProbWithShotPlace, (705,425))
Sprite(goalProbWithBodypart, (705,450))

#Dictionary
data = {}
data['goalProb'] = 0
data['shotPlaceProb'] = 0
data['whichLocation'] = 0
data['shotPlace'] = 0

App().listenMouseEvent('click',mouseClick)
App().run()
