# Aurelien Meray
# PI: 5920312
# NOTE: to compile, make sure you are using python3 (alias python = python3)

print("Welcome to Mad Libs called 'My Trip to Disney World!'\n")
print("Enter a Friend's name" , end=' ')
friendName = input()
print("Enter an integer" , end=' ')
numHours = input()
print("Enter a Vehicle" , end=' ')
vehicle = input()
print("Enter an adjective" , end=' ')
adj1 = input()
print("Enter an adjective" , end=' ')
adj2 = input()
print("Enter an 'ing' verb" , end=' ')
verb1 = input()
print("Enter an animal" , end=' ')
animal = input()
print("Enter an adjective" , end=' ')
adj3 = input()
print("Enter a past tense verb" , end=' ')
verb2 = input()
print("Enter an adjective" , end=' ')
adj4 = input()
print("Enter a noun" , end=' ')
noun = input()
print("Enter a past tense verb" , end=' ')
verb3 = input()
print("Enter another past tense verb" , end=' ')
verb4 = input()
print("Enter a place" , end=' ')
place = input()
print("Enter a verb" , end=' ')
verb5 = input()

print(f"""

Last month, I went to Disney World with {friendName}.
We traveled for {numHours} hours by {vehicle}.
Finally, we got there and it was very {adj1}.
There were {adj2} people {verb1} everywhere.
There were also people dressed up in {animal} costumes.
I wish it had been more {adj3}, but we {verb2} anyway.
We also went on some {adj4} rides, called "Magic {noun}".
{friendName} nearly fell off a ride and had to be {verb3}. 
Later we went to the hotel and {verb4}.
Next year, I want to go to {place}, where we can {verb5}.

""")

