import json
import turtle
import urllib.request
import time
 #you can also just do  import json, turtle, urllib.request, time
    

#create variable for our json file

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)

result = json.loads(response.read())
print(result)

print('People in Space:', result['number'])

people = result['people']
print(people)

for x in people:
    print(x)

for x in people:
    print(x['name'], 'in', x['craft'])

    
#shows current location of ISS    
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
#print(result)

location = result ['iss_position']
lat = location['latitude']
lon = location['longitude']

print('Lattitude:', lat)
print('Longitude:', lon)

lat_new = float(lat)
lon_new = float(lon)

screen = turtle.Screen()

screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.register_shape('/Users/westerica/developer/python practice/iss/iss.gif')
screen.bgpic('/Users/westerica/developer/python practice/iss/map.gif')

iss = turtle.Turtle()
iss.shape('/Users/westerica/developer/python practice/iss/iss.gif')
iss.setheading(90)
iss.penup()

iss.goto(lat_new,lon_new)

#space Center, Houston

lat = float(29.5593)
lon = float(-95.0900) #in python y coordinate is reversed, up is down & down is up

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' +str(lat) +'&lon=' +str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print result

over = result['response'][1]['risetime']
location.write(time.ctime(over))
