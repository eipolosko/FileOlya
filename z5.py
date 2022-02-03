# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('f5.txt','w+') as file5:
    s=input()
    file5.write(s)
    file5.seek(0)
    out_put=file5.read().split()
    out_put=[int(i) for i in out_put]
    sum_chisel=sum(out_put)
    print('Сумма чисел равна: ',sum_chisel)


