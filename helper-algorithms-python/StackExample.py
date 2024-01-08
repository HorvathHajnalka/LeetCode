verem = []

def beszur(elem):
    verem.append(elem)

def kivesz():
    if not ures():
        return verem.pop()
    else:
        print("A verem üres, nem lehet elemet kivenni.")
        return None

def ures():
    return len(verem) == 0

# Teszteljük a verem működését
beszur(1)
beszur(2)
beszur(3)

print("Verem tartalma:")
print(verem)

utolso_elem = kivesz()
if utolso_elem is not None:
    print(f"Kivett elem: {utolso_elem}")
    
print("Verem tartalma a kivétel után:")
print(verem)
