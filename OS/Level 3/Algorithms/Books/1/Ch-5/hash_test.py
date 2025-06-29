import random
import time

"""
This python file contains my self written implementation of Measuring Python List and Dict (Hash) on Indexing data.
This is not part of book. Rather my Experiment.
"""

n = 10000000

list_test1 = [random.randint(0, n) for i in range(n)]
hash_test1 = {i: list_test1[i] for i in range(n)}

print("Length : ", len(list_test1), len(hash_test1))

list_time = 0
hash_time = 0
for i in range(1000000):
    index = random.randint(0, n)
    st1 = time.time()
    val1 = list_test1[index]
    ed1 = time.time()

    st2 = time.time()
    val2 = hash_test1[index]
    ed2 = time.time()
    list_time += ed1-st1
    hash_time += ed2-st2


print("List Time : ", list_time)
print("Hash Time : ", hash_time)

