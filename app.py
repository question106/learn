








# Try Except ~~~~~~~~~~~~~~~~~~~~~~~
# print("type 'q' for quit")
# operating = True
#
# while operating:
#     age = input("Age: ")
#     if age == "q":
#         operating = False
#     else:
#         try:
#             print(int(age))
#         except ValueError:
#             print("Please input integers ONLY!")


# Reusable function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def translator(message):
#     words = message.lower().split(" ")
#     translations = {
#         "hello" : "안녕하세요",
#         "bye" : "안녕히게세요",
#         "thanx" : "감사합니다",
#         "my" : "제",
#         "name" : "이름",
#         "is" : "은",
#         "miss" : "보고싶다",
#         "you" : "너",
#         "love" : "사랑",
#     }
#
#     output = ""
#     for word in words:
#         output = output + translations.get(word, word) + " "
#     print(output)
#
#
# input = "Hello my name is sanjaa"
# translator(input)

# # Function Return~~~~~~~~~~~~~~~~~~~~~
# def square(number):
#     result = number * number
#     print(result)
#     return result * 10
#
# print(f"The Result: {square(3)}")



# First Function~~~~~~~~~~~~~~~
# def greeting():
#     print("Hi There!")
#     print("Welcome aboard")
#
#
# print("Start")
# greeting()
# print("Finish")


# Translator~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# message = input(">>>").lower()
# words = message.split(" ")
# translations = {
#     "hello" : "안녕하세요",
#     "bye" : "안녕히게세요",
#     "thanx" : "감사합니다",
#     "my" : "제",
#     "name" : "이름",
#     "is" : "은",
#     "miss" : "보고싶다",
#     "you" : "너",
#     "love" : "사랑",
# }
#
# output = ""
# for word in words:
#     output = output + translations.get(word, word) + " "
# print(output)

# Number to word converter ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# phone = input("Phone: ")
#
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine",
#     "10": "Ten"
# }
#
# output = ""
# for ch in phone:
#     output = output + digits_mapping.get(ch, "letter") + " "
# print(output)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# dictionary = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine",
#     "10": "Ten"
# }
# output = ""
# phone_number = input("Phone: ")
# numbers = list(phone_number)
# try:
#     for number in numbers:
#         converted = dictionary.get(number)
#         output = output + " " + converted
# except TypeError:
#     print("Please add 'Numbers' ONLY")
# print(output.strip())


#Dictionaries~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
# customer["birthdate"] = "Jan 6 1991"
# print(customer.get("birthdate"))

# Tuples~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# numbers = (1,2,3)
# numbers[2] = 99
# print(numbers.index(2))
#




#Remove Duplicated Numbers~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# numbers = [5,2,8,8,8,8,4,6,6,7,9,5,5,5,5]
# numbers2 = []
#
#
# for number in numbers:
#     numbers2.append(number)
#     if numbers2.count(number) > 1:
#         numbers2.remove(number)
#
#
# print(numbers2)
#
#
#


#Find the biggest number~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# numbers = [13,4,5,7,32,6,7,8,1,2,4]
#
# output = 0
# for number in numbers:
#     if output < number:
#         output = number
# print(output)

#Write "F" with Xs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# numbers = [2, 2, 2, 2, 5]
#
# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#         output = output + "x"
#     print(output)

# Create Matrix~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# for x in range(4):
#     for y in range(4):
#         for z in range(4):
#             print(f"({x}, {y}, {z})")


#Total Price~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# prices = [10, 20, 30, 40, 50, 60]
#
# total = 0
# for price in prices:
#     total = total + price
#
# print(f"Total: {total}")