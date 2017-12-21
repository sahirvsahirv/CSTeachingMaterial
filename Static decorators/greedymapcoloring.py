import json
import codecs
from topojson import geometry

import requests
#import urllib



#p = geometry({'type': "LineString", 'arcs': [0]}, topology1['arcs'])
#pprint.pprint(p)
#input_file = open(r'C:\Users\Gowri\Desktop\CS_classes\MaterialRepo\CSTeachingMaterial\Map Colouring\data\world-50m.json', "r")
#dataform = str(input_file).strip("'<>() ").replace('\'', '\"')
#data = json.loads(dataform)
#with open('C:\Users\Gowri\Desktop\CS_classes\MaterialRepo\CSTeachingMaterial\Map Colouring\data\world-50m.json') as json_file:
    #data = json.loads(json_file)


#works
#data = requests.get("https://raw.githubusercontent.com/d3/d3-geo/master/test/data/world-50m.json").json()

##for country in data:
##        print( country)

#transform
#arcs
#objects
#type

##for country in data['objects']:
##        print( country)

##objects
##arcs
##transform
##countries
##land

##for country in data['objects']['countries']:
##        print( country)
##transform
##objects
##arcs
##type
##land
##countries
##bbox
##type
##geometries

#works
##for country in data['objects']['countries']['geometries']:
##        print( country['type'])
##        print( country['id'])
        
##bbox
##geometries
##type
      
colors = ['Red', 'Blue', 'Green', 'Yellow']

states = ['Andhra', 'Karnataka', 'TamilNadu', 'Kerala']

neighbors = {}
neighbors['Andhra'] = ['Karnataka', 'TamilNadu']
neighbors['Karnataka'] = ['Andhra', 'TamilNadu', 'Kerala']
neighbors['TamilNadu'] = ['Andhra', 'Karnataka', 'Kerala']
neighbors['Kerala'] = ['Karnataka', 'TamilNadu']

colors_of_states = {}
colors_of_states['Andhra'] = None
colors_of_states['Karnataka'] = None
colors_of_states['TamilNadu'] = None
colors_of_states['Kerala'] = None

alreadycoloredlistofneighbours = {}
alreadycoloredlistofneighbours['Andhra'] = None
alreadycoloredlistofneighbours['Karnataka'] = None
alreadycoloredlistofneighbours['TamilNadu'] = None
alreadycoloredlistofneighbours['Kerala'] = None

def nonecolored(state):
    nc = True
    for neighbour in neighbors[state]:
        if(colors_of_states[neighbour] == None):
            continue
        else:
            nc = False
    return nc

def checkneighborcolor(state, color):
    for neighbor in neighbors[state]:
        #check each neighbor and if any neighbor has the same color that you
        #are trying to color with return false
        if(color == colors_of_states[neighbor]):
            return False
    #none of the neighbors have the color - finish the for loop
    return True
        
def getcolorforstate(state):
    for color in colors:
        #check the color of the neighbors
        cancolor = checkneighborcolor(state, color)
        if(cancolor == True):
            return color
def main():
    for state in colors_of_states.keys():
        #check if none of the neighbours are colored
        nc = nonecolored(state)
        #if nonecoloured is False here then some neighbour has been coloured
        #allocating Red to it
        if(nc == True):
            #allocating default color here
            colors_of_states[state] = colors[0]
        else:
            #checking which color to get
            color = getcolorforstate(state)
            colors_of_states[state] = color

    print(colors_of_states)
main()
