from LinkedList import LinkedList, Node

### Hash Table LinkedList ###
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """
    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here
        return self.size / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """
        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for char in key:
            hash = (( hash << 5) + hash) + ord(char)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % len(self.storage)

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        hashed_key = self.hash_index(key)
        if self.storage[hashed_key] != None:
            linkedList = self.storage[hashed_key]
            linkedList.add_to_head((key, value))
        else:
            self.storage[hashed_key] = LinkedList(Node((key, value)))

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        hashed_key = self.hash_index(key)
        if self.storage[hashed_key] == None:
            return None

        if len(self.storage[hashed_key]) >= 1:
            self.storage[hashed_key].remove(key)
        else:
            self.storage[hashed_key].head = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        hashed_key = self.hash_index(key)
        if self.storage[hashed_key] == None:
            return None

        if len(self.storage[hashed_key]) >= 1:
            current_head = self.storage[hashed_key].head

            while current_head != None:
                if current_head.value[0] == key:
                    return current_head.value[1]
                current_head = current_head.next
            return None
        else:
            return self.storage[hashed_key].head.value[1]

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        self.capacity = new_capacity
        value_key_pair = []
        # Get all key-value from store
        # Resize Storage
        # Calculate hash key and insert them in resized storage

        # Deep copy
        for store in self.storage:
            if len(store) >= 1:
                current_head = store.head
                while current_head != None:
                    value_key_pair.append(current_head.value)
                    current_head = current_head.next
            else:
                value_key_pair.append(store[0])
        # print(value_key_pair[0])
        self.storage = [None] * self.capacity

        for key_value in value_key_pair:
            self.put(key_value[0], key_value[1])

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")
    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
