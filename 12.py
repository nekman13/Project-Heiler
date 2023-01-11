import math
from time import perf_counter

def heiler_12(min_count_divisor):
    triangle_num, plus_num = 0, 0
    while True:
        plus_num += 1
        triangle_num += plus_num
        count_divisor = 2
        for divisor in range(2, (int(math.sqrt(triangle_num)) + 1)):
            if triangle_num % divisor == 0:
                count_divisor += 2
        sqrt_num = math.ceil(math.sqrt(triangle_num))
        if sqrt_num ** 2 == triangle_num:
            count_divisor -= 1
        if count_divisor > min_count_divisor:
            print(f'Больше {min_count_divisor} у {triangle_num}')
            break

start = perf_counter()
heiler_12(1000)
finish = perf_counter()
print(finish - start)