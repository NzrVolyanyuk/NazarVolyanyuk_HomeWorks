'''Задание 1
Пользователь вводит с клавиатуры число в диапазоне от 1 до 100.
Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
Если число кратно 5 нужно вывести слово Buzz.
Если число кратно 3 и 5 нужно вывести Fizz Buzz.
Если число не кратно не 3 и 5 нужно вывести само число.
Если пользователь ввел значение не в диапазоне от 1 до 100 требуется вывести сообщение об ошибке.'''

# number_user = 16
# if number_user > 0 and number_user <= 100:
#     if number_user % 3 == 0 and number_user % 5 == 0:
#         print("Fizz Buzz")
#     elif number_user % 3 == 0:
#         print("Fizz")
#     elif number_user % 5 == 0:
#         print("Buzz")
#     else:
#         print(number_user)
# else:
#     print("error")

'''Задание 2
Написать программу, которая по выбору пользователя возводит введенное им число в степень 
от нулевой до седьмой включительно.'''

user_number = 2
user_st = 7

if user_st >= 0 and user_st < 8:
    print(user_number ** user_st)