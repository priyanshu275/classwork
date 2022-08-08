import threading
import os


def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))


def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))


if __name__ == "__main__":

    print("ID of process running main program: {}".format(os.getpid()))


    print("Main thread name: {}".format(threading.current_thread().name))


    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')


    t1.start()
    t2.start()


    t1.join()
    t2.join()
#-----------------------FILEHANDLING--------------------------


file = open('sample.txt', 'r')
for each in file:
    print(each)

file = open("sample.txt", "r")
print (file.read())

file = open('samplw.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

#----------ENCAPSULATION------------
with open("file.text", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
