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
    
#def returnColor(line):