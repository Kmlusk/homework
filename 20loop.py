# 20loop.py

# Print out the numbers from 5 to less than 50 in steps of 7

# Hint: use the 3 argument form of range()

# Your code goes here
start = 5
end = 50

if start % 3 != 0:
	for num in range(start, end +2, 3):
		print(num, end=" ")
else:
	for num in range(start +2, end +2, 3):
		print(num, end=" ")

"""
python3 20loop.py
5
12
19
26
33
40
47
"""
