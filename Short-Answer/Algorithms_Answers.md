#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
O(C), it does not matter how big n gets, the number of operations will not change at all, even if n is 9 million

b)
O(n), each time the input size increases, the number of operations increases by factor of 3

c)
O(n log n), bunnyEars is a recursive function and the number of operations increase slightly more with input size than a linear function

## Exercise II

The best way to find out what floor f is, is to start from the lowest floor and repeatedly drop egg(s) until it breaks.
this can be done recursively or iteratively. the base case would be broken egg. and each floor would drop and go up until that case is reached. the runtime is probably O(n log n) since you would be using recursion.

def egg_game(n):
<!-- broken egg count -->
count = 0
<!-- Base Case: broken egg -->
if n == f:
<!-- break -->
count += 1
return count
<!-- what if n starts out too high? -->
elif n > f:
<!-- break -->
count +=1
return egg_game(n-1)
<!-- not the base case? go up to the next floor -->
return egg_game(n+1)
