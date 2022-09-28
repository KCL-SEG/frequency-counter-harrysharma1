"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
"""Websites used for syntax:
    https://www.w3schools.com/python/python_strings_methods.asp
    https://www.w3schools.com/python/python_lists_methods.asp
    https://www.w3schools.com/python/python_dictionaries_methods.asp   
"""


def frequencies(items):
    for i in range(len(items)):
        items[i]=f'{items[i]}'
        
    frequencies = {}
    size=len(items)
    items.sort()
    while size>0:
        amount=0
        temp=items[0]
        amount=items.count(items[0])
        if frequencies.get(temp) is None:
            frequencies[f"{temp}"]=amount
        size-=1
        items.remove(temp)
        amount=0
        
        
    return frequencies

print(frequencies(['a','a','b','b','b','c']))
print(frequencies([100, 'Hello', '100', '100', 100]))
