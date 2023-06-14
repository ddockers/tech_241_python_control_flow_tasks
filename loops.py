# for loops and while loops

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Bronson", "money": "£0.05"},
    2: {"name": "Masha", "money": "$3.66"},
    3: {"name": "Roscoe", "money": "$1.14"}
}

for num in list_data:  # num is the iterator
    print(num * 2)

# nested loops
# a loop that loops within a loop

for data in embedded_lists:
    print(data) # it still prints out the list
    for num in data:
        print(num) # Before going to the next list, it prints out each individual element

# looping through dictionaries
for value in dict_data:
    print(value) # this prints out 1 2 3

for item in dict_data.values():
    print(item) # this prints out the dict values

for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)

# a loop that only prints the money
for items in dict_data.values():
    print(items["money"])

# loops and if statements
for num in list_data:
    if num == 3:
        print("You have found three!")
    elif num > 3:
        print("You've gone too far")
    else:
        print("Too soon!")