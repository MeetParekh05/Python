import datetime
name = input("Hello! Please enter your name: ")
print("Hello " + name)
age = int(input("Enter your age: "))
year_now = datetime.datetime.now()
# print(year_now.year)
print("You will turn 100 in " , (100-age) + (year_now.year))