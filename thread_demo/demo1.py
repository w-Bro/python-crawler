import time
import threading


def coding():
    for x in range(3):
        print('正在写代码%s' % threading.current_thread())
        time.sleep(1)


def drawing():
    for x in range(3):
        print('正在写画图%s' % threading.current_thread())
        time.sleep(1)


def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()

    # 线程数
    print(threading.enumerate())


if __name__ == '__main__':
    main()