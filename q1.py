def emod(a,b,c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        d = emod(a, b//2, c)
        return (d * d) % c
    else:
        return ((a % c) * emod(a, b - 1, c)) % c

def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
          
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1

def fibonacciModulo(n, m): 
    pisano_period = pisanoPeriod(m) 
      
    n = n % pisano_period 
      
    previous, current = 0, 1
      
    for i in range(n-1): 
        previous, current = current, previous + current 
          
    return (current % m) 

def prepare_fib_list(n, mod_value):
    results = []
    for i in range(n):
        results.append(fibonacciModulo(i, mod_value))
    return results

x = 100
n = pow(10, 15)
mod_value = 13 * 11 * 7 * 5 * 3 * 2 * 1  # 15 faktoriyeldeki carpanlar
result = 0
array = prepare_fib_list(n, mod_value)
print("Dizi olusturuldu")

for i in range(1, x + 1):  # x = 100
    for j in range(n):  # n = 10^15
        a = emod(i, j, mod_value)
        b = array[j]
        result += (a * b) % mod_value
print("Mod value is " , result)