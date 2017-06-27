name = input("What is your name? ")
print ("Hi", name)

number = int(input("I can say hello up to 50 times! How many times should I say hello? "))

if number <= 50:
    for hello in range(number):
        print(name)
else:
    print ("I said less than 50!")
        

moon = input("Do you want to come to the moon with me? ")

if moon == "yes":
    print ("Great, lets go!")
elif moon == "no":
    print ("That's a shame, maybe next time!")
else:
    print ("You have to answer yes or no!")

