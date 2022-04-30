# # Data Types -Strings, Integer,Floats, Boolean
# b1 = True
# b2 = False
# # print(type(b1))

# knows_password = True
# knows_username = True
# login = knows_password and knows_username
# # print(type(login))
# #


# # Boolean Operators  - NOT, AND, OR
# recover = knows_password or knows_username

# # is_raining = True
# # is_cold = True
# # print(is_raining)
# # print(not is_raining)
# # print(is_raining or is_cold)
# # print(is_raining and not is_cold)
# # print(is_raining or not is_cold)
# # print(not is_raining and not is_cold)
# # print(not(is_raining and is_cold))


# # Comparison Operators
# # ==Equal
# # != Not Equal
# # > Greater than
# # < Less than
# # >= Greater than or equal
# # <= Less than or equal
# # print(10 > 5)
# # print(1 > 1.5)
# # print(5.9 != 5.8)
# # print("Sarah" == "Georg")

# # temperature = 16
# # print(temperature < 18)
# # wind_chill = 3
# # print(wind_chill=3)
# # print(wind_chill > 4)
# # print(temperature - wind_chill < 16)
# # name = "Hayley"
# # print("Hayley" == name)

# # name = "Camila"

# # if name == "Sarah":
# #     print("Hello again")
# # elif name == "Camila":
# #     print(f"Hello {name}, what are you doing today?")
# # else:
# #     print("WOW HELLO")

# is_raining = False
# temperature = 16
# wind_chill = 3
# if temperature - wind_chill < 16 and is_raining:
#     print("Just stay home.")
# else:
#     if is_raining:
#         print("You'll need an umbrella.")
#     if temperature - wind_chill < 16:
#         print("You'll need a jumper today")
# # if is_raining:
# #     print("Take an umbrella!")
# # else:
# #     print("Do not take an umbrella")

# # if temperature - wind_chill < 16:
# #     print("Take a jumper")
# # elif temperature - wind_chill > 30:
# #     print("Euck, it's hot today, stay home")
# # else:
# #     print("Wow, what a lovely day!")


# Q1 & Q2
# moths_in_house = True
# mitch_is_home = True
# if moths_in_house:
#     print("Hoooman! Help me get the moths!")
# elif mitch_is_home and moths_in_house:
#     print("Meooooooooooooow! Hissssss!")
# elif mitch_is_home and not moths_in_house:
#     print("Climb on Mitch.")
# else:
#     print("No threats detected.")

# Q3

# # light_colour = "Red"
# # light_colour = "Green"
# light_colour = "Amber"
# car_detected = False

# if light_colour and not car_detected:
#     print("Do nothing.")
# elif light_colour and not car_detected:
#     print("Do nothing.")

# else:
#     print("Flash!")


# Q4
# name = input("Sarah")
Ellen = 120
Dan = 50
Tom = 191

Rider = int(input("Enter your name: "))
height = int(input("Enter your height: "))
if Ellen and Dan and Tom > 120:
    print("Hop on!")
else:
    print("Sorry, not today :(")
