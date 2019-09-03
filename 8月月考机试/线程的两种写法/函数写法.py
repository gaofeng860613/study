from threading import Thread


def dask():
    for i in range(5):
        print('奥特曼第{}次打小怪兽'.format(i))


if __name__ == '__main__':
    p = Thread(target=dask)
    p.start()
