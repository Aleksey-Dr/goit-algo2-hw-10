import random
import time
import matplotlib.pyplot as plt

# ANSI escape-послідовності для кольору та скидання кольору
RED = '\033[91m'
GREEN = '\033[92m' # Код для яскраво-зеленого кольору
YELLOW = '\033[93m'  # Код для яскраво-жовтого кольору
BLUE = '\033[94m'  # Код для яскраво-синього кольору
PURPLE = '\033[95m'  # Код для яскраво-фіолетового кольору
RESET = '\033[0m'

# 1. Реалізація рандомізованого QuickSort
def randomized_partition(arr, low, high):
    """
    Розбиття масиву з випадковим опорним елементом (pivot).
    """
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quick_sort_recursive(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort_recursive(arr, low, pi - 1)
        randomized_quick_sort_recursive(arr, pi + 1, high)

def randomized_quick_sort(arr):
    """
    Основна функція для запуску рандомізованого QuickSort.
    """
    randomized_quick_sort_recursive(arr, 0, len(arr) - 1)


# 2. Реалізація детермінованого QuickSort (опорний елемент - останній)
def deterministic_partition(arr, low, high):
    """
    Розбиття масиву, де опорний елемент - останній.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quick_sort_recursive(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quick_sort_recursive(arr, low, pi - 1)
        deterministic_quick_sort_recursive(arr, pi + 1, high)

def deterministic_quick_sort(arr):
    """
    Основна функція для запуску детермінованого QuickSort.
    """
    deterministic_quick_sort_recursive(arr, 0, len(arr) - 1)


# 3. Налаштування та запуск порівняльного аналізу
array_sizes = [10000, 50000, 100000, 500000]
num_runs = 5

avg_randomized_times = []
avg_deterministic_times = []

print(f"{BLUE}Порівняльний аналіз QuickSort:{RESET}\n")

for size in array_sizes:
    randomized_total_time = 0
    deterministic_total_time = 0

    for _ in range(num_runs):
        # Генеруємо випадковий масив для кожного запуску
        original_arr = [random.randint(0, 1000000) for _ in range(size)]

        # Тестуємо рандомізований QuickSort
        arr_rand = list(original_arr)
        start_time = time.perf_counter()
        randomized_quick_sort(arr_rand)
        end_time = time.perf_counter()
        randomized_total_time += (end_time - start_time)

        # Тестуємо детермінований QuickSort
        arr_det = list(original_arr)
        start_time = time.perf_counter()
        deterministic_quick_sort(arr_det)
        end_time = time.perf_counter()
        deterministic_total_time += (end_time - start_time)

    # Обчислюємо середній час
    avg_rand_time = randomized_total_time / num_runs
    avg_det_time = deterministic_total_time / num_runs

    avg_randomized_times.append(avg_rand_time)
    avg_deterministic_times.append(avg_det_time)

    print(f"{YELLOW}Розмір масиву:{RESET} {size}")
    print(f"   {GREEN}Рандомізований QuickSort{RESET}: {avg_rand_time:.4f} секунд")
    print(f"   {RED}Детермінований QuickSort{RESET}: {avg_det_time:.4f} секунд")

print("\n")

# 4. Вивід зведеної таблиці
print(f"{PURPLE}Зведена таблиця результатів:{RESET}")
print("-" * 50)
print(f"{f'{YELLOW}Розмір масиву{RESET}':<29} | {f'{GREEN}Рандомізований (сек){RESET}':<29} | {f'{RED}Детермінований (сек){RESET}':<25}")
print("-" * 50)

for size, rand_time, det_time in zip(array_sizes, avg_randomized_times, avg_deterministic_times):
    print(f"{size:<20} | {GREEN}{rand_time:<25}{RESET} | {RED}{det_time:<25}{RESET}")

print("-" * 50)
print("\n")

# 5. Побудова графіку
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, avg_randomized_times, label='Рандомізований QuickSort')
plt.plot(array_sizes, avg_deterministic_times, label='Детермінований QuickSort')
plt.xlabel(f'Розмір масиву')
plt.ylabel('Середній час виконання (секунди)')
plt.title('Порівняння рандомізованого та детермінованого QuickSort')
plt.legend()
plt.grid(True)
plt.show()