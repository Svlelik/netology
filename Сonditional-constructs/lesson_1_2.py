# a = 10 + 20
# b = a * 30
# c = a / b
# print('Ответ,', c)

# print(x)

# x = 10

# print(2 > 1)
# print(10 < 6)
# print(10 > 10)
# print(10 >= 10)
# print(7 == 7)
# print(15 != 15)

# print(10 < 5 < 3)
# print(3 < 5 < 10)

# my_comparison = 7 < 3

# print(my_comparison)


# print('c' > 'a')
# print('b' > 'B')
# print('abc' > 'aba')

# print(len('abc') > len('aba'))


# print(True and False)
# print(False and False)
# print(True and True)
# print(True or False)
# print(not True)

# print(9 > 7 and 2 < 4)
# print(8 == 8 or 6 != 6)
# print((8 == 7 or 6 != 6) and 9 > 7)

# print(not(9 > 6) and 5 > 3 or 2 < 4)

# x = 6
# if x % 2 == 0: 
#   print(x, '- четное число')
# else:
#   print(x, '- нечетное число')

# height = 205
# age = 25



# if 18 <= age < 27:
#   if height < 170:
#     print('В танкисты')
#   elif height < 185:
#     print('На флот')
#   elif height < 200:
#     print('В десантники')
#   else:
#     print('В другие войска')
# else:
#   print('Непризывной возраст')

# name = input('Введите имя')

# if name:
#   print('Привет', name)
# else:
#   print('Привет, Мир!')

# number = int(input('Введите число'))

# if number:
#   print('Число равно:', number)
# else:
#   print('Число равно нулю')

# Дана переменная, в которой хранится шестизначное число (номер проездного билета). Напишите программу, которая будет определять, является ли данный билет "счастливым". Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера

# number = int(input('Введите номер билета'))

number = 123456

a = number // 100000
print(a)
b = number // 10000 % 10
print(b)
c = number // 1000 % 10
print(c)
d = number // 100 % 10
print(d)
# a = number % 10
# number = number//10
# print(a)
# b = number % 10
# number = number//10
# print(b)
# c = number % 10
# number = number//10
# print(c)
# d = number % 10
# number = number//10
# print(d)
# v = number % 10
# number = number//10
# print(v)
# e = number % 10
# print(e)
# if a+b+c == d+v+e:
#   print('Счастливое')
# else:
#   print('Не счастливое')

if a + b + c == d + v + e:
  print('Счастливый билет')
else:
  print(...)