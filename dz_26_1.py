from scipy.stats import norm

# Задані параметри
p = .9
n = 50
mu = n * p
sigma = (n * p * (1 - p)) ** .5

# Обчислення ймовірності
lower_bound = .85 * n
upper_bound = .95 * n
p_within_bounds = norm.cdf(upper_bound, mu, sigma) - norm.cdf(lower_bound, mu, sigma)

# Виведення результату
print("Ймовірність того, що число телевізорів, які витримають гарантійний термін роботи буде в межах [{}, {}]: {:.2f}%".format(lower_bound, upper_bound, p_within_bounds * 100))
