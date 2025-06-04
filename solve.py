epsilon = 0.0001
def slope(f, x):
    return (f(x + epsilon/2) - f(x - epsilon/2)) / epsilon

def solve(guess, f):
    delta = f(guess) / slope(f, guess)
    if abs(delta) < epsilon:
        return guess
    return solve(guess - delta, f)

print(round(solve(0, lambda x: x), 4))
