# input

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

totalMinutes = (hour * 60) + mins + dura
fHour = totalMinutes // 60
fMins = totalMinutes % 60

print(fHour)
print(fMins)
