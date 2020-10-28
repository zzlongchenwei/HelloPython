import threading
from contextlib import contextmanager

# Thread-local state to stored information on locks already acquired
_local = threading.local()


@contextmanager
def acquire(*locks):
    # Sort locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))

    # Make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local, 'acquired', [])  # equivalent to _local.acquired, return[]
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):  # if acquired is none and max id(lock) >= id(0)
        raise RuntimeError('Lock Order Violation')  # raise error

    # Acquire all of the locks
    acquired.extend(locks)  # append all lock to []
    _local.acquired = acquired  # assign value to attribute

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # Release locks in reverse order of acquisition
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


# import threading
# x_lock = threading.Lock()
# y_lock = threading.Lock()
#
# def thread_1():
#     while True:
#         with acquire(x_lock, y_lock):
#             print('Thread-1')
#
# def thread_2():
#     while True:
#         with acquire(y_lock, x_lock):
#             print('Thread-2')
#
# t1 = threading.Thread(target=thread_1)
# t1.daemon = True
# t1.start()
#
# t2 = threading.Thread(target=thread_2)
# t2.daemon = True
# t2.start()

x_lock = threading.Lock()
y_lock = threading.Lock()


def thread_1():
    while True:
        with acquire(x_lock):
            with acquire(y_lock):
                print('Thread-1')


def thread_2():
    while True:
        with acquire(y_lock):
            with acquire(x_lock):
                print('Thread-2')


t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()
