name = input("What is your name? ")
print ("Hi", name)


while True:
    number = int(input("I can say hello up to 50 times! How many times should I say hello? "))
    if number > 50:
        print("I said less than 50!")
        continue
    else:
        break

for hello in range(number):
        print(name)

while True:        
    moon = input("Do you want to come to the moon with me? ")
    print (moon)
    if moon not in ["yes", "no"]:
        print ("You must say yes or no!")
        continue
    else:
        break
                 
if moon == "yes":
    print ("Great, lets go!")
elif moon == "no":
    print ("That's a shame, maybe next time!")                 

age = int(input("What year were you born? "))
age = 2017 - age
print("You are", age, "Years old")


