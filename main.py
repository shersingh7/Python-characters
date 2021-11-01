## Dictionaries

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

# customer["name"] = "Davinder Verma"
#
# print(customer["name"])
# print(customer.get("dob", "1st Oct 2001"))


## Exercise

# phone = input("Phone: ")
#
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = ""
#
# for ch in phone:
#     output += digits_mapping.get(ch, "N.A") + " "
#
# print(output)


# ## Emoji
#
# message = input(">")
#
# words = message.split(' ')
#
# emojis = {
#     ":)" : "😁",
#     ":(" : "😔"
# }
# out = ""
# for word in words:
#     out += emojis.get(word, word) + " "
#
# print(out)