# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# for digit in range(6):  # 0,1,2,3,4,5
#     # digit = 0, #digit = 1
#     print(digit)

# numbers = [10, 20, 30, 40]
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# for number in numbers:
#     print(numbers)

# for num in range(10):
#     print(num)
# for num in range(1, 11):
#     print(num)
# for num in range(0, 11, 2):
#     print(num)
#     for num in range(0, 11, 2):
#     print(num)

# numbers = [1, 100]
# for num in range():
#     print(0, 100, 5)


# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]
# different options, same result
# for item in range(len(chilli_wishlist)):
#     print(chilli_wishlist[item])
# for item in chilli_wishlist:
#     print(item)

# nested loops
# chilli_wishlist = [
#     ["igloo"],
#     ["donut toy", "tennis ball", "crocodile toy"],
#     ["chicken", "peanut butter"],
#     ["cardboard box", "kong", "dig mat"]
# ]
# for catergory in chilli_wishlist:
#     for item in catergory:
#         print(item)

# While Loop
# num = 1
# while num > 0:
#     print("Hi")
#     num = 0

# guess = ""
# while guess != "a":
#     print(guess)

# counter = 10
# while counter <= 10:
#     print(counter)
#     counter = counter + 1

# Exercises for Loops
# Q1
# number = input("Please enter a number: ")
# count = 1
# for num in range(0, int(number)):
#     y = int(number) * count
#     print(number, " * ", count, " = ", y)
#     count += 1

# number = int(input("Enter a number"))
# for i in range(1, number+1):
#     print(f"{number} * {i} = {number * i}")
# - more flexible way

# Q2
# number = input("Please enter a number: ")
# number = int(number)
# sum = 0
# for num in range(0, number+1, 1):
#     sum = sum+num
# print("SUM of first ", number, "numbers is: ", sum)

# Q3
# random_numbers = [3, 5, 9, 1]
# print("The sum of my_list is", sum(random_numbers))

# random_numbers = [-3, -5, 9, 1]
# print("The sum of my_list is", sum(random_numbers))

# random_numbers = []
# print("The sum of my_list is", sum(random_numbers))

# total = 0
# random_numbers = [3, 5, 9, 1]
# for num in random_numbers:
#     total += num
#     print(total)


# Q4
# mailing_list = [
#     ["Chilli", "chilli@thechihuahua.com"],
#     ["Roary", "roary@moth.catchers"],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Ivy", "noreply@goldendreamers.xyz"],
# ]
# for entry in mailing_list:
#     print(entry[0] + ": " + entry[1])


# While Loop: Excersises
# Q1
# input_number = input("Enter a number: ")
# completed_list = []
# print(input_number)
# print(completed_list)
# while input_number != "":
#     completed_list.append(int(input_number))
#     input_number = input("Enter a number: ")
# print(completed_list)
# print(sum(completed_list))

# Q2

# maximum = int(input(" Please Enter any Maximum Value : "))
# for number in range(1, maximum + 1):
#     if(number % 2 != 0):
#         print("{0}".format(number))

#  Q3
# i = 20
# num = int(input("enter a number:"))
# while num != i:
#     # num=int(input("enter a number: "))

#     if num < i:
#         print("Too low!")
#         # num=int(input("enter a number: "))
#     elif num > i:
#         print("Too high!")
#     num = int(input("enter a number: "))
# print("correct!")

# Loops: Exercises (Extension)

# Extra
# name = "Sarah"
# while True:
#     print(f"Hi, {name}")
#     name = input("Enter a name:")

# counter = 0
# while counter < 5:
#     print("Hello")
#     print(f"counter1: ", {counter})
# counter = counter + 1
# print("counter 2: ", counter)

# total = 0
# random_numbers = [3, 5, 6, 6]
# counter = 0
# while counter < len(random_numbers):
#     print(counter)
#     print(random_numbers[counter])
#     # total += random_numbers[counter]
#     counter += 1

# Q1
# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
# ]

# price_list = []
# for item in groceries:
#     input_item = input(item[0] + " quantity: ")
#     price = int(input_item) * item[1]
#     price_list.append([item[0], price])
# print(price_list)

# print("====Izzy's Food Emporium====")
# total = 0
# for item in price_list:
#     print(item[0], " ", "$"+str('%.2f' % item[1]))
#     total += item[1]
# print("============================")
# print("$"+str(total))
