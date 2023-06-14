# Is it hot? No, really? Is it really??

"""
Make a new program with same functionality
but takes temperature from the user and gives an
output based on the temperature
"""

print("What is the temperature today in degrees Celsius?")
temp = int(input())

if temp >= 28:
    print("Yeah, you're right. It's well hot!")
elif temp >= 20:
    print("It's pretty warm, yeah")
elif temp >= 12:
    print("Typical British summer, innit?")
elif temp >= 7:
    print("How is it THIS cold in Spring??")
else:
    print("We're gonna have to bite the bullet and turn the heating on")