# ----------------------------------RENT CALCULATOR----------------------------------------#



rent =int(input("enter your room/flat rent = "))
food =int(input("enter your food pay= "))
electricity_unit =int(input("enter your unit charge will you spend= "))
unit_charge =int(input("enter you charge per unit= "))
persons = int(input("enter the number of person live= "))

electricity_bill = electricity_unit * unit_charge
output = (rent + food + electricity_bill ) // persons
print("Each person's will be pay = ",output)
