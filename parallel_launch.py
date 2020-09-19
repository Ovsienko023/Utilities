import concurrent.futures
import time


def test1(name):
    print("Начало функции", name)
    time.sleep(2)
    print("Конец функции", name)

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor: # ThreadPoolExecutor(max_workers=3)
        # for i in range(5):
            # executor.submit(test1) # submit(test1, args)
        executor.submit(test1, 1)
        executor.submit(test1, 2)
        executor.submit(test1, 3)

main()
