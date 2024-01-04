import threading
def even():
    lst_even=[]
    for i in range(30, 51):
        if i % 2 == 0:
            lst_even.append(i)
    print(f"Even: {lst_even}")

def odd():
    lst_odd=[]
    for i in range(30, 51):
        if i % 2 != 0:
            lst_odd.append(i)
    print(f"Odd: {lst_odd}")

t1 = threading.Thread(target=even)
t2 = threading.Thread(target=odd)

t1.start()
t2.start()

t1.join()
t2.join()
