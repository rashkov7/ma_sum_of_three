import time

import pytest

from task import (
    generate_random_array,
    max_sum_sorted_method,
    max_sum_cycles_stop_cycles,
    max_sum_cycles,
    maximum_delay,
    number_of_elements,
    numbers_range
)
arr_positive = ([1,2,3,4,5,20,15,30],54)
arr_negative = ([-1,-2,-3,-4,-20,-15,-30],-19)
arr_random_small = ([-1,-2,-3,-4,20,15,30],49)
arr_random_big = generate_random_array(number_of_elements, numbers_range)

arr = (arr_positive,arr_negative,arr_random_small,arr_random_big)

data = [
    (max_sum_sorted_method, arr),
    (max_sum_cycles_stop_cycles, arr),
    (max_sum_cycles, arr),
]
id_test = ["solution sorted solution", "solution with stopping flag", "solution nested cycles"]


@pytest.mark.parametrize("func, arr",data)
def test_work_with_positive_numbers_only_expected_output(func,arr):
    expected = arr[0][1]
    tested_arr = arr[0][0]
    result = func(tested_arr)
    assert expected == result

@pytest.mark.parametrize("func, arr",data)
def test_work_with_negative_numbers_only_expected_output(func,arr):
    expected = arr[1][1]
    tested_arr = arr[1][0]
    result = func(tested_arr)
    assert expected == result

@pytest.mark.parametrize("func, arr",data)
def test_work_with_random_numbers__expected_output(func,arr):
    expected = arr[2][1]
    tested_arr = arr[2][0]
    result = func(tested_arr)
    assert expected == result

@pytest.mark.parametrize("func, arr", data, ids=id_test)
def test_delay_for_each_solution(func, arr):
    start = time.time()
    func(arr[-1])
    end = time.time()
    t = end - start
    assert t < maximum_delay
