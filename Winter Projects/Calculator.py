import math 

response = float(input("Please input your number in the form of a decimal: "))
response2 = float(input("Please input your second number in the form of a decimal: "))
method = input("Please select the method you want to use to calculate (+ , - , / , // , % , *): ")
result = 0

if method == "+":
   result = response + response2
   print(round(result,3))
elif method == "-":
   result = response - response2
   print(round(result,3))
elif method == "/":
   result = response / response2 
   print(round(result,3))
elif method == "//":
   result = response // response2
   print(round(result,3))
elif method == "%":
   result = response % response2
   print(round(result,3))
elif method == "*":
   result = response * response2
   print(round(result,3))
else:
   print("You have either put a letter in response 1 and 2 or you have put a wrong method. So please try again.") 