from multiprocessing import Process

a = 0


def dask1():
    global a
    for i in range(10):
        a += 1
    print(a)


def dask2():
    global a
    for i in range(10):
        a += 2
    print(a)


if __name__ == '__main__':
    p1 = Process(target=dask1)
    p2 = Process(target=dask2)
    p1.start()
    p2.start()
