# Bonus: make it so the input has to be lower case and a string (movie ratings)

print("How old are you?")
age = str(input().lower())



if age >= 18:
    print("You can watch all movies!")
elif age >= 15:
    print("Sorry, you cannot watch 18 rated movies, but you can watch all other movies")
elif age >= 12:
    print("Sorry, you cannot watch 18 or 15 rated movies, but you can watch all other movies")
elif age >= 8:
    print("Sorry, you cannot watch 18, 15 or 12 rated movies, but you can watch all other movies")
else:
    print("Sorry, you can only watch U rated movies")