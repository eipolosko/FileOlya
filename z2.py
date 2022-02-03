# Создать текстовый файл (не программно),
# сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('f2.txt','r') as file2:
    s=file2.readlines()
    print(''.join(s))
    print(f'Количество строк = {len(s)}')
    k=1
    for i in s:
        count_words=len(i.split())
        print(f'Количество cлов в {k} строке  = { count_words}')
        k+=1
