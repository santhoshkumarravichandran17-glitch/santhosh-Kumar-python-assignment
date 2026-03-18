
fp = open("students.txt", "w")

fp.write("1 Dinesh\n")
fp.write("2 Kumar\n")

fp.close()

print("Written successfully")

fp = open("students.txt", "r")

data = fp.read()
print(data)

fp.close()


import threading
import time

def write_data():
    fp = open("students.txt", "w")
    fp.write("1 Dinesh\n")
    time.sleep(1)
    fp.write("2 Kumar\n")
    time.sleep(1)
    fp.close()
    print("Writing done")

def read_data():
    time.sleep(2)
    fp = open("students.txt", "r")
    print(fp.read())
    fp.close()
    print("Reading done")

t1 = threading.Thread(target=write_data)
t2 = threading.Thread(target=read_data)

t1.start()
t2.start()
