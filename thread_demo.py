import threading

class Factoriel (threading.Thread):
    def __init__(self, number, name):
        threading.Thread.__init__(self)
        self.number = number
        self.name = name

    def run(self):
        print(f"Thread naziva  {self.name} je pokrenut")
        factoriel = 1
        for i in range(1, self.number + 1): # start 0, end , korak 1
            factoriel = factoriel * i
        print(f"Factorial broja {self.number} je {factoriel}.")
        print(f"Thread naziva {self.name} je zavrsio.")


print("Start DEFAULT Thread")
thread1 = Factoriel(1111)
thread2 = Factoriel(10)
thread3 = Factoriel(1000)

thread1.start()
thread2.start()
thread3.start()
print("DEFAULT thread je završio")



















#res = "2:21:17"
#splited_res=res.split(":")
#h = splited_res[0]
#print(h)





