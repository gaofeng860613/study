from threading import Thread


class dask(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(5):
            print('奥特曼第{}次打小怪兽'.format(i))


if __name__ == '__main__':
    p = dask()
    p.start()