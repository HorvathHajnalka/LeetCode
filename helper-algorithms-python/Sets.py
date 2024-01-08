# Halmaz (Set) létrehozása
my_set = {1, 2, 3, 4, 5}

# Elemek hozzáadása a halmazhoz
my_set.add(6)

# Elemek eltávolítása a halmazból
my_set.remove(3)  # Hiba, ha az elem nincs a halmazban
my_set.discard(3)  # Az elem eltávolítása, ha benne van, különben hiba nélkül

# Elem jelenlétének ellenőrzése a halmazban
if 4 in my_set:
    print("A 4 benne van a halmazban")

# Halmazműveletek (Unió, Metszet, Különbség, Szimmetrikus Különbség)
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)  # {1, 2, 3, 4, 5}
intersection_set = set1.intersection(set2)  # {3}
difference_set = set1.difference(set2)  # {1, 2} vagy set1 - set2
symmetric_difference_set = set1.symmetric_difference(set2)  # {1, 2, 4, 5}

# Halmaz bejárása
for elem in my_set:
    print(elem)

# Halmaz hosszának lekérdezése
hossz = len(my_set)

# Üres halmaz létrehozása
ures_halmaz = set()

# Lista átalakítása halmazzá (Ismétlődő elemek eltávolításával)
lista = [1, 2, 2, 3, 4, 4, 5]
halmaz = set(lista)  # {1, 2, 3, 4, 5}
