import numpy as np
import matplotlib.pyplot as plt
import numpy
import time
import math

nums_usable = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rand_pool = []
rand_distrib = []
test_prime_num = 0


def prime_primitive_test(num):
    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(num))):
        if ((num % i) == 0):
            return False
    return True


def ferma_test(num, dual, base_max):
    ba = bb = numpy.random.randint(2, base_max + 1)
    if dual:
        while ba == bb:
            bb = numpy.random.randint(2, base_max + 1)
        if pow(bb, num - 1, num) != 1:
            return False
    if pow(ba, num - 1, num) != 1:
        return False
    return True


def miller_rabin(num, passes):
    def mr_cycle(a):
        if pow(a, d, num) == 1:
            return False
        for i in range(s):
            if pow(a, (2 ** i) * d, num) == (num - 1):
                return False
        return True

    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    s = 0
    d = num - 1
    while (d & 1) == 0:
        d >>= 1
        s += 1
    assert (((2 ** s) * d) == (num - 1))
    for _ in range(passes):
        a = numpy.random.randint(2, num)
        if mr_cycle(a):
            return False
    return True


for _ in range(10 ** 5):
    a = numpy.random.randint(1, 10 ** 9)
    rand_pool += [a]
    i = 0
    while a > 0:
        a //= 10
        i += 1
    nums_usable[i] += 1
rand_pool.sort()

print("Числа:", rand_pool)
print("Значащие цифры:", nums_usable)

rtime = time.perf_counter()

for num in rand_pool:
    if ferma_test(num, False, 100):
        test_prime_num += 1

print("Время (сек) Ферма 1:", time.perf_counter() - rtime)
print("Колво простых чисел Ферма 1:", test_prime_num)
test_prime_num = 0
rtime = time.perf_counter()

for num in rand_pool:
    if ferma_test(num, True, 100):
        test_prime_num += 1

print("Время Ферма 2:", time.perf_counter() - rtime)
print("Колво простых чисел Ферма 2:", test_prime_num)
test_prime_num = 0
rtime = time.perf_counter()

for num in rand_pool:
    if miller_rabin(num, 1):
        test_prime_num += 1

print("Время Миллера-Рабина 1:", time.perf_counter() - rtime)
print("Колво простых чисел Миллера-Рабина 1:", test_prime_num)
test_prime_num = 0
rtime = time.perf_counter()

for num in rand_pool:
    if miller_rabin(num, 2):
        test_prime_num += 1

print("Время Миллера-Рабина 2:", time.perf_counter() - rtime)
print("Колво простых чисел Миллера-Рабина 2:", test_prime_num)
test_prime_num = 0
rtime = time.perf_counter()

for i in range(1, len(rand_pool) + 1):
    if prime_primitive_test(rand_pool[i-1]):
        test_prime_num += 1
    rand_distrib += [test_prime_num / i]

print("Время примитивный", time.perf_counter() - rtime)
print("Колво простых чисел примитивный:", test_prime_num)
test_prime_num = 0
rtime = time.perf_counter()

print("Расперделение простых чисел по массиву (плотность [1, n]):",
      rand_distrib)

# Гистограмма распределения
for i in range(len(nums_usable)):
    nums_usable[i] = math.log(nums_usable[i] + 1, math.e)

x = np.arange(0, len(nums_usable))
y = np.array(nums_usable)

fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set_facecolor('seashell')
fig.set_facecolor('white')
fig.set_figwidth(6)    #  ширина Figure
fig.set_figheight(6)    #  высота Figure
plt.show()

# График распределения простых чисел
x = np.arange(0, len(rand_distrib))
y = np.array(rand_distrib)

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_facecolor('seashell')
fig.set_facecolor('white')
plt.show()

# График распределения простых чисел
temp = []
print(len(rand_pool))
print(len(rand_distrib))
for i in range(len(rand_pool)):
    temp.append(math.log(rand_pool[i]) * rand_distrib[i])

x = np.arange(0, len(temp))
y = np.array(temp)

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_facecolor('seashell')
fig.set_facecolor('white')
plt.show()
