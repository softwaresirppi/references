f(x) = SUMMATION OF ((x - c) ** i) * diff-i-times(f)(c) / i!
where i = [0...infinity)

sin(x) = SUMMATION OF ((x) ** i) * diff-i-times(sin)(0) / i!
where i = [0...infinity)

DIFFERENTIATION CHAIN: cos -> -sin -> -cos -> sin

sin(x)
  = x ** 0 * sin(0) / 0! + x ** 1 * cos(0) / 1! + x ** 2 * -sin(0) / 2! + x ** 3 * -cos(0) / 3! + ...
  = x ** 1 * 1 / 1! + x ** 3 * -1 / 3! + x ** 5 * 1 / 5! + x ** 7 * -1 / 7! + ...
  = x - x ** 3 / 3! + x ** 5 / 5! - x ** 7 / 7! + ...
