print('Привет! Как тебя зовут?')
a = input()
print('Хорошо ' + a + ' я загадал число, попробуй его отгадать')
import random
b = random.randint(1,20)
i=0
for i in range(6):
    c = int(input())
    if b == c:
        break
    if b>c:
        print ('Загаданное число немного больше')
    if c>b:
        print ('Загаданное число немного меньше') 
if b == c:
    print ('Поздравляю, Вам понадабилось '+ str(i+1) + ' попыток')
else:
    print ('Загаданное число равно', b)

