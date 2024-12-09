import random
length = 10
random_numbers = [random.randint(3, 20) for i in range(length)]
print(random_numbers)

for i in random_numbers:
    print('')
    password = []
    for j in range(1, i):
        for k in range(1, i):
            if i % (j + k) == 0 and j != k:
                a = sorted([j, k])
                if not a in password:
                    password.append(a)

    print(f"{i}: {password}")


