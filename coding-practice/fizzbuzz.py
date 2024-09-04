class Solution(object):
    def fizzBuzz(self, n):
        fizzbuzz_arr = []
        fizz = 1
        buzz = 1
        for i in range(1, n+1):
            if fizz == 3 and buzz == 5:
                fizzbuzz_arr.append("FizzBuzz")
                fizz = 1
                buzz = 1
            elif fizz == 3:
                fizzbuzz_arr.append("Fizz")
                fizz = 1
                buzz += 1
            elif buzz == 5:
                fizzbuzz_arr.append("Buzz")
                buzz = 1
                fizz += 1
            else:
                fizzbuzz_arr.append(str(i))
                fizz += 1
                buzz += 1
        return fizzbuzz_arr
        