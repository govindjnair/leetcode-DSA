import threading
import time
from multiprocessing import Process, cpu_count


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())
    start_time = time.perf_counter()
    process1 = Process(target=counter, args=(20000000,))
    process2 = Process(target=counter, args=(20000000,))
    process3 = Process(target=counter, args=(20000000,))
    process4 = Process(target=counter, args=(20000000,))
    process5 = Process(target=counter, args=(20000000,))
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    end_time = time.perf_counter()
    print(end_time-start_time)


if __name__ == "__main__":
    main()


# def walk_dog():
#     time.sleep(8)
#     print("You finished walking the dog")
#
#
# def trash():
#     time.sleep(2)
#     print("You took out the trash")
#
#
# def mail():
#     time.sleep(4)
#     print("you got the mail")
#
#
# thread1 = threading.Thread(target=walk_dog, daemon=True)
# thread1.start()
#
# thread2 = threading.Thread(target=trash)
# thread2.start()
#
# thread3 = threading.Thread(target=mail)
# thread3.start()
#
# print(threading.active_count())
# print(threading.enumerate())
#
# thread1.join()
# thread2.join()
# thread3.join()
#
