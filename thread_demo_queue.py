import queue
import threading
import socket
import sqlite3

numbers = [100, 111112, 50, 9, 1578]
data_queue = queue.Queue()
end_thread = False

for number in numbers:
    data_queue.put(number)

class Factoriel(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue

    def run(self):
        print(f"Thread naziva {self.name} ({self.ident}) je pokrenut!")
        local_variables = threading.local()

        while not end_thread:
            local_variables.number = self.queue.get()
            local_variables.factoriel = 1

            for i in range(1, local_variables.number + 1):
                local_variables.factoriel *= i

            print(f"Factoriel broja {local_variables.number} je izračunat - vjerujte mi - {self.name}.")

        print(f"Thread naziva {self.name} je završio.")

print("Start DEFAULT thread")
thread1 = Factoriel("1. thread", data_queue)
thread2 = Factoriel("2. thread", data_queue)
thread3 = Factoriel("3. thread", data_queue)


thread1.start()
thread2.start()
thread3.start()


while not data_queue.empty():
    pass

end_thread = True


print("DEFAULT thread je završio.")