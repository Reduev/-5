import random
import math
import statistics

random_numbers = [random.randint(1, 100) for _ in range(100)]

average = sum(random_numbers) / len(random_numbers)

median = statistics.median(random_numbers)

std_deviation = statistics.stdev(random_numbers)

sum_of_numbers = sum(random_numbers)
sqrt_of_sum = round(math.sqrt(sum_of_numbers), 2)

print(f"Среднее: {average:.2f}, Медиана: {median}, Стандартное отклонение: {std_deviation:.2f}, Корень из суммы: {sqrt_of_sum}")