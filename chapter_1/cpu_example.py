import time
import threading
import multiprocessing


def fib(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_sync():
    fib(40)
    fib(41)


def fib_threading():
    first_thread = threading.Thread(target=fib, args=(40, ))
    second_thread = threading.Thread(target=fib, args=(41, ))

    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()


def fib_multiprocessing():
    first_process = multiprocessing.Process(target=fib, args=(40, ))
    second_process = multiprocessing.Process(target=fib, args=(41, ))

    first_process.start()
    second_process.start()

    first_process.join()
    second_process.join()


sync_start_time = time.time()
fib_sync()
sync_end_time = time.time()
print(f'Синхронное выполнение CPU Bound программы заняло {sync_end_time - sync_start_time:.4f} секунд')

threading_start_time = time.time()
fib_threading()
threading_end_time = time.time()
print(f'Многопоточное выполнение CPU Bound программы заняло {threading_end_time - threading_start_time:.4f} секунд')

multiprocessing_start_time = time.time()
fib_multiprocessing()
multiprocessing_end_time = time.time()
print(f'Мультипроцессорное выполнение CPU Bound программы заняло '
      f'{multiprocessing_end_time - multiprocessing_start_time:.4f} секунд')


"""Возможный результат выполнения"""
# Синхронное выполнение CPU Bound программы заняло 86.4309 секунд
# Многопоточное выполнение CPU Bound программы заняло 114.7185 секунд
# Мультипроцессорное выполнение CPU Bound программы заняло 46.2637 секунд
