a = 4293
b = 8548

s = []

for n in range(a, b):
        if n % 2 == 1:
                s.append(n)

print sum(s)
