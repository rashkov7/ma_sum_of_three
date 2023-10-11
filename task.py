import random
import time

number_of_elements = 550
numbers_range = (-100000, 500000)
maximum_delay = 1.5


def execution_time(func):
    """
    Decorator to measuring function execution time.
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"\nExecution time - ({func.__name__}): {end - start:0.3f}s")
        return result

    return wrapper


def generate_random_array(range_of_array: int, number_range: tuple) -> list:
    """
    Generating random array
    :param range_of_array: How many elements will contain the array
    :param number_range: The biggest possible number
    :return: list
    """
    random_numbers = []
    for _ in range(range_of_array):
        random_numbers.append(random.randint(number_range[0], number_range[1]))
    return random_numbers


@execution_time
def max_sum_cycles(random_arr: list) -> float:
    """
    The maximum sum of three non-adjacent elements in A. Using nested cycles method
    :param random_arr: Array for given task
    :return: float -> result
    """
    max_value = float('-inf')
    n = len(random_arr)
    for i in range(n):
        for j in range(i + 2, n):
            for k in range(j + 2, n):
                current_sum = random_arr[i] + random_arr[j] + random_arr[k]
                if current_sum > max_value:
                    max_value = current_sum
    return max_value


@execution_time
def max_sum_cycles_stop_cycles(random_arr: list) -> float:
    """
    The maximum sum of three non-adjacent elements in A. Using nested cycles method but optimized with stop cycles variable.
    If current sum reaches that variable we stop all cycles and return results.
    :param random_arr: Array for given task
    :return: float -> result
    """
    sorted_arr = sorted(random_arr, reverse=True)
    max_sum = sum(sorted_arr[:3])

    max_value = float('-inf')
    n = len(random_arr)
    for i in range(n - 4):
        for j in range(i + 2, n - 2):
            for k in range(j + 2, n):
                current_sum = random_arr[i] + random_arr[j] + random_arr[k]
                if current_sum > max_value:
                    max_value = current_sum
                    if current_sum == max_sum:
                        return max_value
    return max_value


@execution_time
def max_sum_sorted_method(random_arr: list) -> float:
    """
    The maximum sum of three non-adjacent elements in A. Using Sorting method
    :param random_arr: Array for given task
    :return: float -> result
    """

    sorted_array = sorted(enumerate(random_arr), key=lambda x: x[1], reverse=True)
    new_arr = sorted_array[:6]

    max_value = float('-inf')
    current_sum = float('-inf')
    for i in range(4):
        selected_elements = set()
        all_values = []
        if max_value < current_sum:
            max_value = current_sum
            selected_elements.add(new_arr[i][0])
        for indx, value in new_arr:
            if not indx + 1 in selected_elements and not indx - 1 in selected_elements:
                all_values.append(value)
                selected_elements.add(indx)
                if len(all_values) == 3:
                    current_sum = sum(all_values)
                    break
    return max_value


# a = generate_random_array(number_of_elements, numbers_range)
# print("")
# print(f"Elements in tested array: {number_of_elements}, bound: {numbers_range}")
# print(f"Result: {max_sum_cycles(a)}")
# print(f"Result: {max_sum_cycles_stop_cycles(a)}")
# print(f"Result: {max_sum_sorted_method(a)}")

