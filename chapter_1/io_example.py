import time
import threading
import multiprocessing


def sleep_for_20_sec():
    time.sleep(20)


def fib_sync():
    sleep_for_20_sec()
    sleep_for_20_sec()


def fib_threading():
    first_thread = threading.Thread(target=sleep_for_20_sec)
    second_thread = threading.Thread(target=sleep_for_20_sec)

    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()


def fib_multiprocessing():
    first_process = multiprocessing.Process(target=sleep_for_20_sec)
    second_process = multiprocessing.Process(target=sleep_for_20_sec)

    first_process.start()
    second_process.start()

    first_process.join()
    second_process.join()


sync_start_time = time.time()
fib_sync()
sync_end_time = time.time()
print(f'Синхронное выполнение IO Bound программы заняло {sync_end_time - sync_start_time:.4f} секунд')

threading_start_time = time.time()
fib_threading()
threading_end_time = time.time()
print(f'Многопоточное выполнение IO Bound программы заняло {threading_end_time - threading_start_time:.4f} секунд')

multiprocessing_start_time = time.time()
fib_multiprocessing()
multiprocessing_end_time = time.time()
print(f'Мультипроцессорное выполнение IO Bound программы заняло '
      f'{multiprocessing_end_time - multiprocessing_start_time:.4f} секунд')


"""Возможный результат выполнения"""
# Синхронное выполнение IO Bound программы заняло 40.0376 секунд
# Многопоточное выполнение IO Bound программы заняло 20.0207 секунд
# Мультипроцессорное выполнение IO Bound программы заняло 20.0869 секунд
