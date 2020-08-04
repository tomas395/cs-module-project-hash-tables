# ## Day 1

# Task: Implement a basic hash table without collision resolution.

# 1. Implement a `HashTable` class and `HashTableEntry` class.

# 2. Implement a good hashing function.

#    Recommend either of:

#    * DJB2
#    * FNV-1 (64-bit)

#    You are allowed to Google for these hashing functions and implement
#    from psuedocode.

# 3. Implement the `hash_index()` that returns an index value for a key.

# 4. Implement the `put()`, `get()`, and `delete()` methods.

# You can test this with:

# ```
# python test_hashtable_no_collisions.py
# ```

# The above test program is _unlikely_ to have collisions, but it's
# certainly possible for various hashing functions. With DJB2 (32 bit) and
# FNV-1 (64 bit) hashing functions, there are no collisions.


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
        self.capacity = capacity
        self.bucket_arr = [None] * capacity
        self.total = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.bucket_arr)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
            hash &= 0xFFFFFFFF
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        bucket_index = self.hash_index(key)
        self.bucket_arr[bucket_index] = value
        self.bucket_arr.append(value)
        self.total += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        bucket_index = self.hash_index(key)
        if self.bucket_arr[bucket_index] is None:
            print("Your value is not contained in the index.")
        else:
            del self.bucket_arr[bucket_index]
            self.total -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        bucket_index = self.hash_index(key)
        if self.bucket_arr[bucket_index] is None:
            return None
        else:
            return self.bucket_arr[bucket_index]

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

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
