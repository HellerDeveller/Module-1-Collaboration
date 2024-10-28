# Program by Marcin Brodowicz
# This program continuously asks for name and gpa and outputs a qualification
# if gpa is high enough until 'ZZZ' is entered


lname = input("Enter your last name or 'ZZZ' to quit: ")

while lname != 'ZZZ':
    fname = input("Enter your first name: ")
    while True:
        try:
            gpa = float(input("What is your GPA? "))
            break
        except:
            print("That is not a valid GPA!")
    if gpa >= 3.5:
        print(f"Congratulations {fname}, you've made it on the Dean's List!!")
    elif gpa >= 3.25:
        print(f"Congratulations {fname}, you've made it on the Honor Roll!")
    print("Recorded.")
    lname = input("Enter your last name or 'ZZZ' to quit: ")
