my_arr  = ["hi", "world", "how", "are", "you", "lorem", "ipsum", "set"]

# Search for an element in an arrray
'''
Linear Search
'''
## O(n) -- Linear Search
def find_elemt(arr, el):
    for thing in arr:
        if thing == el:
            return True
    return False

'''
Binary Search
'''
## O(log n) -- Binary Search
def find_elemt(arr, el):
    pass


'''
Hash Tables = arrays + hashing function
'''
# which Big O complexity is faste than log n? -- Constant time O(1)
# if we increase the input we still take the same number of steps to find what we're looking for.

## O(1) -- Hash Tables
'''
def magic_fun_find_index(arr, el):
    return el_index

idx = magic_fun_find_index(my_arr, "set") ## 7
my_arr[idx]
'''
### write a function that will take a string and return a number ###
def len_hash(str):
    return len(str)
# a lot of collisions
print(len("sad") == len("sad"))
print(len("ball") == len("hats"))

# Fast
# Deterministic


# add up the ASCII or unicode
# UTF-8
# use .encode()


## a: 1
## b: 2

def UTF8_hash(str):
    total = 0
    utf_bytes = str.encode()
    for byte in utf_bytes:
        total += byte

    return total

print(UTF8_hash('sad'))
print(UTF8_hash('was'))

UTF8_hash('dad')
UTF8_hash('add')

print(UTF8_hash('supercalifragilisticexpialidocious'))


# but we still have collisions

# a hash function: takes a string, gives back a number
# operate on the bytes that make up the string
# Deterministic

# to improve hash functions, make output more unique!
# SHA256

# Hash function + array!!
# hash function gives us back some big number
# how to map the output of our hash function to an index in an array?

### array filled with 20 None's

# 'put' into our array
my_arr2 = [None] * 2000

our_hash = UTF8_hash('supercalifragilisticexpialidocious') ## 3643
idx = our_hash % len(my_arr2)
my_arr2[idx] = 'Mary Poppins'

print(my_arr2)

# 'get'
our_hash = UTF8_hash('supercalifragilisticexpialidocious') ## 3643
idx = our_hash % len(my_arr2)
val = my_arr2[idx] = 'Mary Poppins'

print(val)

## KEy value store
# 'supercalifragilisticexpialidocious' is the key
# 'Mary Poppins' is the value

# Hash tablie in programming languages?
## Python: dictionary
## JS: object
## Hash map
## Map

## Pseudocode for put
# 1. hash the key
# 2. take hte hash and mod it with len of array
# 3. go to index and put in the value

## Pseudocode for get
# 1. hash the key
# 2. take the hash and mod it with the len of aray
# 3. go th index and get out the value

## Time complexity?
# same for get and put
# linear in length of string/key
# constant time in length of array <--- this is what we pay attention to
# O(1) runtime

## Collision
key1 = 'dad'
key2 = 'add'

# put 1
hash1 = UTF8_hash(key1)
idx1 = hash1 % len(my_arr2)
my_arr2[idx1] = 'howdy'

# put 2
hash2 = UTF8_hash(key2)
idx2 = hash2 % len(my_arr2)
my_arr2[idx2] = 'whats up yall'

# get
get_hash = UTF8_hash(key1)
idx3 = hash2 % len(my_arr2)
print(my_arr2[idx3])


# even when we use our hash function with modulo, we get collisions
# to be solved later

# we wrote our own hash function, what about Pythons hash()?
# many different hash functions! can also hash()

# when used with hash tables, hashing function should be Fast
# why? we want O(1), and a lot of lookups

# other uses of hash functions
# passwords!!
# encryption/decryption

# password --> hashing function --> hashed_pasword in db
# password --> hashing function --> hash === hashed_pasword ??

## here hash function should be slow

### SHA-256 has never had a collision
## can use the output (hash) as a fingerprint for your string




# how to turn result of hash function into a usable index?
## modulo the hash with len(my_arr2)

'''
Modulo demonstration
modulo returns from 0 to len(list) - 1
1 % 20 --> 1
15 % 20 --> 15
2- % 20 --> 0
21 % 20 --> 1
22 % 20 --> 2
39 % 20 --> 19
40 % 20 --> 0
'''
