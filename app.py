dictionary = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten"
}
output = ""
phone_number = input("Cell Phone Number: ")
numbers = list(phone_number)
try:
    for number in numbers:
        converted = dictionary.get(number)
        output = output + " " + converted
except TypeError:
    print("Please add 'Numbers' ONLY!")
print(output.strip())
























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