# 1
a = input("Введите свое имя => ")
print(a)
b = int(input("Ведите свой возраст => "))
print(b)
#2
x = int(input("Введите время в секундах => "))
sec = x % 3600
min = sec // 60
seconds = sec % 60
print("hour", hour)
print("minute", min)
print("seconds", seconds)
#3
y = int(input("Введите число от 1 до 9 => "))
t = str(y)
t1 = t + t
t2 = t + t + t
total = y + int(t1) + int(t2)
print(total)
#4
f = int(input("Введите целое положительное число => "))
m = 0
while(f):
       if(f % 10 > m):
        m = f % 10
       f //= 10
print(m)
#5-6
v = float(input("Величина выручки? => "))
c = float(input("Величина издержек? => "))
p = int(input("Введите количество работников => "))
if v > c:
    print("Предприятие работает с прибылью")
    prof = ((v - c) / v )
    print("рентабельность = ", prof)
    d = (v-c) / p
    print("величина прибыли, приходящаяся на одного работника = ", d)
else:
    print("Предприятие убыточное")
