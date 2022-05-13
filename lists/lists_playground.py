# Lists
# 0 elements
# 0 index, 0,1,2

# characters = ["a", "b", "c"]
# print(characters)
# if "d" in characters:
#     print("Good")
# else:
#     characters.append("d")
#     print(characters)

# print(characters.remove("a"))
# print(characters)

# print(characters)
# print(type(characters))
# print(characters[0])
# characters.append("d")
# characters.extend(["e", "f"])
# characters.insert(1, "g")
# print(characters[-2])
# print(characters[0:2])  # starting index included, stopping index
# print(characters[1:3])

# asli = [[3, 5]], ["blue", "pink"]]
# print(asli[0])

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

# if "blueberries" in chilli_wishlist:
#     print("blueberries")
# else:
#     chilli_wishlist.append("blueberries")
#     print(chilli_wishlist)

# print(len(chilli_wishlist))
# if len(chilli_wishlist) > 8:
#     print("Chilli wants a lot of stuff!")

# if "tennis ball" in chilli_wishlist:
#     print("chilli would like a tennis ball.")
# else:
#     print("chilli doesnt want a tennis ball.")

# print(chilli_wishlist)
# print(chilli_wishlist[2])
# print(chilli_wishlist[-1])
# print(chilli_wishlist[3])
# print(chilli_wishlist[1:3])
# chilli_wishlist[1] = "carrot" - how to edit and override elements in the list
# print(chilli_wishlist)

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]
# # Print the sublist of items positions 2 through to 3
# # # Print the item in the -3 position

# # print(chilli_wishlist[2:4])
# # print(chilli_wishlist[-3])

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]
# chilli_wishlist[2] = "bowl"
# chilli_wishlist.append("dog mat")
# print(chilli_wishlist.extend(["kong", "tennis ball", "crocodile toy"]))
# chilli_wishlist.pop(2)
# chilli_wishlist.remove("igloo")
# print(chilli_wishlist)

# Q1
foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"]

# print(foods[0])
# print(foods[2])
# print(foods[9])
# print(foods[0:3])
# print(foods[7:10])
# print(foods[6][-1])


# Q2
# mailing_list = [
#     ["Chilli", "chilli@thechihuahua.com"],
#     ["Roary", "roary@moth.catchers"],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Ivy", "noreply@goldendreamers.xyz"], ]

# print(mailing_list[0][0] + ":" + mailing_list[0][1])
# print(mailing_list[1][0] + ":" + mailing_list[1][1])
# print(mailing_list[2][0] + ":" + mailing_list[2][1]
#       + "\n" + mailing_list[3][0] + ":" + mailing_list[3][1])


# Q3
# name = input("Please enter your name: ")
# name_2 = input("Please enter your name: ")
# name_3 = input("Please enter your name: ")
# name_lists = []
# name_lists = name + name_2 + name_3
# print(name_lists)

# Q4
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]
# d = []
# e = []
# # print(a + b + c)
# print([a] + [b] + [c])
