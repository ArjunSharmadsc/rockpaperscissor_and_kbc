import time
print(" here is the time time module along with the time \n")
timestamp= time.strftime('%H:%M:%S')
print(timestamp)
timestamp= time.strftime('%H')
print(timestamp)
timestamp= time.strftime('%M')
print(timestamp)

if int(time.strftime('%H') )< 12:
    print("good morning sir")
elif int(time.strftime('%H'))>=12 | int(time.strftime('%H') )<= 18:
    print("good evening sir")
else:
    print("print good night sir")