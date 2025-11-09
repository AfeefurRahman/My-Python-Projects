import math 

# Code from Milestone #1 

def clampValueToRange(value,low,high):
    if value > low and value < high:  
        newValue = int(value)
        return newValue
    elif value < low:
        low_result = int(low)
        return low_result
    elif value > high:
        high_result = int(high)
        return high_result
    
def returnColor(line):
    result_list = []
    newList = line.split()
    for x in range(3):
        result_list.append(int(newList[x]))
    return result_list

def returnLocation(line):
    resultList = []
    newString = line.split()
    for x in range(len(newString)-1,len(newString)-3,-1):
        resultList.append(int(newString[x]))
        resultList.reverse()
    return resultList

def locationValid(x,width,y,height):
    if x >= 0 and y >= 0 and x < width and y < height:
        return True
    else:
        return False

# Milestone 2 Starts here 
# Problem 1 
def convertPixel(color):
    finalColor = {"r": 0, "g": 0, "b": 0}
    finalColor["r"] = clampValueToRange(color[0],0,255)
    finalColor["g"] = clampValueToRange(color[1],0,255)
    finalColor["b"] = clampValueToRange(color[2],0,255)
    return finalColor

# Problem 2 
def positionPixel(x,y,color):
    result = {"pixel":color,'x': x, 'y':y}
    return result 

# Problem 3 
def updateChangeList(pixel,pixelList):
    pixelList.append(pixel)
    return None

# Problem 4 
def readPixelFile(pixels,filename):
    with open(filename , 'r') as file:
        for line in file:
            clean_line = line.strip()
            if clean_line:
                color_list = returnColor(clean_line)
                location_list = returnLocation(clean_line)
                
                color_dict = convertPixel(color_list)

                x = location_list[0]
                y = location_list[1]

                new_pixel = positionPixel(x,y,color_dict)
                updateChangeList(new_pixel,pixels)

print(updateChangeList({'pixel': {'r': 0, 'g': 100, 'b': 255}, 'x': 2, 'y': 3}, []))