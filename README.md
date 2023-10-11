# Max Sum of three
Improve performance of task

## Two solutions with times better performance than the original one.
### *First one is that I show you during the meeting with Stop Cycle Flag.
In that solution we try to stop all iteration as soon as possible. 
To do that, we find the maximum possible sum of three elements of given array and then assigned to variable (_max_sum_). When current sum of 3 elements is equals to that max_sum we stop iterration and  return the result. It is not the best solution but as you see it works.
       
### *Second one we sorted elements.
   First we sorted the given array in descended order and take first six elements in the new array, than we assigned result to different variable. All elements in new array will be tuples with two values (first is index of position in original array, second is his value). For that purpose we use "_enumerate_" function when we sorting the orgininal array.
   After that we have only six element that we can itterate through in. So we make a set in wich we add all indexes of elements witch are selected (_selected_elements_). We started with the biggest value. To be selected an element, his index must be non-adjancent with all indexes in "_selected_elements_". The end of the day we return the biggest sum of three elements from that six.

## What I use in this code?
  First I need to generate an array filled with random numbers.  With that array i will check performance of my code. (_generate_random_array_)
  Second I need to measure time execution of each function. So i made a decorator to manage with that task. (_execution_time_)
  Finally I need to chek all solutions. So I use **Pytest** to check them. I made a couple of tests with expectet results and one with random big array to check performance of solution
  In that code I left some variables that you can change.
      _number_of_elements_ = default (550) - generated random elements in tested array
      _numbers_range_ = (-100000, 500000) - tis is range of numbers. smallest - biggest
      _maximum_delay_ = 1.5 - thist is maxim time limit for each function to be executed.

## **Example Test**

_Elements in tested array: 1000, bound: (-100000, 500000)_

_Execution time - (max_sum_cycles): 16.453s_
_Result: 1494656_

_Execution time - (max_sum_cycles_stop_cycles): 6.402s_
_Result: 1494656_

_Execution time - (max_sum_sorted_method): 0.001s_
_Result: 1494656_
