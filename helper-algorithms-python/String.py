# String létrehozása
my_string = "Hello, World!"

# String hosszának lekérdezése
length = len(my_string)  # Ebben az esetben: 13

# String karakterekre való hivatkozás (indexelés)
first_char = my_string[0]  # Az első karakter: 'H'
last_char = my_string[-1]  # Az utolsó karakter: '!'

# String szeletelése (substring)
substring = my_string[7:12]  # 'World'

# String műveletek
uppercase_string = my_string.upper()  # Nagybetűsítés
lowercase_string = my_string.lower()  # Kisbetűsítés
reversed_string =  my_string[::-1]  #fordított sorrend

# String összefűzése
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + ", " + string2  # 'Hello, World!'

# String-ek összefűzése f-strings segítségével (Python 3.6+)
name = "Alice"
greeting = f"Hello, {name}!"  # 'Hello, Alice!'

# Karakterlánc karaktereinek iterálása
for char in my_string:
    print(char)

# String keresése
if "Hello" in my_string:
    print("A 'Hello' szó megtalálható a stringben")

# String módosítása (stringként kezelhetetlen, mivel azok nem változhatnak)
# Példa: my_string[0] = 'J' hibát okozna

# Stringek szétválasztása egy adott elválasztó karakter alapján
csv = "apple,banana,orange"
split_result = csv.split(",")  # ['apple', 'banana', 'orange']

# Stringek összefűzése egy adott elválasztó karakterrel
words = ["apple", "banana", "orange"]
join_result = ", ".join(words)  # 'apple, banana, orange'
