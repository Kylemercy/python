
print("________________________________")
print("________________________________")
print("Temperature conversion system")
print("________________________________")
print("________________________________")
print("selections: \n press 1 To enter Celsius \n press2 To enter Fahrenheit \n press 3 To enter Kelvin ")
select = int(input("Enter your selection: "))
if select  > 3:
  print("invalid input")
if select == 1:
  temp = float(input("Enter your temperature in Celsius: "))
  fahrenheit = round((((9/5)*temp)+32),2)
  Kelvin = round((temp + 273.15),2)
  print("\n")
  print("Temperature in Fahrenheit is:", fahrenheit,"fahrenheit,deg")
  print("Temperature in Kelvin is :", Kelvin,"Kelvin,deg")

elif select  == 2:
  temp = float(input("Enter your selection in Fahrenheit: "))
  celsius = round(((5/9)*(temp -32)),2)
  Kelvin = round(((temp-459.67)*(5/9)),2)
  print("\n")
  print("Temperature in Celsius is : ", celsius,"Celsius,deg")
  print("Temperature in Kelvin is :", Kelvin,"Kelvin,deg")
 

elif select == 3:
  temp = float(input("Enter temperature in Kelvin: "))
  fahrenheit = round(((temp*(9/5))-459.67),2)
  celsius = round((temp-273.15), 2)
  print('Temperature in Farenheit: ', fahrenheit, 'deg F')
  print('Temperature in Celcius: ', celsius, 'deg C')
