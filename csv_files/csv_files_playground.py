import os
import csv
# import os
# cwd = os.getcwd()
# print("This is mt directory" + cwd)
# with open("csv_files/2016_pilbara.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line)

# population = []

# with open("csv_files/2016_pilbara.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         population.append(line)

# print(population)
# print()

# for age_group in population:
#     print(f"{age_group[0]} {age_group[1]}")

# # writing to csv file
# with open("population.csv", mode="w", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")

#     for age_group in population:
#         csv_writer.writerow([age_group[1], age_group[0]])

# Q1
# import os
# cwd = os.getcwd()
# print("This is my directory" + cwd)

# with open("csv_files/colours_20_simple.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line[0], line[1], line[2])


# Q2
# import os
# cwd = os.getcwd()
# print("This is my directory" + cwd)

# with open("csv_files/colours_20_simple.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line[2], "HEX:", line[1], "RGB: ", line[0])

# Q4
# import os
# cwd = os.getcwd()
# print("This is my directory" + cwd)

# num_yellow = 0
# num_red = 0
# num_green = 0
# num_blue = 0
# with open("csv_files/colours_20_simple.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         if "yellow" in line[2]:
#             num_yellow += 1
#         if "red" in line[2]:
#             num_red += 1
#         if "green" in line[2]:
#             num_green += 1
#         if "blue" in line[2]:
#             num_blue += 1

# print("yellow: ", num_yellow)
# print("red: ", num_red)
# print("green: ", num_green)
# print("blue: ", num_blue)


# num_yellow = 0
# num_red = 0
# num_green = 0
# num_blue = 0
# cwd = os.getcwd()
# print("This is my directory" + cwd)
# with open("csv_files/colours_213.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         if "yellow" in line[4]:
#             num_yellow += 1
#         if "red" in line[4]:
#             num_red += 1
#         if "green" in line[4]:
#             num_green += 1
#         if "blue" in line[4]:
#             num_blue += 1

# print("yellow: ", num_yellow)
# print("red: ", num_red)
# print("green: ", num_green)
# print("blue: ", num_blue)

# Q5

import os
cwd = os.getcwd()

velocity_list = []
galaxy_list = []

with open("csv_files/galaxies.csv", encoding="utf-8") as csv_file:

    reader = csv.reader(csv_file)
    next(reader, None)
    for line in reader:
        velocity_list.append(int(line[1]))
        galaxy_list.append(line[0])
print("Galaxy", galaxy_list[velocity_list.index(max(velocity_list))], "has the min velocity of", max(
    velocity_list), "km/sec")
print("Galaxy", galaxy_list[velocity_list.index(min(velocity_list))], "has the max velocity of", min(
    velocity_list), "km/sec")
