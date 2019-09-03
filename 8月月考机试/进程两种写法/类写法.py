from multiprocessing import Process


class dask(Process):
    def __init__(self):
        Process.__init__(self)

    def run(self):
        for i in range(5):
            print('奥特曼第{}次打小怪兽'.format(i))


if __name__ == '__main__':
    p = dask()
    p.start()
