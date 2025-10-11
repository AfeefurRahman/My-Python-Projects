import math

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
    newString = line.replace(" ","")
    for x in range(0,3):
        result_list.append(newString[x])
    return result_list

def returnLocation(line):
    resultList = []
    newString = line.replace(" ", "")
    for x in range(len(newString)-1,len(newString)-3,-1):
        resultList.append(newString[x])
        resultList.reverse()
    return resultList

def locationValid(x,width,y,height):
    if x >= 0 and y >= 0 and x < width and y < height:
        return True
    else:
        return False
