# Cantor pairing
# https://en.wikipedia.org/wiki/Pairing_function#Cantor_pairing_function

import math
def getHash(x,y):
    return ((x+y+1)*(x+y)/2)+y
def getPair(hashedVal):
    z = hashedVal
    w = math.floor((math.sqrt(8*z + 1)-1)/2)
    t = ((w*w)+w)/2
    y = z - t
    x = w - y
    return x,y

print(getPair(getHash(5476856, 0)))
