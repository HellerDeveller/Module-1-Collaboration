class Vehicle():
    def type(self):
        print(f"Vehicle type: {vehicle}")

class Automobile(Vehicle):
    def year(self):
        print(f"Year: {year}")

    def make(self):
        print(f"Make: {make}")

    def model(self):
        print(f"Model: {model}")

    def doors(self):
        print(f"Number of Doors: {doors}")

    def roof(self):
        print(f"Type of Roof: {roof}")

vehicle = input("Enter the type of vehicle: ")
year = input("Enter the year it was made in: ")
make = input("Enter the maker/manufacturer: ")
model = input("Enter the model: ")
while True: 
    doors = input("Enter the number of doors: ")
    while True:
        try:
            doors = int(doors)
            break
        except:
            doors = input("That is not a number, try again: ")
    if doors < 2 or doors > 4:
        print("There can only be 2-4 doors, try again.")
    else:
        break
while True:
    roof = input("Enter the type of roof (solid/sun roof): ")
    check = roof.lower()
    if check == "solid" or check == "sun roof":
        break
    else:
        print("The roofs are either solid or sun roof, try again.")

Vehicle().type()
Automobile().year()
Automobile().make()
Automobile().model()
Automobile().doors()
Automobile().roof()