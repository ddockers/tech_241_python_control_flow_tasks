# Control flow

# Like giving Python a recipe or order to do things

# Conditional statements

# Asking a question, and making a decision based on the answer. If this is true, do this thing. If not, do something else.

# Cinema task
print("How old are you?")
age = int(input())

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