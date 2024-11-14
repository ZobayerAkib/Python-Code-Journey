from collections import Counter

category=['A','B','C',
          'B','C','A',
          'A', 'B', 'C',
          'B'] # A list to check counter class of python collection

#Without Counter: A for loop iterates over each item in category and
# updates a dictionary freq by checking if the item is already in the dictionary.
# If it is, it increments the count; if not, it adds the item with a count of 1.

freq={} #A dictionary

for i in category:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(f"The frequency without counter: {freq}")

#With Counter: The Counter class from Python's collections module automatically counts each element in the category list
# and returns a Counter object (a specialized dictionary with counts).

freq1=Counter(category)
print(f"The frequency with counter: {freq1}") # a counter object
print(f"The frequency with counter: {dict(freq1)}") # a dictionary