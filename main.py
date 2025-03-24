def z1():
    s = [1,228,666,5,4]
    a = int(input('угадайте число: '))
    if a in s:
        print('Поздравляю, вы угадали число!')
    else:
        print('Нет такого числа!')


from random import *
def z2():

    s = [randint(1, 20) for x in range(5)]
    print(s)
    k = []
    m = 0
    for i in range(len(s)):
        for j in range((len(s)-1)-m):
            if s[i] == s[j+1 + m]:
                k += [s[i]]
        m += 1

    if len(k) == 0:
        print('повторяющихся нет')
    else:
        print(k)

def z3():
    dn = ('Понедельник', 'Вторник', "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    a = int(input('Сколько дней выходных?'))
    print("Ваши выходные дни - ", dn[-a:])
    print("Ваши рабочие дни : ", dn[:-a])

def z4():
    g1 = ['Иванов', 'Петров', 'Иванов', 'Лукашенко', 'Путин', 'Трамп', 'Гоша', 'Ленин', 'Стетхем', 'Дикаприо']
    g2 = ['Сталоне', 'Шварцнегер', 'Гослинг', "Мэддисон", "Озон", "Забубенский","1","2","3","4"]
    shuffle(g1)
    shuffle(g2)
    sport = tuple(g1[:5] + g2[:5])
    print('1-я группа : ', *g1)
    print('2-я группа: ', *g2)
    print ('Спортивная команда : ', sport)
    print(len(sport))
    print(*sorted(sport))
    if 'Иванов' in sport:
        print('Иванов есть')
        if sport.count('Иванов') > 1:
            print('аж целых ', sport.count('Иванов') )
        else:
            print('Но он один')
    else:
        print('Иванова нет')

a = int(input('Введите номер задания'))
if a == 1: z1()
if a == 2: z2()
if a == 3: z3()
if a == 4: z4()