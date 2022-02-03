# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки,
# в расчёт средней прибыли её не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить её в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json
with open('f7.txt') as file7:
    s=file7.readlines()
    print(''.join(s))
    ar_str=[]
    sum_prib=0
    kol_f_prib=0
    dict_f={}
    dict_aver={}
    result=[]
    for i in s:
        i.split()
        ar_str.append(i.split())
    for a in ar_str:
        pribil=int(a[2])-int(a[3])
        if pribil>0:
            print(f'Прибыль {a[0]} составляет {pribil}')
            dict_f[a[0]]=pribil
            sum_prib+=pribil
            kol_f_prib+=1
        else:
            print(f'Фирма {a[0]} понесла убытки {-pribil}')
            dict_f[a[0]] = pribil
    aver=sum_prib/kol_f_prib
    print(f'Средняя прибыль всех компаний = {aver}')
    dict_aver['average_profit']=aver
    result.append(dict_f)
    result.append(dict_aver)
    print(result)
with open('result.json','w') as file7_1:
    json.dump(result, file7_1)




