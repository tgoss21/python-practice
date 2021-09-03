# Hash map: A key-value store that uses an array and a hashing function to save and retrieve values.
# Key: The identifier given to a value for later retrieval.
# Hash function: A function that takes some input and returns a number.
# Compression function: A function that transforms its inputs into some smaller range of possible outputs.

# Recipe for saving to a hash table:
# - Take the key and plug it into the hash function, getting the hash code.
# - Modulo that hash code by the length of the underlying array, getting an array index.
# - Check if the array at that index is empty, if so, save the value (and the key) there.
# - If the array is full at that index continue to the next possible position depending on your collision strategy.

# Recipe for retrieving from a hash table:
# - Take the key and plug it into the hash function, getting the hash code.
# - Modulo that hash code by the length of the underlying array, getting an array index.
# - Check if the array at that index has contents, if so, check the key saved there.
# - If the key matches the one you're looking for, return the value.
# - If the keys don't match, continue to the next position depending on your collision strategy.

class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes) % self.array_size
    return hash_code + count_collisions

  def assign(self, key, value):
    array_index = self.hash(key)
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # Collision!
    number_collisions = 1
    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      current_array_value = self.array[new_hash_code]
      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return
      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return
      number_collisions += 1
    return

  def retrieve(self, key):
    array_index = self.hash(key)
    possible_return_value = self.array[array_index]
    if possible_return_value is None:
      return None
    if possible_return_value[0] == key:
      return possible_return_value[1]
    
    retrieval_collisions = 1
    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      possible_return_value = self.array[new_hash_code]
      if possible_return_value is None:
        return None
      if possible_return_value[0] == key:
        return possible_return_value[1]
      retrieval_collisions += 1
    return


hash_map = HashMap(15)
hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')
print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))
