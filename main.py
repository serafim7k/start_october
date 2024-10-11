list_fruits = ["lemon", "orange", "apple", "kiwi"]

[list_fruits.append("mango") for i in list_fruits if i == "kiwi"]

print(list_fruits)