'''
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

'''

















res = "1:34:02"
splited_res=res.split(":")
h = int(splited_res[0])
m = int(splited_res[1])
s = int(splited_res[2])
total_seconds = h*60 + m*60 + s
modulo_minutes = total_seconds%60
total_minutes = h*60 + m + s/60
total_hours = total_minutes/60
print(total_seconds)
print(total_minutes)
print(total_hours)
hm = 21.097
fm = 42.095
hm_speed_kmh = hm/total_hours
fm_speed_kmh = fm/total_hours
hm_speed_pace_mins_decimal_format = total_minutes/hm
fm_speed_pace_mins_decimal_format = total_minutes/fm
hm_speed_pace_mins_pace_format = str(hm_speed_pace_mins_decimal_format).split(".")
hm_speed_pace_mins_pace_format = str(hm_speed_pace_mins_pace_format[0]) + ":" + str(int(hm_speed_pace_mins_pace_format[1])*0.6)
fm_speed_pace_mins_pace_format = str(fm_speed_pace_mins_decimal_format).split(".")
fm_speed_pace_mins_pace_format = str(fm_speed_pace_mins_pace_format[0]) + ":" + str(int(fm_speed_pace_mins_pace_format[1])*0.6)
print(hm_speed_kmh)
print(fm_speed_kmh)
print(hm_speed_pace_mins_pace_format)
print(fm_speed_pace_mins_pace_format)
'''
ULTRA
'''
six_hours_duration = 6
twelve_hours_duration = 12
twenty_four_hours_duration = 24
six_hours_in_min = six_hours_duration * 60
twelve_hours_in_min = twelve_hours_duration * 60
twenty_four_hours_in_min = twenty_four_hours_duration * 60
