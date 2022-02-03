# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на
# чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл
try:
    with open('f4.txt',encoding=('utf-8')) as file4:
        s=file4.readlines()
        print(''.join(s))
        ar_rus=['Oдин','Два','Три','Четыре']
        ar_en=['One','Two','Three','Four']
        result=[]
        num=0
        for i in s:
            k=i.replace(ar_en[num], ar_rus[num])
            result.append(k)
            num+=1
        #print(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
try:
    with open('f4.txt','w',encoding=('utf-8')) as file5:
       file5.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")




