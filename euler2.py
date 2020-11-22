fib1 = 1;
fib2 = 2;
sum = fib2;

while fib2 + fib1 <= 4000000:
    tmp = fib2
    fib2 = fib2 + fib1
    fib1 = tmp
    if fib2 % 2 == 0:
        sum += fib2

print(sum)
