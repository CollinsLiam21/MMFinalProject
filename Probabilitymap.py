#Liam Collins
#probmap

from ggame import *

def mouseClick(event): 
    A = event.x
    B = event.y
    #Location 5
    if event.x < 150 and 300 < event.y < 500:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '0%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))
    #Location 4
    if 550 < event.x < 700 and 300 < event.y < 500:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '0%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))
    #Location 11
    if 150 < event.x < 237.5 and 300 < event.y < 425:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '7%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))
    #Location 9
    if 462.5 < event.x < 550 and 300 < event.y < 425:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '6%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))
    #Location 3
    if 237.5 < event.x < 462.5 and 300 < event.y < 425:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '15%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))
    #Location 12
    if 150 < event.x < 237.5 and 425 < event.y < 500:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '20%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))
    #Location 10
    if 462.5 < event.x < 550 and 425 < event.y < 500:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '20%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))
    #Location 7
    if event.x < 250 and 225 < event.y < 300:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '8%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))
    #Location 8
    if 450 < event.x < 700 and 225 < event.y < 300:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '8%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))
    #Location 15
    if 250 < event.x < 450 and 225 < event.y < 300:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '3%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))
    #Location 6left
    if event.x < 250 and 150 < event.y < 225:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '3%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))
    #Location 6right 
    if 450 < event.x < 700 and 150 < event.y < 225:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '3%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))
    #Location 16
    if 250 < event.x < 450 and 150 < event.y < 225:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '2%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))
    #Location 17
    if event.x < 700 and 75 < event.y < 150:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '1%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))
    #Location 18
    if event.x < 700 and event.y < 75:
        Sprite(SoccerBall, (A-10,B-10))
        data['goalProb'] = '2%'
        Sprite(TextAsset(data['goalProb'],fill=black, style='bold 20pt Times'), (900,400))

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
orange = Color(0xFFA500,1)

blackOutline = LineStyle(2,black)
noOutline = LineStyle(0,black)

field = RectangleAsset(700,500,blackOutline,green) #width, height, outline, fill
YardBox = RectangleAsset(400,200,blackOutline,green) #width, height, outline, fill
location_13 = RectangleAsset(225,75,blackOutline,green)
SoccerBall = CircleAsset(10,blackOutline,black)
goalProb = TextAsset('Goal Probability',fill=black, style='bold 20pt Times') #text, other options
#blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill
#greenEllipse = EllipseAsset(100,50,blackOutline,green) #width, height, outline, fill
#blackLine = LineAsset(50,160,blackOutline) #x_endpoint, y_endpoint, lineStyle
#redTriangle = PolygonAsset([(75,75), (100,100), (50,100)],blackOutline,red) #endpoint, outline, fill

Sprite(field)
Sprite(YardBox, (150,300))
Sprite(location_13, (237.5,425))
#Sprite(HalfCircleBox, (50,50))
#Sprite(blueCircle,(50,50))
#Sprite(greenEllipse,(200,50))
#Sprite(blackLine)
#Sprite(redTriangle, (175,200))
Sprite(goalProb, (705,400))

#Dictionary
data = {}
data['goalProb'] = 0

App().listenMouseEvent('click',mouseClick)
App().run()
