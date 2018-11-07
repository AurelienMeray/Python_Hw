# Aurelien Meray
# PI: 5920312
# NOTE: to compile, make sure you are using python3 (alias python=python3)

print("Welcome to Mad Libs called 'My Trip to Disney World!'\n")
question = ['a Friends name', 'an integer', 'a vehicle', 'an adjective', 'an adjective',
 			'an ing verb', 'an animal', 'an adjective', 'a past tense verb','an adjective',
 			'a noun', 'a past tense verb', 'a past tense verb','a place', 'a verb']
answer=[]
for i in range(15):
	print("Enter", question[i])
	data=input()
	answer.append(data)

print(f"""
Last month, I went to Disney World with {answer[0]}.
We traveled for {answer[1]} hours by {answer[2]}.
Finally, we got there and it was very {answer[3]}.
There were {answer[4]} people {answer[5]} everywhere.
There were also people dressed up in {answer[6]} costumes.
I wish it had been more {answer[7]}, but we {answer[8]} anyway.
We also went on some {answer[9]} rides, called "Magic {answer[10]}".
{answer[0]} nearly fell off a ride and had to be {answer[11]}. 
Later we went to the hotel and {answer[12]}.
Next year, I want to go to {answer[13]}, where we can {answer[14]}.
""")
