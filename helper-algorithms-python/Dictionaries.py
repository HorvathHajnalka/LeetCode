#ha ismétlődő értékeket kell keresni
# Creating a dictionary
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Accessing values by key
print(my_dict['name'])  # Output: John

# Modifying values
my_dict['age'] = 31
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Adding a new key-value pair
my_dict['country'] = 'USA'
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}

# Removing a key-value pair
del my_dict['city']
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'country': 'USA'}

# Checking if a key is in the dictionary
if 'age' in my_dict:
    print('Age is present in the dictionary')

# Getting the keys and values
keys = my_dict.keys()
values = my_dict.values()
print('Keys:', keys)     # Output: Keys: dict_keys(['name', 'age', 'country'])
print('Values:', values) # Output: Values: dict_values(['John', 31, 'USA'])

# Iterating through the dictionary
for key, value in my_dict.items():
    print(f'{key}: {value}')

# Getting the length of the dictionary
length = len(my_dict)
print('Dictionary Length:', length)  # Output: Dictionary Length: 3
