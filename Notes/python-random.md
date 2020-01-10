import random as rd
# Return the next random floating point number in the range [0.0, 1.0).
rd.random()

rd.choice(["up", "down", "left", "right", "jump", "neer"])

rd.choices(["up", "down", "left", "right", "jump", "neer"], k=2)

# return [0, 500] random int value
rd.randint(0, 500)

# Return a randomly selected element from range(start, stop, step).
rd.randrange(0, 500, 6)

# 搅乱序列(可变)
x = ["up", "down", "left", "right", "jump", "neer"]
rd.shuffle(x)
print(x)

# 搅乱序列(不可变)
# Return a k length list of unique elementsd
# chosen from the population sequence or set.
# Used for random sampling without *replacement*.
tmp = ("up", "down", "left", "right", "jump", "neer")
rd.sample(tmp, 2)


# mark
# random.triangular(low, high, mode)
# Return a random floating point number N such that low <= N <= high and with the specified mode between those bounds. The low and high bounds default to zero and one. The mode argument defaults to the midpoint between the bounds, giving a symmetric distribution.

# random.betavariate(alpha, beta)
# Beta distribution. Conditions on the parameters are alpha > 0 and beta > 0. Returned values range between 0 and 1.

# random.expovariate(lambd)
# Exponential distribution. lambd is 1.0 divided by the desired mean. It should be nonzero. (The parameter would be called “lambda”, but that is a reserved word in Python.) Returned values range from 0 to positive infinity if lambd is positive, and from negative infinity to 0 if lambd is negative.
#指数

# random.gammavariate(alpha, beta)
# Gamma distribution. (Not the gamma function!) Conditions on the parameters are alpha > 0 and beta > 0.

# The probability distribution function is:

#           x ** (alpha - 1) * math.exp(-x / beta)
# pdf(x) =  --------------------------------------
#             math.gamma(alpha) * beta ** alpha
# random.gauss(mu, sigma)
# Gaussian distribution. mu is the mean, and sigma is the standard deviation. This is slightly faster than the normalvariate() function defined below.
# 高斯

# random.lognormvariate(mu, sigma)
# Log normal distribution. If you take the natural logarithm of this distribution, you’ll get a normal distribution with mean mu and standard deviation sigma. mu can have any value, and sigma must be greater than zero.
# 正态分布

# random.normalvariate(mu, sigma)
# Normal distribution. mu is the mean, and sigma is the standard deviation.

# random.vonmisesvariate(mu, kappa)
# mu is the mean angle, expressed in radians between 0 and 2*pi, and kappa is the concentration parameter, which must be greater than or equal to zero. If kappa is equal to zero, this distribution reduces to a uniform random angle over the range 0 to 2*pi.

# random.paretovariate(alpha)
# Pareto distribution. alpha is the shape parameter.
# 帕累托分布

# random.weibullvariate(alpha, beta)
# Weibull distribution. alpha is the scale parameter and beta is the shape parameter.
# 威布尔分布