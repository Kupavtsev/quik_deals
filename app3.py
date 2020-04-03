# Version 3

file = open('032.txt', 'r')

# We create dict generator from lines
# and give the number to each line
d = {ix: line for ix, line in enumerate(file)}
for key, val in d.items():          # Выводит содержимое файла ввиде словаря
    print(key, '=>', val)

d_new = {}          

def side(d, line1, line2):              # Проверяем две подряд идущие строки по напровлению сделки
    side_first = d[line1][10:18]        # если разные, первая строка открытие позиции
    print(side_first)                    
    side_second = d[line2][10:18]
    print(side_second)
    if side_first != side_second:
        return True
    else: pass


if __name__ == '__main__':
    #while True:
        first  = side(d, 1, 2)              
        if first == True:                    
            d_new = d[1]                    # Помещаем в новый словарь строку окрытия позиции. Ключ сохраняется!!!
            d.pop(1)                        # Удаляем из словаря загруженного файла полученую строку полной позиции
            print(d_new)
            for key, val in d.items():
                print(key, '=>', val)

'''
if __name__ == '__main__':
Создание нового словаря сднлать через Цикл

'''