import math
import matplotlib.pyplot as plt

n = 0
run_time1 = lambda n: math.log2(n) # O(log n)
run_time2 = lambda n: n # O(n)
run_time3 = lambda n : math.log2(n) * n # O(n log n)
run_time4 = lambda n : n**2 # O(n^2)
run_time5 = lambda n : math.factorial(n) # O(n!)

def growth_rate(n):
    input_sizes = [i for i in range(1, n+1)]
    x = []
    rt1, rt2, rt3, rt4, rt5 = [], [], [], [], []
    for n in input_sizes:
        x.append(n)
        rt1.append(run_time1(n))
        rt2.append(run_time2(n))
        rt3.append(run_time3(n))
        rt4.append(run_time4(n))
        rt5.append(run_time5(n))

    plt.plot(x, rt1, label="O(log n)")
    plt.plot(x, rt2, label="O(n)")
    plt.plot(x, rt3, label="O(n * log n)")
    plt.plot(x, rt4, label="O(n^2)")
    plt.plot(x[:7], rt5[:7], label="O(n!)")
    plt.xlabel("n -> Size of the input")
    plt.ylabel("Rate of growth of O(Big-Oh)")
    plt.legend()
    plt.show()


growth_rate(50)
