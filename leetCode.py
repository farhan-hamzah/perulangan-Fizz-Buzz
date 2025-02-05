# FizzBuzz
num = int(input())
hasil = []
c = 1
while c <= num:
    if c%15 == 0:
        hasil.append("FizzBuzz")
    elif c%3 == 0:
       hasil.append("Fizz")
    elif c%5 == 0:
        hasil.append("Buzz")
    else:
        hasil.append(c)
    c += 1
print(hasil)

