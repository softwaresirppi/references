let f(x) be a function. 

To find some value that could make f(value) = 0.
in other words. To find (inverse of f)(0)
guess some value.
better guess = guess - f(guess) / f'(guess)
repeat this till satisfied.


EXAMPLE:
to find sqrt(2).
x = sqrt(2)
x^2 = 2
x^2 - 2 = 0
LET f(x) = x^2 - 2
f'(x) = 2x

better guess
    = guess - (x^2 - 2) / 2x
    = guess - (x^2/2x - 2/2x)
    = guess - (x/2 - 1/x)

guess = 2
better guess = 1.5
better guess = 1.416
better guess = 1.414
...


To find square root of x,
better guess = (guess + x/guess) / 2
to find cube root of x,
better guess = (2*guess + x/guess^2) / 3
to find fourth root of x,
better guess = (3*guess + x/guess^3) / 4
...
to find nth root of x,
better guess = ((n - 1) * guess + x/guess^(n - 1)) / n
