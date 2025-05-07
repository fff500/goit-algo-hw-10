import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Аналітичний інтеграл
def f(x):
    return x**2 + x + 2

a = 0
b = 2

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

result, error = spi.quad(f, a, b)
print("Аналітичний інтеграл: ", result, error)

# Метод Монте-Карло
N = 10000
random_x = np.random.uniform(a, b, N)
value = f(random_x)
monte_carlo = (b - a) * np.mean(value)
print("Інтеграл функції за методом Монте-Карло:", monte_carlo)

#Графік
fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 + x + 2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
