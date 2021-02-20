import timeit
 

def abc():
    for _ in range(1000):
        pass


def abc2():
    for _ in range(10000):
        pass


a = timeit.timeit(abc, number=10)
print(a)

b = timeit.timeit(abc2, number=10)
print(b)
