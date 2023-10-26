"""

You want to make a dictionary that is subset of
another dictionary

"""

prices = {
    'A': 45.23,
    'B': 100,
    'C': 300,
    'D': 235
}

p1 = {key:value for key, value in prices.items() if value > 100}

print(p1)