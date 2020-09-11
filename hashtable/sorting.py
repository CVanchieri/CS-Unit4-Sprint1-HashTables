
### Questions ###

# Can you sort a hash table?
## no
## we do not know where things will be put

# Do hash tables preserve order?
## no
## the hash function puts keys at random indices

# Can you sort a dictionary?
## yes
## Python 3.5+ keys are kept in order enetered
## Does that impact the time complexity for dict over regular hash tables?
## Contrast to JS: when loopping over object items, order is not guaranteed
## Means JS object is a little closer to a pure hash table than the Python dict is

# Even with a Python dictionary, you can't sorted
## We want to print these items, by key, descending

# How could we sort the keys?
d = {
    'foo': 12,
    'bar': 10,
    'quux': 21
    }

for pair in d.items():
    print(pair)

list(d.items())

sorted_list = list(d.items()).sort()
print(sorted_list)

my_list = list(d.items())
print(my_list)

my_list.sort()

for pair in my_list:
    print(pair)

## use.items() and sort the tuples

# Two common functions/methods for sorting in Python?
## .sort(), sorted(arr)

## .items() returns a 'dict_items' object
## can use sorted(), not .sort()...

## could use list comprehension

## iterable: any data structure you can run a for loop on

my_list = list(d.items())
my_list.sort(reverse=True) # sorts in ascending order, by default, reverse=TRue to decende instead
print(my_list)

for pair in my_list:
    print(pair)

my_list.sort(key = lambda tupl: tupl[1]) # sort by value instead of key. optional function argument

## JS: (a, b) => a * b
## Python: Lambda x, y: x * y


# Given a string, print the number of occurences of each letter

## Print starting with the most numberous letter, down to least numerous

# Store leter as dict key with value of 0, each time the letter appears, increase value by 1
## how to handle spaces?
## how to handle upper and lower case?

string_to_count = 'The quick brown fox jumps of the lazy dog'

def letter_counts(s):
    d = {}
    for letter in s:
        letter = letter.lower()
        if letter == " ":
            continue
         # d[letter] = letter.count()
        elif letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1

    return d

print(letter_counts(string_to_count))

def print_letters(s):
    counts_dict = letter_counts(s)
    ## sort by value
    counts_list = list(counts_dict.items())
    counts_list.sort(reverse = True, key = lambda x: x[1]) # sort by value, and in descending order
    ## loop through and print
    for pair in counts_list:
        print(f'count: {pair[1]} letter: {pair[0]}')

print(print_letters(string_to_count))
