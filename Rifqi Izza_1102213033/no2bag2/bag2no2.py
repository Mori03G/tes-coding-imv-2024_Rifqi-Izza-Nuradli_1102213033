def check_fib(n):
    import math
    a = (5 * (n**2)) + 4
    b = (5 * (n**2)) - 4
    return (math.sqrt(a)).is_integer() or (math.sqrt(b)).is_integer()

n = int(input('Masukan Angka: ' ))
result = check_fib(n)
if (result):
    print(f"Angka {n} merupakan angka fibonnaci ")
else:
    print(f"Angka {n} Bukan angka fibonnaci ")