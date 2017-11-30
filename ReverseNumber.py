def reversenumber(number):
    global reverse #объявим глобальную переменую,которая равна нулю
    if number == 0: #выход из рекурсии, когда число равняется нулю
        reverse, result = 0, reverse #назначаем переменной reverse ноль, чтобы использовать при повторном вызове функции, а переменной result присваеваем результат функции
        return(print(result)) #вывод результата
    lastdigit = number % 10 #присваемваем переменной lastdigit последнюю цифру входного числа number
    reverse = (reverse * 10) + lastdigit #записываем реверсивное число
    number = reversenumber(number//10) #здесь начинается рекурсия, из числа удаляется последняя цифра, чтобы выбрать следуещюю цифру из числа и записать в переменную reverse

reverse = 0 #просто переменная для функции
#тестим
reversenumber(1234)
reversenumber(223322)
reversenumber(1)
reversenumber(0)
reversenumber(554325)
reversenumber(987654321)
