# Fibonacci rekurzióval - O(2^n)
def fibonacci(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibonacci(i - 1) + fibonacci(i - 2) #  return meghatározása!!!!!!

# Optimalizált Fibonacci - O(n)
def fibonacci2(n):
    memo = [-1] * (n + 1) #létrehozunk egy listát, minden elemét -1re állítjuk, jelezve, hogy még nem számoltuk ki
    return fibonacci2_helper(n, memo) # meghívjuk a rekurzív függvényt

def fibonacci2_helper(i, memo):
    if i == 0 or i == 1:
        return i
    if memo[i] == -1:
        memo[i] = fibonacci2_helper(i - 1, memo) + fibonacci2_helper(i - 2, memo) # csak akkor számol ha még nem számoltuk ki, különben csak visszaadja
    return memo[i] 

# Példák:
n = 10
print(f"Fibonacci({n}) = {fibonacci(n)}") # Rekurzióval számolva
print(f"Fibonacci2({n}) = {fibonacci2(n)}") # Optimalizált módszerrel számolva
