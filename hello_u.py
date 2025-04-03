#Ask user for name

name = input("What is your name?: ")


#Ask user for age
age = input("What is your age?: ")


#Ask user for city

city = input("what city are you from?: ")


#Ask user what they enjoy

enjoy = input("What do you Enjoy?: ")



#Create output text

string = "Your name is {} and you are {} years old. You live in {} and you love{}"
output = string.format(name, age, city, enjoy )

#Print output to screen
print(output)
