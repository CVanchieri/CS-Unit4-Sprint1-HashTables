

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

'''
HasTable with UTF8
'''
### UTF8 ###
print('''--- UTF8 HashTable ---''')
def UTF8_hash(str):
    total = 0
    utf_bytes = str.encode()
    for byte in utf_bytes:
        total += byte

    return total

print(f"what is the hash for sad?, {UTF8_hash('sad')}")
print(f"what is the hash for was?, {UTF8_hash('was')}")

print(f"what is the hash for dad?, {UTF8_hash('dad')}")
print(f"what is the hash for add?, {UTF8_hash('add')}")
print(f"---> 'dad' & 'add' have a 'collision', dad = {UTF8_hash('dad')} add = {UTF8_hash('add')}")
print(f"what is the hash for Supercalifragilisticexpialidocious?, {UTF8_hash('Supercalifragilisticexpialidocious')} \n")

def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100

'''
HashTable with ASCII
'''
### ASCII ###
print('''--- ASCII HashTable ---''')
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val): # set (add) item to a hashtable
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key): # get item from a hashtable
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self,key): # delete an item from a hashtable
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable() # set the HashTable class
print(f" March 6 should be 9, {t.get_hash('march 6')}") # standard ACII '9'
t['march 6'] = 130 # set march 6 equal to 130
t['march 1'] = 20 # set march 1 equal to 20
t['dec 17'] = 20 # set dec 17 equal to 20
print('''March 6 was changed to 130
March 1 was added as 20
Dec 17 was added as 20
''')
print(f" March 6 should be 130, {t['march 6']}") # print the march 1 from the hashtable
print(f" March 1 should be 20, {t['march 1']}") # print the march 1 from the hashtable
del t['march 1'] # delete march 1 from the hashtable
print(f" March 1 was removed and should be None, {t['march 1']}") # print the march 1 from the hashtable
print(f" Dec 17 should be 20, {t['dec 17']}") # print the march 1 from the hashtable
print(f" HashTable = {t.arr}") # print the full array

print(f" March 6 is index = {t['march 6']}, March 17 is index = {t['march 17']}, this is a 'collision'")

t['march 17'] = 459

print(f" March 17 was changed to 459, {t['march 17']}")
print(f" With March 17 changed to 459, {t['march 17']}, due to the collision with March 6, March 6 now is {t['march 6']} as well")
print(f" HashTable = {t.arr}")


'''
HashTable Collions
'''
print('''--- HashTable Collisions ---''')
### Collisions ###
# happen when multiple keys are being stored at the same index

### Seperate Chaining  ###
# stores a list/linked list at each index instead of a single key

### Linear Probing ###
# when adding a key to an index, if the index is filled it moves to the next index that is empty, if at the end of the list it goes back to the start

class HashTable:
    def __init__(self):
        self.MAX = 10
        #self.arr = [None for i in range(self.MAX)]
        self.arr = [[] for i in range(self.MAX)] # fix collision with the use [] empty list instead of 'None'

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val): # set (add) item to a hashtable
        h = self.get_hash(key)
        found = False
        #self.arr[h] = val
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True # if found break loop
                break
        if not found: #
            self.arr[h].append((key, val)) # add key to list if not there


    def __getitem__(self, key): # get item from a hashtable
        h = self.get_hash(key)
        # return self.arr[h]
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]


    def __delitem__(self, key): # delete an item from a hashtable
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

t = HashTable() # set the HashTable class

t['march 6'] = 78
t['march 8'] = 67
t['march 9'] = 4
t['march 17'] = 459

print(f" March 6 was changed to 78, {t['march 6']}")
print(f" March 8 was added as 67, {t['march 8']}")
print(f" March 9 was added as 4, {t['march 9']}")
print(f" March 17 was changed to 459, {t['march 17']}")
print(''' # Colission Solved # ''')
print(f" Adjusting the hashtable to work with a 'list' on the index, March 17 459, and March 6 78, no longer collide")
print(f" HashTable = {t.arr}")

print(f" March 17, {t['march 17']} is being deleted")
del t['march 17']
print(" March 17 is gone")
print(f" HashTable = {t.arr}")









'''

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
