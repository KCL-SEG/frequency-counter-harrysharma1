"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""



def frequencies(items):
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
print(frequencies([100, 'Hello', 100, 100, 100]))
