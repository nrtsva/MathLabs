import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def func(x) :
    return math.exp(-x)

def integral(func, a, b, n, metod) :
    sum = 0
    h = (b - a) / n
    start = a + (metod / 2) * h

    for i in range(n) :
        sum += func(start + i * h)
        ax.add_patch(
            patches.Rectangle(
                (i * h, 0),
                h,
                func(start + i * h),
                edgecolor = 'blue',
                facecolor = 'blue',
                fill = False
            ))

    return sum * h

def delta(n, metod) :
    if metod == 1 :
        return 1 / 3 / n**2
    else :
        return 2 / n

def data(res, n, metod) :
    s = "Integral ~ " + str(round(res, 3)) + "\n"
    a = str(round(math.fabs(-math.exp(-2) + 1 - res), 3))
    b = str(round(delta(n, metod), 3))
    s = s + "real delta = " + a + ", teor delta = " + b + "\n"
    s = s + "("
    if metod == 0:
        s = s + "left rectangles metod, "
    if metod == 1 :
        s = s + "middle rectangles metod, "
    if metod == 2:
        s = s + "right rectangles metod, "
    s = s + "n = " + str(n) + ")"
    return s

a = 0
b = 2
print("f(x) = e^(-x); [" + str(a) + ", " + str(b) + "]")
print("Input n(number of split points): ")
n = int(input())
print("Input metod:\n\t0 - left rectangles\n\t1 - medium rectangles\n\t2 - right rectangles")
metod = int(input())

fig, ax = plt.subplots()

# plot function graph
x = np.linspace(a, b, 100)
y_ideal = [func(a) for a in x]
ax.plot(x, y_ideal, color = "red")

res = integral(func, a, b, n, metod);

# plot X - axis
ax.axhline(y = 0, color = 'k')
# plot Y - axis
ax.axvline(x = 0, color = 'k')

plt.grid()
#plt.title("Integral ~ " + str(round(res, 3)) + "\n(" + ("left rectangles" if(metod == 0) else("middle rectangles" if (metod == 1) else "right rectangles")) + " metod, n = " + str(n) + ")")
plt.title(data(res, n, metod))
plt.show()