#Liam Collins
#probmap

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
orange = Color(0xFFA500,1)

blackOutline = LineStyle(2,black)
noOutline = LineStyle(0,black)

field = RectangleAsset(700,450,blackOutline,green) #width, height, outline, fill
box = RectangleAsset(400,200,blackOutline,green) #width, height, outline, fill
location_13 = RectangleAsset(225,75,noOutline,orange)
#blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill
#greenEllipse = EllipseAsset(100,50,blackOutline,green) #width, height, outline, fill
#blackLine = LineAsset(50,160,blackOutline) #x_endpoint, y_endpoint, lineStyle
#redTriangle = PolygonAsset([(75,75), (100,100), (50,100)],blackOutline,red) #endpoint, outline, fill
#text = TextAsset('Literature',fill=green, style='bold 40pt Times') #text, other options

Sprite(field)
Sprite(box, (150,250))
Sprite(location_13, (237.5,375))
#Sprite(blueCircle,(50,50))
#Sprite(greenEllipse,(200,50))
#Sprite(blackLine)
#Sprite(redTriangle, (175,200))
#Sprite(text, (200,400))

App().run()
